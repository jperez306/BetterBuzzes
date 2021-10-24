from Bus import Bus
from BusStop import BusStop
from Population import Population
from Rider import SchedulePoint, Rider
import matplotlib.pyplot as plt


def run():
    stop_c = BusStop(1, None, 3*60)
    stop_b = BusStop(2, stop_c, 5*60)
    stop_a = BusStop(3, stop_b, 7*60)
    stop_c.next_stop = stop_a

    riders = []
    for i in range(30):
        riders.append(Rider(i, [SchedulePoint(stop_a, stop_c, 1*60*60, 15*60),
                                SchedulePoint(stop_c, stop_a, 5*60*60, 30*60)]))
    for i in range(50):
        riders.append(Rider(i, [SchedulePoint(stop_b, stop_c, 1 * 60 * 60, 15 * 60),
                                SchedulePoint(stop_c, stop_b, 5 * 60 * 60, 30 * 60)]))
    for rider in riders:
        rider.setup()
    population = Population(riders=riders)
    bus1 = Bus(1, stop_a)
    bus2 = Bus(1, stop_b)

    stop_a_v = []
    stop_b_v = []
    stop_c_v = []
    bus1_loc = []
    bus2_loc = []
    bus1_cap = []
    bus2_cap = []

    for t in range(60*60*8):
        population.update(t)
        bus1.update(t)
        bus2.update(t)
        stop_a_v.append(stop_a.get_volume())
        stop_b_v.append(stop_b.get_volume())
        stop_c_v.append(stop_c.get_volume())
        bus1_loc.append(bus1.current_stop.id_number)
        bus2_loc.append(bus2.current_stop.id_number)
        bus1_cap.append((bus1.get_volume()))
        bus2_cap.append((bus2.get_volume()))

    plt.plot(stop_a_v)
    plt.plot(stop_b_v)
    plt.plot(stop_c_v)
    plt.show()
    plt.plot(bus1_loc)
    plt.plot(bus2_loc)
    plt.show()

    print(population.get_wait_times()/2/100/60)


if __name__ == '__main__':
    run()
