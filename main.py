import schedule
import time
import csv
from datetime import datetime
from cpu_kpis import get_cpu_kpi
from disk_io import get_disk_io
from docker_info import Docker_collecter
from gpu_kpis import get_gpu_kpis
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


header = ['timestamp',  # 1
          'cpu_load', 'avg_temp_cpu', 'cpu_numbers', 'IPS', 'CPS', 'queue_length', 'pid_count',  # 7
          'gpu_numbers', 'avg_gpu_temperature',  # 2
          'ram_percent',  # 1
          'swap_total', 'swap_percent',  # 1
          'disk_utilization', 'disk_latency', 'disk_temperature',  # 3
          'docker_container'  # 1
          ]  # 16

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
