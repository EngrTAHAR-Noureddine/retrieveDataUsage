import psutil


def get_ram_kpis():  # In MB
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_total = ram.total / 1024 / 1024
    ram_available = ram.available / 1024 / 1024
    free_ram = ram.free / 1024 / 1024
    used_ram = ram.used / 1024 / 1024

    return [ram_percent, ram_total, used_ram, ram_available, free_ram]


def get_swap_kpis():  # In MB
    swap = psutil.swap_memory()
    swap_percent = swap.percent
    swap_total = swap.total / 1024 / 1024
    free_swap = swap.free / 1024 / 1024
    used_swap = swap.used / 1024 / 1024
    return [swap_percent, swap_total, used_swap, free_swap]
