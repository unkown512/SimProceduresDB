import sys
import importlib
from memory_monitor import MemoryMonitor
from concurrent.futures import ThreadPoolExecutor


def start_memory_monitor(program):
    '''
        Params:
            arg1(module): python module

        Return:
            max ram usage 
            ram timeline array
            user time array
    '''
    with ThreadPoolExecutor() as executor:
        monitor = MemoryMonitor()
        mem_thread = executor.submit(monitor.measure_usage)
        try:
            fn_thread = executor.submit(program.evaluate)
            result = fn_thread.result()
        finally:
            monitor.keep_measuring = False
            max_usage, ram_timeline, user_time = mem_thread.result()
            
        print(f"Peak memory usage: {max_usage}")
        return max_usage, ram_timeline, user_time

if __name__ == "__main__":
    '''
        sys.argv[1] must be the python program name

        There must be a function called `evaluate`
    '''
    if( len(sys.argv) != 2 ):
        print("Usage: python3 procedure_evaluation.py <program_path>")
        quit()

    program = importlib.import_module(sys.argv[1])
    if( 'evaluate' not in dir(program) ):
        print(f"Program:{program.__name__} missing function evaluate")
        quit()
    print(start_memory_monitor(program))
