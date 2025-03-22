class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)
    
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

# Create instance and print statements should be outside the class
bus = Bus()
fare_amount = bus.fare()

print(f"Bus Seating Capacity: {bus.seating_capacity}")
print(f"Total fare for Bus: INR{fare_amount}")
