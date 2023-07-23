import psutil
import time


def get_disk_latency():
    # Get disk I/O counters for the first time
    io_counters_start = psutil.disk_io_counters()

    # Wait for a short interval to capture the change in disk I/O counters
    time.sleep(1)

    # Get disk I/O counters again after the interval
    io_counters_end = psutil.disk_io_counters()

    # Calculate the busy_time (disk latency) as the difference between read_time and write_time
    read_time_diff = io_counters_end.read_time - io_counters_start.read_time
    write_time_diff = io_counters_end.write_time - io_counters_start.write_time
    busy_time = read_time_diff + write_time_diff

    return busy_time


def get_disk_io():
    disk_latency = get_disk_latency()
    disk_utilization = psutil.disk_usage('/').percent
    disk_io_counters = psutil.disk_io_counters()
    read_count = disk_io_counters.read_count
    write_count = disk_io_counters.write_count
    read_bytes = disk_io_counters.read_bytes / 1024 / 1024
    write_bytes = disk_io_counters.write_bytes / 1024 / 1024
    return [disk_utilization,disk_latency, read_count, read_bytes, write_count, write_bytes]
