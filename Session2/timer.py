import time
class timer:
    def __init__(self):
        self.second = 0
    def tick(self):
        self.second -= 1
    def reset(self, n):
        self.second = n
    def start(self):
        print(self.second)
        while True:
            if self.second > 0:
                time.sleep(1)
                timer.tick(self)
                print(self.second)
            else:
                print("Time's up")
                break
new_timer = timer
while True:
    command = input("Insert option (Start/Reset/Exit): ")
    if command == "Start":
        seconds = int(input("Insert time (seconds): "))
        new_timer.reset(new_timer, seconds)
        new_timer.start(new_timer)
    elif command == "Reset":
        new_timer.reset(new_timer, seconds)
    elif command == "Exit":
        break



        



