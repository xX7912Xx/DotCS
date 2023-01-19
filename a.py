from threading import main_thread
from reprint import output
from time import sleep

def doubleprogressbar():
    with output(output_type='dict') as output_lines:
        for i in range(1,101):
            for progress in range(1,101):
                output_lines['Partial Progress'] = "[{done}{padding}] {percent}%".format(
                        done = "#" * int(progress/5),
                        padding = " " * (20 - int(progress/5)),
                        percent = progress
                )
                sleep(0.01)
            output_lines['Total Progress'] = "[{done}{padding}] {percent}%".format(
                        done = "#" * int(i/5),
                        padding = " " * (20 - int(i/5)),
                        percent = i
            )

if __name__ == "__main__":
    doubleprogressbar()
