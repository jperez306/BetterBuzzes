import numpy as np


class BusBrain(object):
    def __init__(self):
        self.choice_index = 0
        self.choices = (np.random.random(10000) * 0).astype(int)

    def __repr__(self):
        return str(self.id_number) + " @ stop " + str(self.current_stop)

    def give_next_wait_time(self):
        wait_time = self.choices[self.choice_index]
        self.choice_index += 1
        return wait_time
