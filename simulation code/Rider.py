import numpy as np


class Rider(object):
    def __init__(self, id_number, schedule):
        self.id_number = id_number
        self.schedule = schedule
        self.predicted_schedule = []
        self.arrival_time = 0
        self.wait_times = []

    def __repr__(self):
        return str(self.id_number)

    def setup(self):
        self.wait_times = []
        for transit in self.schedule:
            self.predicted_schedule.append(transit.generate_value())

    def update(self, time):
        if time in self.predicted_schedule:
            for transit in self.schedule:
                if transit.predicted_value == time:
                    self.arrival_time = time
                    transit.start.add_rider([self, transit])

    def pickup(self, time):
        self.wait_times.append(time - self.arrival_time)


class SchedulePoint(object):
    def __init__(self, start, end, mean, st_dv):
        self.start = start
        self.end = end
        self.mean = mean
        self.st_dv = st_dv
        self.predicted_value = 0

    def generate_value(self):
        self.predicted_value = int(np.random.normal(self.mean, self.st_dv))
        if self.predicted_value < 0:
            self.predicted_value = 0
        return self.predicted_value
