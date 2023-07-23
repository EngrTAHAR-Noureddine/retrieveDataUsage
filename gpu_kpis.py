import GPUtil


def get_gpus():
    try:
        gpus = len(GPUtil.getGPUs())
    except Exception:
        gpus = 0
    return gpus


def get_gpu_kpis():
    gpus = GPUtil.getGPUs()
    gpu_percent = []
    gpu_temperatures = []
    for gpu in gpus:
        gpu_percent.append(gpu.load * 100)
        gpu_temperatures = [gpu.temperature for gpu in gpus]
    avg_gpu_temperature = 0
    if gpu_temperatures:
        avg_gpu_temperature = sum(gpu_temperatures) / len(gpu_temperatures)
    try:
        running_gpus = sum(usage > 0 for usage in gpu_percent)
    except Exception:
        running_gpus = 0

    return [running_gpus, avg_gpu_temperature]