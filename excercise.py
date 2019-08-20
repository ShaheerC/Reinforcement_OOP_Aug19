class Location:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class Trip:
    
    def __init__(self):
        self.stops = []

    def add_stop(self, stop):
        self.stops.append(stop)

    def trip_start(self):
        print("Began trip.")
        for i in range(len(self.stops)-1):
            print(f"Travelled from {self.stops[i]} to {self.stops[i+1]}.")
        print("Ended trip.")

vacation = Trip()
toronto = Location('Toronto')
ottawa = Location('Ottawa')
montreal = Location('Montreal')
quebec = Location('Quebec City')
halifax = Location('Halifax')
stjohns = Location("St. John's")

vacation.add_stop(toronto)
vacation.add_stop(ottawa)
vacation.add_stop(montreal)
vacation.add_stop(quebec)
vacation.add_stop(halifax)
vacation.add_stop(stjohns)

vacation.trip_start()