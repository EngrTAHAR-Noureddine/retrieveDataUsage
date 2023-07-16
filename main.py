import psutil
import GPUtil
import schedule
import time
import csv
from datetime import datetime


def get_cpu_usage():
    cpus_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_load = psutil.cpu_percent(interval=1)
    return cpus_percent, cpu_load


def get_cpu_queue_length():
    cpu_count = psutil.cpu_count(logical=False)
    cpu_percent_avg = psutil.cpu_percent(interval=1)
    # Estimate the CPU Queue Length
    queue_length = (cpu_percent_avg / 100) * cpu_count
    return queue_length


#  Interrupts per Second (IPS)
def calculate_ips(interval=1):
    interrupts1 = psutil.cpu_stats().interrupts
    time.sleep(interval)
    interrupts2 = psutil.cpu_stats().interrupts
    ips = (interrupts2 - interrupts1) / interval
    return abs(ips)


def calculate_cps(interval=1):
    ctx_switches1 = psutil.cpu_stats().ctx_switches
    time.sleep(interval)
    ctx_switches2 = psutil.cpu_stats().ctx_switches
    cps = (ctx_switches2 - ctx_switches1) / interval
    return abs(cps)


def get_ram_usage():
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    return ram_percent


def memory_usage():
    memory_utilization = psutil.virtual_memory().percent
    available_memory = psutil.virtual_memory().available / 1024 / 1024
    memory_paging = psutil.swap_memory()
    memory_paging_total = memory_paging.total / 1024 / 1024
    memory_paging_used = memory_paging.used / 1024 / 1024
    memory_paging_free = memory_paging.free / 1024 / 1024
    swap_utilization = memory_paging.percent
    page_faults = psutil.virtual_memory().page_faults

    return [memory_utilization, available_memory, memory_paging_total, memory_paging_used, memory_paging_free,
            swap_utilization, page_faults]

def disk_usage():
    disk_utilization = psutil.disk_usage('/').percent
    disk_io_counters = psutil.disk_io_counters()
    read_count = disk_io_counters.read_count
    write_count = disk_io_counters.write_count
    read_mb = disk_io_counters.read_bytes / 1024 / 1024
    write_mb = disk_io_counters.write_bytes / 1024 / 1024
    disk_latency = psutil.disk_io_counters().busy_time / psutil.disk_io_counters().read_count


def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    gpu_percent = []
    for gpu in gpus:
        gpu_percent.append(gpu.load * 100)
    return gpu_percent


def write_to_csv(file_path, data):
    with open(file_path, mode='a', newline='') as file:
        print("Write done")
        writer = csv.writer(file)
        writer.writerow(data)


def record_system_usage():
    cpus_percent, cpu_load = get_cpu_usage()
    ram_usage = get_ram_usage()
    gpu_usage = get_gpu_usage()
    ips = calculate_ips()
    cps = calculate_cps()
    cpu_queue_length = get_cpu_queue_length()
    # Memory
    memory_info_list = memory_usage()

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [current_time] + cpus_percent + [cpu_load, cpu_queue_length, ram_usage, ips,
                                            cps] + gpu_usage + memory_info_list
    write_to_csv('system_usage.csv', data)


header = ['timestamp'] + [f'cpu_{i}_usage' for i in range(psutil.cpu_count())] + ['cpu_load', 'cpu_queue', 'ram_usage',
                                                                                  "IPS",
                                                                                  "CPS"] + [
             f'gpu_{i}_usage' for i in range(len(GPUtil.getGPUs()))] + ['memory_utilization', 'available_memory',
                                                                        'memory_paging_total', 'memory_paging_used',
                                                                        'memory_paging_free',
                                                                        'swap_utilization', 'page_faults']
write_to_csv('system_usage.csv', header)

schedule.every(5).seconds.do(record_system_usage)

while True:
    schedule.run_pending()
    time.sleep(1)
