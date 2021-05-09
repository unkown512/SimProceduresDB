import resource
from time import sleep
'''
    Sample resources every 100 MS (0.1 seconds)
'''

class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True

    def measure_usage(self):
        max_usage = 0
        ram_timeline = []
        user_time = []
        while self.keep_measuring:
            ram_timeline.append(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            user_time.append(resource.getrusage(resource.RUSAGE_SELF).ru_utime)
            max_usage = max(
                max_usage,
                ram_timeline[-1]
            )
            sleep(0.1)
        return max_usage, ram_timeline, user_time
