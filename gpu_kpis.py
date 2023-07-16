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
    return gpu_percent
