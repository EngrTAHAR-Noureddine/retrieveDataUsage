import schedule
import csv
from datetime import datetime
import psutil
import time
import docker
import GPUtil


# DOKER
class Docker_collecter:
    def __init__(self):
        self.client = docker.from_env()

    def get_container_count(self):
        try:
            containers = len(self.client.containers.list())
        except Exception:
            containers = 0
        return containers


# CPU
def get_cpus():
    try:
        counters = psutil.cpu_count()
    except Exception:
        counters = 0
    return counters


def get_cpu_kpi():
    cpus_percent = []
    if get_cpus() > 0:
        cpus_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_load = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=False)
    queue_length = (cpu_load / 100) * cpu_count
    # get IPS and CPS
    cpu_state = psutil.cpu_stats()
    interrupts1, ctx_switches1 = cpu_state.interrupts, cpu_state.ctx_switches
    time.sleep(1)
    cpu_state = psutil.cpu_stats()
    interrupts2, ctx_switches2 = cpu_state.interrupts, cpu_state.ctx_switches
    ips = (interrupts2 - interrupts1) / 1
    cps = (ctx_switches2 - ctx_switches1) / 1
    ips = abs(ips)
    cps = abs(cps)
    # cpus_percent, cpu_load, ips, cps, queue_length, pid_count
    return cpus_percent + [cpu_load, ips, cps, queue_length, pid_count()]


def pid_count():
    try:
        num_pid = len(psutil.pids())
    except Exception:
        num_pid = None
    return num_pid


# GPU
def get_gpus():
    try:
        gpus = len(GPUtil.getGPUs())
    except Exception:
        gpus = 0
    return gpus


def get_gpu_kpis():
    gpus = GPUtil.getGPUs()
    gpu_percent = []
    for gpu in gpus:
        gpu_percent.append(gpu.load * 100)
    return gpu_percent


# RAM
def get_ram_kpis():  # In MB
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_total = ram.total / 1024 / 1024
    ram_available = ram.available / 1024 / 1024
    free_ram = ram.free / 1024 / 1024
    used_ram = ram.used / 1024 / 1024

    return [ram_percent, ram_total, used_ram, ram_available, free_ram]


# SWAP
def get_swap_kpis():  # In MB
    swap = psutil.swap_memory()
    swap_percent = swap.percent
    swap_total = swap.total / 1024 / 1024
    free_swap = swap.free / 1024 / 1024
    used_swap = swap.used / 1024 / 1024
    return [swap_percent, swap_total, used_swap, free_swap]


# WRITE IN CSV FILE
def write_to_csv(file_path, data):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


# DISK I/O
def get_disk_latency():
    # Get disk I/O counters for the first time
    io_counters_start = psutil.disk_io_counters()

    # Wait for a short interval to capture the change in disk I/O counters
    time.sleep(1)

    # Get disk I/O counters again after the interval
    io_counters_end = psutil.disk_io_counters()

    # Calculate the busy_time (disk latency) as the difference between read_time and write_time
    read_time_diff = io_counters_end.read_time - io_counters_start.read_time
    write_time_diff = io_counters_end.write_time - io_counters_start.write_time
    busy_time = read_time_diff + write_time_diff

    return busy_time


def get_disk_io():
    disk_latency = get_disk_latency()
    disk_utilization = psutil.disk_usage('/').percent
    disk_io_counters = psutil.disk_io_counters()
    read_count = disk_io_counters.read_count
    write_count = disk_io_counters.write_count
    read_bytes = disk_io_counters.read_bytes / 1024 / 1024
    write_bytes = disk_io_counters.write_bytes / 1024 / 1024
    return [disk_utilization, disk_latency, read_count, read_bytes, write_count, write_bytes]


# RECORD DATA
def record_system_usage():
    global docker_info
    cpu_kpis = get_cpu_kpi()
    gpu_kpis = get_gpu_kpis()
    ram_kpis = get_ram_kpis()
    swap_kpis = get_swap_kpis()
    disk_io = get_disk_io()

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [current_time] + cpu_kpis + gpu_kpis + ram_kpis + swap_kpis + disk_io + [docker_info.get_container_count()]
    write_to_csv('system_usage.csv', data)


header = ['timestamp']

if get_cpus() > 0:
    header = header + [f'cpu_{i}_usage' for i in range(get_cpus())]

header = header + ['cpu_load', 'IPS', 'CPS', 'queue_length', 'pid_count']

if get_gpus() > 0:
    header = header + [f'gpu_{i}_usage' for i in range(get_gpus())]

header = header + ['ram_percent', 'ram_total', 'ram_used', 'ram_available', 'ram_free', 'swap_percent', 'swap_total',
                   'swap_used', 'swap_free', 'disk_utilization','disk_latency', 'read_count', 'read_bytes', 'write_count', 'write_bytes', 'docker_container']

write_to_csv('system_usage.csv', header)
schedule.every(5).minute.do(record_system_usage)

docker_info = Docker_collecter()

while True:
    schedule.run_pending()
    time.sleep(1)

# TODO: get Response Time and Error Rates , Request or Transaction Rates
