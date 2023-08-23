class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        results = []
        for flight in self.flights:
            if flight.source == source:
                results.append(flight)
        return results

    def search_by_destination(self, destination):
        results = []
        for flight in self.flights:
            if flight.destination == destination:
                results.append(flight)
        return results

def main():
    flight_table = FlightTable()
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))
                                                                            
    user_input = input("Enter your search query (Flight ID / Source City / Destination): ")

    flight = flight_table.search_by_id(user_input)
    if flight:
        print_flight_details(flight)
    else:
        results = flight_table.search_by_source(user_input)
        if not results:
            results = flight_table.search_by_destination(user_input)

        if results:
            print_results("Search results:", results)
        else:
            print("No flights found.")

def print_flight_details(flight):
    print("Flight Details:")
    print(f"Flight ID: {flight.flight_id}")
    print(f"Source City: {flight.source}")
    print(f"Destination: {flight.destination}")
    print(f"Price: {flight.price}")

def print_results(message, results):
    print(message)
    for flight in results:
        print(f"Flight ID: {flight.flight_id}, Source City: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")

if __name__ == "__main__":
    main()
