import psutil


def get_avg_cpu_temperature():
    cpu_temp_values = []
    try:
        temperatures = psutil.sensors_temperatures()
        if "coretemp" in temperatures:
            cpu_temperatures = temperatures["coretemp"]
            cpu_temp_val = [entry.current for entry in cpu_temperatures if "Package id 0" in entry.label]
            cpu_temp_values = cpu_temp_values + cpu_temp_val
    except AttributeError:
        cpu_temp_values = []
    avg_cpu_temperature = None
    if cpu_temp_values:
        avg_cpu_temperature = sum(cpu_temp_values) / len(cpu_temp_values)
    return avg_cpu_temperature


def get_disk_temperature():
    disk_temp = None
    try:
        disks = psutil.disk_partitions(all=True)
        for disk in disks:
            if 'disk' in disk.device and disk.mountpoint == '/':
                disk_info = psutil.disk_io_counters(perdisk=True).get(disk.device)
                if disk_info is not None and hasattr(disk_info, 'temperature') and disk_info.temperature is not None:
                    disk_temp = disk_info.temperature

    except Exception:
        disk_temp = 0
    return disk_temp

# print(get_disk_temperature(), get_avg_cpu_temperature())