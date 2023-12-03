with open("day6\\input.txt", 'r') as f:
    data = list(map(int, f.read().strip().split(",")))

class Lanternfish:
    reproduction_rate = 6
    first_cycle_offset = 2

    def __init__(self, init_timer: int = None):
        if init_timer is None:
            self.timer = self.reproduction_rate + self.first_cycle_offset
        else:
            self.timer = init_timer

    def __int__(self):
        return self.timer

    def __repr__(self):
        return f"<Lanternfish(timer={self.timer})>"

    def next_day(self) -> True:
        if self.timer == 0:
            self.timer = self.reproduction_rate
            return True
        else:
            self.timer -= 1
            return False

fishs = list(map(Lanternfish, data))
# print(fishs)

for i in range(80):
# for i in range(256): way too long + memory consuming
    for fish in fishs.copy():
        if fish.next_day():
            fishs.append(Lanternfish())

print(len(fishs))
