import psutil
import time


def get_cpus():
    try:
        counters = psutil.cpu_count()
    except Exception:
        counters = 0
    return counters


def get_cpu_kpi():
    cpus_percent = []
    if get_cpus() > 0:
        cpus_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_load = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=False)
    queue_length = (cpu_load / 100) * cpu_count
    # get IPS and CPS
    cpu_state = psutil.cpu_stats()
    interrupts1, ctx_switches1 = cpu_state.interrupts, cpu_state.ctx_switches
    time.sleep(1)
    cpu_state = psutil.cpu_stats()
    interrupts2, ctx_switches2 = cpu_state.interrupts, cpu_state.ctx_switches
    ips = (interrupts2 - interrupts1) / 1
    cps = (ctx_switches2 - ctx_switches1) / 1
    ips = abs(ips)
    cps = abs(cps)
    try:
        running_cpus = sum(usage > 0 for usage in cpus_percent)
    except Exception:
        running_cpus = 0
    # cpus_percent, cpu_load, ips, cps, queue_length, pid_count
    return [cpu_load, running_cpus, ips, cps, queue_length, pid_count()]


def pid_count():
    try:
        num_pid = len(psutil.pids())
    except Exception:
        num_pid = None
    return num_pid
