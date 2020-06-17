import os

def wake():
    os.system("tvservice -p")
    os.system("sudo chvt 9 && sudo chvt 7")

def snooze():
    os.system("tvservice -o")

def state():
    os.system("tvservice -s")


if __name__ == "__main__":
    # from time import sleep
    # while True:
    #     snooze()
    #     sleep(20)
    #     wake()
    #     sleep(20)

    state()
