import schedule
import time
import csv
from datetime import datetime
from cpu_kpis import get_cpus, get_cpu_kpi
from disk_io import get_disk_io
from docker_info import Docker_collecter
from gpu_kpis import get_gpus, get_gpu_kpis
from ram_kpis import get_ram_kpis, get_swap_kpis

file_csv_path = "system_usage.csv"


def write_to_csv(file_path, data):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def record_system_usage():
    global docker_info, file_csv_path
    cpu_kpis = get_cpu_kpi()
    gpu_kpis = get_gpu_kpis()
    ram_kpis = get_ram_kpis()
    swap_kpis = get_swap_kpis()
    disk_io = get_disk_io()

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [current_time] + cpu_kpis + gpu_kpis + ram_kpis + swap_kpis + disk_io + [docker_info.get_container_count()]
    write_to_csv(file_csv_path, data)


header = ['timestamp']

if get_cpus() > 0:
    header = header + [f'cpu_{i}_usage' for i in range(get_cpus())]

header = header + ['cpu_load', 'IPS', 'CPS', 'queue_length', 'pid_count']

if get_gpus() > 0:
    header = header + [f'gpu_{i}_usage' for i in range(get_gpus())]

header = header + ['ram_percent', 'ram_total', 'ram_used', 'ram_available', 'ram_free', 'swap_percent', 'swap_total',
                   'swap_used', 'swap_free', 'disk_utilization','disk_latency', 'read_count', 'read_bytes', 'write_count', 'write_bytes', 'docker_container']

write_to_csv(file_csv_path, header)
schedule.every(5).minutes.do(record_system_usage)

docker_info = Docker_collecter()

while True:
    schedule.run_pending()
    time.sleep(1)

# TODO: get Response Time and Error Rates , Request or Transaction Rates
# 17:10 - 17:24 - running android studio and application
# 17:25 running xcode and ios simulator
# 17:32 running xcode using code
# 17:35 run app ios
# 17:40 stop xcode and simulator and app and android studio
# 18:33 sleep mode of computer
# 18:40 open computer
# 00:20 sleep system
# 09:53 open system


# 17:15 lancit les robots
# 23/07 09:14 stop emulators