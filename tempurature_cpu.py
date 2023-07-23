import psutil

def get_cpu_temperature():
    try:
        temperatures = psutil.sensors_temperatures()
        if "coretemp" in temperatures:
            cpu_temperatures = temperatures["coretemp"]
            cpu_temp_values = [entry.current for entry in cpu_temperatures if "Package id 0" in entry.label]
            return cpu_temp_values
    except AttributeError:
        pass

    return []

# Get CPU temperatures
cpu_temperatures = get_cpu_temperature()

if cpu_temperatures:
    avg_cpu_temperature = sum(cpu_temperatures) / len(cpu_temperatures)
    print("Average CPU Temperature: {:.2f}°C".format(avg_cpu_temperature))
else:
    print("CPU temperature information not available on this system.")
