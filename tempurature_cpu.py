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
    avg_cpu_temperature = 0
    if cpu_temp_values:
        avg_cpu_temperature = sum(cpu_temp_values) / len(cpu_temp_values)
    return avg_cpu_temperature
