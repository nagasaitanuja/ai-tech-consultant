# run.py - Runs all 3 tasks in one command
from task1.main import run as run_task1
from task2.main import run as run_task2
from task3.main import run as run_task3

if __name__ == "__main__":
    run_task1()
    run_task2()
    run_task3()
