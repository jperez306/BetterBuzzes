from BusBrain import BusBrain


class Bus(object):
    def __init__(self, id_number, current_stop):
        self.id_number = id_number
        self.brain = BusBrain()
        self.current_stop = current_stop
        self.transitioning = False
        self.time_until_next = 0
        self.riders = []

    def __repr__(self):
        return str(self.id_number) + " @ stop " + str(self.current_stop) + ": " + str(self.get_volume()) + str(self.transitioning)

    def setup(self, current_stop):
        self.current_stop = current_stop
        self.transitioning = True
        self.time_until_next = 0
        self.riders = []

    def update(self, time):
        if self.time_until_next <= 0:
            if self.transitioning:
                self.transitioning = False
                self.current_stop = self.current_stop.next_stop
                self.rider_exchange(time)
                self.time_until_next = self.brain.give_next_wait_time()
            else:
                self.transitioning = True
                self.time_until_next = self.current_stop.time_to_next
        self.time_until_next -= 1

    def rider_exchange(self, time):
        new_points = []
        for rider in self.riders:
            if not rider[1].end == self.current_stop:
                new_points.append(rider)
        for rider in self.current_stop.riders:
            new_points.append(rider)
            rider[0].pickup(time)
        self.current_stop.clear_riders()
        self.riders = new_points

    def add_rider(self, rider_transit_tup):
        self.riders.append(rider_transit_tup)

    def get_volume(self):
        return len(self.riders)
