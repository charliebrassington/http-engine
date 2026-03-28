from threading import Thread
from typing import List


def run_threads(thread_list: List[Thread]) -> None:
    for thread in thread_list:
        thread.daemon = True
        thread.start()

    for thread in thread_list:
        thread.join()
