class BusStop(object):
    def __init__(self, id_number, next_stop, time_to_next):
        self.id_number = id_number
        self.next_stop = next_stop
        self.time_to_next = time_to_next
        self.riders = []

    def __repr__(self):
        return str(self.id_number) + ": " + str(self.get_volume())

    def clear_riders(self):
        self.riders = []

    def add_rider(self, rider_transit_tup):
        self.riders.append(rider_transit_tup)

    def get_volume(self):
        return len(self.riders)
