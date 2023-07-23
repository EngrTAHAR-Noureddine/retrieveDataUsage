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
    for gpu in gpus:
        gpu_percent.append(gpu.load * 100)
    try:
        running_gpus = sum(usage > 0 for usage in gpu_percent)
    except Exception:
        running_gpus = 0

    return [running_gpus]
