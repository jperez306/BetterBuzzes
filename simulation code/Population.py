class Population(object):
    def __init__(self, riders):
        self.riders = riders

    def __repr__(self):
        s = ""
        for rider in self.riders:
            s += str(rider) + " "
        return s

    def update(self, time):
        for rider in self.riders:
            rider.update(time)

    def get_wait_times(self):
        counter = 0
        for rider in self.riders:
            counter += sum(rider.wait_times)
        return counter
