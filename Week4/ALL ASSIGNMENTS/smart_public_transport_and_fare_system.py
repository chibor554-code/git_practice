"""
Smart Public Transport & Fare System
Project 02 - Week 3 Full Stack Project (Challenge Edition)
TechRise Cohort 3

MULTI-USER SECURITY UPDATE:
- Replaced single password with a dynamic User Database (users_db.json).
- Added First-Time Setup for the initial Admin account.
- Added Login/Registration portal with hidden inputs and SHA-256 hashing.
- Maintained the 3-strike security lockout rule.
"""

import time                 
import functools              
import json                   
import os                     
import random                  
import sys                    # Used to forcefully exit the program
import getpass                # Used to hide password input on the screen
import hashlib                # Used to encrypt/hash passwords

from datetime import datetime             
from typing import List, Dict, Optional, Generator       
from contextlib import contextmanager
from enum import Enum                     

# Analytics dependencies
import matplotlib             
matplotlib.use('Agg')       # FIX: Must be called BEFORE importing pyplot
import pandas as pd                 
import matplotlib.pyplot as plt     


# ==================== SECURITY & USER MANAGEMENT ====================

invalid_input_count = 0
MAX_INVALID_INPUTS = 3
DATA_FILE = "transport_system_data.json"
USERS_DB_FILE = "users_db.json"

def handle_invalid_input(message="Invalid input!"):
    """Tracks invalid inputs and shuts down the system if the limit is reached."""
    global invalid_input_count
    invalid_input_count += 1
    print(f"❌ {message} ({invalid_input_count}/{MAX_INVALID_INPUTS} attempts)")
    if invalid_input_count >= MAX_INVALID_INPUTS:
        print("\n🚫 SECURITY ALERT: Too many invalid inputs. System is shutting down.")
        sys.exit(1)

def get_hidden_input(prompt=""):
    """Gets input without showing characters on the screen."""
    try:
        return getpass.getpass(prompt)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

def hash_password(plain_text_password):
    """Encrypts (hashes) a password using SHA-256."""
    return hashlib.sha256(plain_text_password.encode('utf-8')).hexdigest()

def load_users() -> dict:
    """Loads the user database from JSON."""
    if not os.path.exists(USERS_DB_FILE):
        return {}
    try:
        with open(USERS_DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(users: dict):
    """Saves the user database to JSON."""
    with open(USERS_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user() -> bool:
    """Handles the creation of a new user."""
    print("\n" + "-"*40)
    print(" 📝 CREATE NEW USER")
    print("-"*40)
    
    username = input("Enter new username: ").strip()
    if not username:
        print("❌ Username cannot be empty.")
        return False
        
    users = load_users()
    if username in users:
        print(f"❌ Username '{username}' already exists!")
        return False
        
    pwd1 = get_hidden_input("Enter password: ")
    pwd2 = get_hidden_input("Confirm password: ")
    
    if not pwd1:
        print("❌ Password cannot be empty.")
        return False
    if pwd1 != pwd2:
        print("❌ Passwords do not match.")
        return False
        
    users[username] = hash_password(pwd1)
    save_users(users)
    print(f"✅ User '{username}' created successfully!")
    return True

def login_user(users: dict) -> bool:
    """Handles user login."""
    username = input("Username: ").strip()
    pwd = get_hidden_input("Password: ")
    
    if username in users:
        if users[username] == hash_password(pwd):
            print(f"\n✅ Welcome, {username}! Access Granted.")
            global invalid_input_count
            invalid_input_count = 0 # Reset global app counter on successful login
            return True
            
    print("❌ Invalid username or password.")
    return False

def authenticate() -> bool:
    """Main authentication gate. Handles first-time setup and login."""
    users = load_users()
    
    # 1. First Time Setup
    if not users:
        print("\n🔔 NO USERS FOUND IN DATABASE.")
        print("Please create the first Admin account to continue.")
        while not register_user():
            pass # Keep asking until they successfully create one
        users = load_users() # Reload to include the new user

    # 2. Login Portal
    login_attempts = 0
    while login_attempts < MAX_INVALID_INPUTS:
        print("\n" + "="*45)
        print(" 🔐 SMART TRANSPORT: SECURE PORTAL")
        print("="*45)
        print("1. Login")
        print("2. Create New Staff User")
        print("="*45)
        
        choice = input("Select option (1/2): ").strip()
        
        if choice == '1':
            if login_user(users):
                return True
            login_attempts += 1
            print(f"⚠️ Attempts remaining: {MAX_INVALID_INPUTS - login_attempts}")
        elif choice == '2':
            if register_user():
                users = load_users() # Reload to include the new user
        else:
            print("❌ Invalid option.")
            login_attempts += 1
            
    print("\n🚫 SECURITY LOCKOUT: Too many failed login attempts. Shutting down.")
    sys.exit(1)


# ==================== CUSTOM EXCEPTIONS ====================

class SeatUnavailableError(Exception):   
    def __init__(self, seat_number: str, trip_id: str):
        self.seat_number = seat_number
        self.trip_id = trip_id
        super().__init__(f"Seat {seat_number} is unavailable for trip {trip_id}")

class TripFullError(Exception):                 
    def __init__(self, trip_id: str, vehicle_type: str):
        self.trip_id = trip_id
        self.vehicle_type = vehicle_type
        super().__init__(f"Trip {trip_id} ({vehicle_type}) is fully booked")

class DriverUnavailableError(Exception):       
    def __init__(self, driver_name: str, trip_time: datetime):
        self.driver_name = driver_name
        self.trip_time = trip_time
        super().__init__(f"Driver {driver_name} is already assigned at {trip_time}")

class InvalidStopError(Exception):       
    def __init__(self, stop: str, route_name: str):
        self.stop = stop
        self.route_name = route_name
        super().__init__(f"Stop '{stop}' is not on route '{route_name}'")


# ==================== DECORATORS ====================

def timer(func):     
    @functools.wraps(func)    
    def wrapper(*args, **kwargs):  
        start_time = time.time()   
        result = func(*args, **kwargs)     
        end_time = time.time()    
        execution_time = (end_time - start_time) * 1000     
        print(f"[TIMER] {func.__name__} executed in {execution_time:.4f} ms")
        return result   
    return wrapper   

def retry(times: int = 3):     
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except SeatUnavailableError as e:
                    last_exception = e
                    print(f"[RETRY] Attempt {attempt + 1}/{times} failed: {e}")
                    if attempt < times - 1:
                        print(f"[RETRY] Retrying in 0.5 seconds...")
                        time.sleep(0.5)
            raise last_exception
        return wrapper
    return decorator


# ==================== ENUMS ====================

class VehicleType(Enum):
    BUS = "Bus"
    MINIVAN = "Minivan (Danfo)"
    SHARED_TAXI = "Shared Taxi"

class SeatStatus(Enum):
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    BOOKED = "Booked"
    OCCUPIED = "Occupied"


# ==================== BASE CLASSES ====================

class Person:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"{self.name} ({self.phone})"

class Driver(Person):
    def __init__(self, name: str, phone: str, license_number: str):
        super().__init__(name, phone)
        self.license_number = license_number
        self.current_trip = None  
    
    def is_available(self) -> bool:
        return self.current_trip is None
    def assign_trip(self, trip): self.current_trip = trip
    def release_trip(self): self.current_trip = None
    def __str__(self):
        return f"Driver: {self.name} (License: {self.license_number})"

class Passenger(Person):
    def __init__(self, name: str, phone: str, email: str = ""):
        super().__init__(name, phone)
        self.email = email
        self.tickets: List['Ticket'] = []
    
    def add_ticket(self, ticket): self.tickets.append(ticket)
    def get_booking_history(self) -> List['Ticket']: return self.tickets
    def __str__(self): return f"Passenger: {self.name} ({self.phone})"


# ==================== VEHICLE HIERARCHY ====================

class Vehicle:
    base_fare_per_km = 0.0  
    def __init__(self, plate_number: str, capacity: int):
        self.plate_number = plate_number
        self.capacity = capacity
        self.vehicle_type = VehicleType.BUS
    def get_fare_rate(self) -> float: return self.base_fare_per_km
    def __str__(self):
        return f"{self.vehicle_type.value} - {self.plate_number} (Capacity: {self.capacity})"

class Bus(Vehicle):
    base_fare_per_km = 50.0  
    def __init__(self, plate_number: str):
        super().__init__(plate_number, capacity=50)
        self.vehicle_type = VehicleType.BUS

class Minivan(Vehicle):
    base_fare_per_km = 75.0  
    def __init__(self, plate_number: str):
        super().__init__(plate_number, capacity=18)
        self.vehicle_type = VehicleType.MINIVAN

class SharedTaxi(Vehicle):
    base_fare_per_km = 120.0  
    def __init__(self, plate_number: str, capacity: int = 4):
        super().__init__(plate_number, capacity)
        self.vehicle_type = VehicleType.SHARED_TAXI


# ==================== FARE CALCULATOR ====================

class FareCalculator:
    FARE_MULTIPLIERS = {
        VehicleType.BUS: 1.0,
        VehicleType.MINIVAN: 1.5,
        VehicleType.SHARED_TAXI: 2.4
    }
    
    @classmethod
    @timer
    def calculate_fare(cls, vehicle: Vehicle, distance_km: float, stop_multiplier: float = 1.0) -> float:
        base_rate = vehicle.get_fare_rate()
        multiplier = cls.FARE_MULTIPLIERS.get(vehicle.vehicle_type, 1.0)
        fare = base_rate * distance_km * multiplier * stop_multiplier
        return round(fare, 2)
    
    @classmethod
    def get_fare_comparison(cls, distance_km: float) -> Dict[str, float]:
        comparison = {}
        for v_type, multiplier in cls.FARE_MULTIPLIERS.items():
            base_rate = 50.0 if v_type == VehicleType.BUS else (75.0 if v_type == VehicleType.MINIVAN else 120.0)
            comparison[v_type.value] = base_rate * distance_km * multiplier
        return comparison


# ==================== ROUTE AND TRIP ====================

class Route:
    def __init__(self, name: str, origin: str, destination: str, intermediate_stops: List[str] = None, distance_km: float = 0.0):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.intermediate_stops = intermediate_stops or []
        self.distance_km = distance_km
        self.all_stops = [origin] + self.intermediate_stops + [destination]
    
    def is_valid_stop(self, stop: str) -> bool: 
        return stop in self.all_stops
    
    def get_stop_index(self, stop: str) -> int:
        if not self.is_valid_stop(stop): 
            raise InvalidStopError(stop, self.name)
        return self.all_stops.index(stop)
    
    def calculate_segment_distance(self, from_stop: str, to_stop: str) -> float:
        if not self.is_valid_stop(from_stop) or not self.is_valid_stop(to_stop):
            raise InvalidStopError(from_stop if not self.is_valid_stop(from_stop) else to_stop, self.name)
        from_idx = self.get_stop_index(from_stop)
        to_idx = self.get_stop_index(to_stop)
        if from_idx == to_idx: 
            raise ValueError("Boarding and alighting stops cannot be the same")
        
        total_segments = len(self.all_stops) - 1
        segment_distance = self.distance_km / total_segments
        return segment_distance * abs(to_idx - from_idx)
    
    def __str__(self):
        stops_str = " ↔ ".join(self.all_stops)
        return f"Route {self.name}: {stops_str} ({self.distance_km} km)"


class Trip:
    trip_counter = 0  
    
    def __init__(self, route: Route, vehicle: Vehicle, driver: Driver, departure_time: datetime, direction: str = "forward"):
        Trip.trip_counter += 1
        self.trip_id = f"TRP-{Trip.trip_counter:04d}"
        self.route = route
        self.vehicle = vehicle
        self.driver = driver
        self.departure_time = departure_time
        self.direction = direction
        self.seats: Dict[str, SeatStatus] = {}
        self._initialize_seats()
        self.booked_seats: Dict[str, 'Ticket'] = {}
    
    def _initialize_seats(self):
        for i in range(1, self.vehicle.capacity + 1):
            self.seats[f"{i:02d}"] = SeatStatus.AVAILABLE
    
    @property
    def available_seats_count(self) -> int:
        return sum(1 for status in self.seats.values() if status == SeatStatus.AVAILABLE)
    
    @property
    def is_full(self) -> bool: 
        return self.available_seats_count == 0
    
    def is_seat_available(self, seat_number: str) -> bool:
        return self.seats.get(seat_number) == SeatStatus.AVAILABLE
    
    def get_available_seats(self) -> List[str]:
        return [seat for seat, status in self.seats.items() if status == SeatStatus.AVAILABLE]
    
    def get_route_description(self) -> str:
        if self.direction == "forward":
            stops = self.route.all_stops
        else:
            stops = list(reversed(self.route.all_stops))
        return " → ".join(stops)
    
    def book_seat(self, seat_number: str, passenger: Passenger, boarding_stop: str, alighting_stop: str, fare: float) -> 'Ticket':
        if not self.route.is_valid_stop(boarding_stop): 
            raise InvalidStopError(boarding_stop, self.route.name)
        if not self.route.is_valid_stop(alighting_stop): 
            raise InvalidStopError(alighting_stop, self.route.name)
        
        current_status = self.seats.get(seat_number)
        if current_status not in (SeatStatus.AVAILABLE, SeatStatus.RESERVED):
            raise SeatUnavailableError(seat_number, self.trip_id)
        
        ticket = Ticket(trip=self, passenger=passenger, seat_number=seat_number,
                        boarding_stop=boarding_stop, alighting_stop=alighting_stop, fare=fare)
        
        self.seats[seat_number] = SeatStatus.BOOKED
        self.booked_seats[seat_number] = ticket
        passenger.add_ticket(ticket)
        return ticket
    
    def confirm_seat(self, seat_number: str):
        if seat_number in self.seats: 
            self.seats[seat_number] = SeatStatus.OCCUPIED
    
    def release_seat(self, seat_number: str):
        if seat_number in self.seats:
            self.seats[seat_number] = SeatStatus.AVAILABLE
            if seat_number in self.booked_seats: 
                del self.booked_seats[seat_number]
    
    def __str__(self):
        direction_symbol = "→" if self.direction == "forward" else "←"
        return (f"Trip {self.trip_id}: {self.route.name} {direction_symbol}\n"
                f"  Route: {self.get_route_description()}\n"
                f"  Vehicle: {self.vehicle}\n  Driver: {self.driver}\n"
                f"  Departure: {self.departure_time}\n"
                f"  Available Seats: {self.available_seats_count}/{self.vehicle.capacity}")


class Ticket:
    ticket_counter = 0  
    
    def __init__(self, trip: Trip, passenger: Passenger, seat_number: str,
                 boarding_stop: str, alighting_stop: str, fare: float):
        Ticket.ticket_counter += 1
        self.ticket_id = f"TKT-{Ticket.ticket_counter:06d}"
        self.trip = trip
        self.passenger = passenger
        self.seat_number = seat_number
        self.boarding_stop = boarding_stop
        self.alighting_stop = alighting_stop
        self.fare = fare
        self.booking_time = datetime.now()
        self.payment_status = "Pending"
    
    def mark_paid(self):
        self.payment_status = "Paid"
        self.trip.confirm_seat(self.seat_number)
    
    def to_dict(self) -> Dict:
        return {
            'ticket_id': self.ticket_id,
            'passenger_name': self.passenger.name,
            'passenger_phone': self.passenger.phone,
            'vehicle_type': self.trip.vehicle.vehicle_type.value,
            'route_name': self.trip.route.name,
            'route_origin': self.trip.route.origin,
            'route_destination': self.trip.route.destination,
            'direction': self.trip.direction,
            'distance_km': self.trip.route.calculate_segment_distance(self.boarding_stop, self.alighting_stop),
            'fare': self.fare,
            'departure_time': self.trip.departure_time.isoformat(),
            'seat_number': self.seat_number,
            'boarding_stop': self.boarding_stop,
            'alighting_stop': self.alighting_stop,
            'payment_status': self.payment_status,
            'is_valid': self.payment_status == "Paid"
        }
    
    def __str__(self):
        direction_arrow = "→" if self.trip.direction == "forward" else "←"
        return (f"\n{'='*50}\nTICKET: {self.ticket_id}\n{'='*50}\n"
                f"Passenger: {self.passenger.name}\nPhone: {self.passenger.phone}\n"
                f"Trip: {self.trip.trip_id} - {self.trip.route.name}\n"
                f"Route: {self.boarding_stop} {direction_arrow} {self.alighting_stop}\n"
                f"Seat: {self.seat_number}\n"
                f"Vehicle: {self.trip.vehicle.vehicle_type.value}\n"
                f"Departure: {self.trip.departure_time}\n"
                f"Fare: ₦{self.fare:,.2f}\nStatus: {self.payment_status}\n{'='*50}\n")
    
    def __repr__(self): 
        return f"Ticket({self.ticket_id}, {self.passenger.name}, ₦{self.fare})"


# ==================== CONTEXT MANAGER ====================

@contextmanager
def seat_reservation(trip: Trip, seat_number: str):
    if not trip.is_seat_available(seat_number):
        raise SeatUnavailableError(seat_number, trip.trip_id)
    
    trip.seats[seat_number] = SeatStatus.RESERVED
    print(f"[SEAT RESERVATION] Seat {seat_number} on {trip.trip_id} reserved temporarily")
    
    try:
        yield
    except Exception as e:
        print(f"[SEAT RESERVATION] Exception occurred: {e}")
        trip.release_seat(seat_number)
        print(f"[SEAT RESERVATION] Seat {seat_number} released due to error")
        raise
    else:
        print(f"[SEAT RESERVATION] Seat {seat_number} booking successful")


# ==================== GENERATORS ====================

def available_seats_generator(trip: Trip) -> Generator[str, None, None]:
    for seat_num, status in trip.seats.items():
        if status == SeatStatus.AVAILABLE: 
            yield seat_num

def calculate_route_revenue(trips: List[Trip]) -> Generator[float, None, None]:
    for trip in trips:
        for ticket in trip.booked_seats.values():
            if ticket.payment_status == "Paid": 
                yield ticket.fare


# ==================== TRANSPORT MANAGEMENT SYSTEM ====================

class TransportSystem:
    def __init__(self, name: str):
        self.name = name
        self.vehicles: List[Vehicle] = []
        self.routes: List[Route] = []
        self.trips: List[Trip] = []
        self.drivers: List[Driver] = []
        self.passengers: List[Passenger] = []
    
    def add_vehicle(self, vehicle: Vehicle): self.vehicles.append(vehicle)
    def add_route(self, route: Route): self.routes.append(route)
    def add_driver(self, driver: Driver): self.drivers.append(driver)
    
    def find_or_create_passenger(self, name: str, phone: str, email: str = "") -> Passenger:
        for p in self.passengers:
            if p.phone == phone:
                if name: p.name = name
                if email: p.email = email
                return p
        new_passenger = Passenger(name, phone, email)
        self.passengers.append(new_passenger)
        return new_passenger
    
    def create_trip(self, route: Route, vehicle: Vehicle, driver: Driver, 
                   departure_time: datetime, direction: str = "forward") -> Trip:
        trip = Trip(route, vehicle, driver, departure_time, direction)
        self.trips.append(trip)
        return trip
    
    @retry(times=3)
    def book_ticket(self, passenger: Passenger, trip: Trip, seat_number: str, 
                   boarding_stop: str, alighting_stop: str) -> Ticket:
        distance = trip.route.calculate_segment_distance(boarding_stop, alighting_stop)
        fare = FareCalculator.calculate_fare(trip.vehicle, distance)
        with seat_reservation(trip, seat_number):
            print(f"  Processing payment of ₦{fare:,.2f}...")
            time.sleep(0.1)
            ticket = trip.book_seat(seat_number, passenger, boarding_stop, alighting_stop, fare)
            ticket.mark_paid()
            return ticket
    
    def get_revenue_report(self) -> Dict:
        total_revenue = sum(calculate_route_revenue(self.trips))
        revenue_by_type = {}
        for trip in self.trips:
            v_type = trip.vehicle.vehicle_type.value
            trip_revenue = sum(t.fare for t in trip.booked_seats.values() if t.payment_status == "Paid")
            revenue_by_type[v_type] = revenue_by_type.get(v_type, 0) + trip_revenue
        return {"total_revenue": total_revenue, "by_vehicle_type": revenue_by_type,
                "total_trips": len(self.trips), "total_tickets": sum(len(t.booked_seats) for t in self.trips)}
    
    def export_tickets_csv(self, path: str = "reports/tickets.csv"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        all_tickets = [ticket.to_dict() for trip in self.trips for ticket in trip.booked_seats.values()]
        if not all_tickets:
            print("️  No tickets to export"); return None
        df = pd.DataFrame(all_tickets)
        df.to_csv(path, index=False)
        print(f" Exported {len(all_tickets)} tickets to {path}")
        return df


# ==================== ANALYTICS ENGINE ====================

class TransportAnalytics:
    def __init__(self, system: TransportSystem):
        self.system = system
        self.df = None
    
    def load_data(self):
        all_tickets = [ticket.to_dict() for trip in self.system.trips for ticket in trip.booked_seats.values()]
        if not all_tickets:
            print("⚠️  No ticket data available for analytics"); return False
        self.df = pd.DataFrame(all_tickets)
        self._clean_and_engineer_features()
        return True
    
    def _clean_and_engineer_features(self):
        self.df['fare'] = pd.to_numeric(self.df['fare'], errors='coerce').astype(float)
        self.df['distance_km'] = pd.to_numeric(self.df['distance_km'], errors='coerce').astype(float)
        self.df['departure_time'] = pd.to_datetime(self.df['departure_time'])
        self.df = self.df[self.df['is_valid'] == True]
        self.df['fare_per_km'] = (self.df['fare'] / self.df['distance_km']).round(2)
        self.df.replace([float('inf'), -float('inf')], float('nan'), inplace=True)
        self.df.dropna(subset=['fare_per_km'], inplace=True)
        self.df['hour'] = self.df['departure_time'].dt.hour
        
        def categorize_time(hour):
            if 5 <= hour <= 11: return 'Morning'
            elif 12 <= hour <= 16: return 'Afternoon'
            elif 17 <= hour <= 20: return 'Evening'
            else: return 'Night'
        self.df['time_of_day'] = self.df['hour'].apply(categorize_time)
        
        mean_fare = self.df['fare'].mean()
        self.df['is_high_revenue'] = self.df['fare'] > mean_fare
        print(f"📊 Analytics: {self.df['is_high_revenue'].sum()} high-revenue trips (fare > ₦{mean_fare:,.2f})")
    
    def create_revenue_by_route_chart(self, save_path: str = "reports/revenue_by_route.png"):
        if self.df is None: return
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        self.df['route'] = self.df['route_origin'] + ' ↔ ' + self.df['route_destination']
        revenue_by_route = self.df.groupby('route')['fare'].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(10, 6))
        plt.bar(revenue_by_route.index, revenue_by_route.values, color='steelblue')
        plt.xticks(rotation=45, ha='right')
        plt.title('Total Revenue by Route', fontsize=14, fontweight='bold')
        plt.xlabel('Route', fontsize=12); plt.ylabel('Total Revenue (₦)', fontsize=12)
        plt.tight_layout(); plt.savefig(save_path, dpi=300); plt.close()
        print(f" Saved revenue chart to {save_path}")
    
    def create_volume_by_time_chart(self, save_path: str = "reports/volume_time.png"):
        if self.df is None: return
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        volume_by_time = self.df['time_of_day'].value_counts().reindex(['Morning', 'Afternoon', 'Evening', 'Night'])
        
        plt.figure(figsize=(8, 6))
        plt.bar(volume_by_time.index, volume_by_time.values, color='coral')
        plt.title('Passenger Volume by Time of Day', fontsize=14, fontweight='bold')
        plt.xlabel('Time of Day', fontsize=12); plt.ylabel('Number of Tickets', fontsize=12)
        plt.tight_layout(); plt.savefig(save_path, dpi=300); plt.close()
        print(f"📈 Saved volume chart to {save_path}")
    
    def create_fare_efficiency_chart(self, save_path: str = "reports/fare_efficiency.png"):
        if self.df is None: return
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        avg_fare_per_km = self.df.groupby('vehicle_type')['fare_per_km'].mean()
        
        plt.figure(figsize=(8, 6))
        plt.bar(avg_fare_per_km.index, avg_fare_per_km.values, color='forestgreen')
        plt.title('Fare Efficiency by Vehicle Type', fontsize=14, fontweight='bold')
        plt.xlabel('Vehicle Type', fontsize=12); plt.ylabel('Average Fare per Km (₦)', fontsize=12)
        plt.tight_layout(); plt.savefig(save_path, dpi=300); plt.close()
        print(f" Saved efficiency chart to {save_path}")
    
    def generate_insights(self):
        if self.df is None: return
        print("\n" + "="*70 + "\n                    TRANSPORT INSIGHTS REPORT\n" + "="*70)
        
        self.df['route'] = self.df['route_origin'] + ' ↔ ' + self.df['route_destination']
        revenue_by_route = self.df.groupby('route')['fare'].sum()
        highest_revenue_route = revenue_by_route.idxmax()
        highest_revenue_amount = revenue_by_route.max()
        
        popular_time = self.df['time_of_day'].mode()[0]
        avg_fare_per_km = self.df.groupby('vehicle_type')['fare_per_km'].mean()
        best_efficiency_vehicle = avg_fare_per_km.idxmax()
        worst_efficiency_vehicle = avg_fare_per_km.idxmin()
        
        print(f"\n💰 Highest Revenue Route: {highest_revenue_route} (₦{highest_revenue_amount:,.2f})")
        print(f"⏰ Most Popular Time of Day: {popular_time}")
        print(f" Best Fare Efficiency: {best_efficiency_vehicle} (₦{avg_fare_per_km.max():,.2f}/km)")
        print(f"📉 Worst Fare Efficiency: {worst_efficiency_vehicle} (₦{avg_fare_per_km.min():,.2f}/km)")
        print(f"💵 Total Revenue Collected: ₦{self.df['fare'].sum():,.2f}")
        
        print("\n" + "="*70 + "\n                    STRATEGIC RECOMMENDATION\n" + "="*70)
        print(f"\n📌 INSIGHT QUESTION:")
        print(f"If the company wants to increase revenue without adding new vehicles,")
        print(f"should they run more trips on the highest-revenue route, or increase")
        print(f"fares on the vehicle type with the worst fare-per-km ratio?")
        
        print(f"\n💡 RECOMMENDATION:")
        if avg_fare_per_km.min() < (avg_fare_per_km.max() * 0.7):
            print(f"INCREASE FARES on {worst_efficiency_vehicle}!")
            print(f"  - Their fare-per-km is significantly underperforming.")
            print(f"  - There's room to raise prices to match market rates without adding operational costs.")
        else:
            print(f"RUN MORE TRIPS on {highest_revenue_route}!")
            print(f"  - This route has proven high demand and revenue.")
            print(f"  - Adding capacity here maximizes return on investment.")
        print("="*70 + "\n")


# ==================== JSON DATA PERSISTENCE ====================

def save_system_state(system: TransportSystem):
    data = {
        "counters": {"trip": Trip.trip_counter, "ticket": Ticket.ticket_counter},
        "passengers": [{"name": p.name, "phone": p.phone, "email": p.email, 
                        "ticket_ids": [t.ticket_id for t in p.tickets]} for p in system.passengers],
        "trip_states": {}
    }
    for trip in system.trips:
        trip_data = {"seats": {seat: status.value for seat, status in trip.seats.items()}, "booked_tickets": {}}
        for seat, ticket in trip.booked_seats.items():
            trip_data["booked_tickets"][seat] = {
                "ticket_id": ticket.ticket_id, "passenger_name": ticket.passenger.name,
                "passenger_phone": ticket.passenger.phone,
                "boarding_stop": ticket.boarding_stop, "alighting_stop": ticket.alighting_stop,
                "fare": ticket.fare, "payment_status": ticket.payment_status
            }
        data["trip_states"][trip.trip_id] = trip_data

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"💾 System state saved to {DATA_FILE}")

def load_system_state(system: TransportSystem) -> bool:
    if not os.path.exists(DATA_FILE): return False
    try:
        with open(DATA_FILE, "r") as file: data = json.load(file)
        print(f"📂 Loaded existing data from {DATA_FILE}")

        passenger_lookup = {}
        for p_data in data["passengers"]:
            p = Passenger(p_data["name"], p_data["phone"], p_data["email"])
            passenger_lookup[p.phone] = p
            system.passengers.append(p)

        for trip in system.trips:
            if trip.trip_id in data["trip_states"]:
                trip_data = data["trip_states"][trip.trip_id]
                trip.seats = {seat: SeatStatus(status) for seat, status in trip_data["seats"].items()}
                for seat, t_data in trip_data["booked_tickets"].items():
                    passenger = passenger_lookup.get(t_data["passenger_phone"])
                    if not passenger:
                        passenger = Passenger(t_data["passenger_name"], t_data["passenger_phone"])
                        system.passengers.append(passenger)
                        passenger_lookup[t_data["passenger_phone"]] = passenger
                    
                    ticket = Ticket(trip=trip, passenger=passenger, seat_number=seat,
                                    boarding_stop=t_data["boarding_stop"], 
                                    alighting_stop=t_data["alighting_stop"], 
                                    fare=t_data["fare"])
                    ticket.payment_status = t_data["payment_status"]
                    trip.booked_seats[seat] = ticket
                    passenger.tickets.append(ticket)

        Trip.trip_counter = data["counters"]["trip"]
        Ticket.ticket_counter = data["counters"]["ticket"]
        return True
    except Exception as e:
        print(f"️ Error loading data: {e}"); return False


# ==================== DEMO MODE (AUTO-GENERATOR) ====================

def generate_test_bookings(system: TransportSystem, batch_size: int = 5):
    print(f"\n🎲 GENERATING {batch_size} TEST BOOKINGS FOR DEMO...\n")
    
    first_names = ["Chinedu", "Fatima", "Emmanuel", "Blessing", "Yusuf", "Grace", "Ahmed", "Nneka", "Obinna", "Kemi", "Tunde", "Amaka"]
    last_names = ["Okafor", "Hassan", "Nwosu", "Ade", "Ibrahim", "Okoro", "Bello", "Eze", "Okeke", "Adebayo", "Bakare", "Uche"]

    booked_count = 0
    
    while booked_count < batch_size:
        available_trips = [trip for trip in system.trips if not trip.is_full]
        
        if not available_trips:
            print("⚠️  All trips are fully booked! Cannot generate more test bookings.")
            break
            
        trip = random.choice(available_trips)
        available_seats = trip.get_available_seats()
        
        if not available_seats:
            continue
            
        seat = random.choice(available_seats)
        
        stops = trip.route.all_stops
        if len(stops) < 2:
            continue
            
        # FIX: Ensure boarding stop comes before alighting stop in the route
        indices = sorted(random.sample(range(len(stops)), 2))
        boarding = stops[indices[0]]
        alighting = stops[indices[1]]
        
        rand_first = random.choice(first_names)
        rand_last = random.choice(last_names)
        name = f"{rand_first} {rand_last}"
        phone = f"080{random.randint(10000000, 99999999)}"
        email = f"{rand_first.lower()}.{rand_last.lower()}{random.randint(1,99)}@email.com"
        
        passenger = system.find_or_create_passenger(name, phone, email)
        
        try:
            distance = trip.route.calculate_segment_distance(boarding, alighting)
            fare = FareCalculator.calculate_fare(trip.vehicle, distance)
            
            ticket = trip.book_seat(seat, passenger, boarding, alighting, fare)
            ticket.mark_paid()
            
            print(f"✅ Booked: {passenger.name} - {trip.trip_id} ({boarding}↔{alighting}) - Seat {seat} - ₦{fare:,.2f}")
            booked_count += 1
        except Exception as e:
            pass

    save_system_state(system)
    print(f"\n📊 SUMMARY: {booked_count} new tickets booked successfully. Data saved.")


# ==================== INTERACTIVE CLI ====================

def display_menu():
    print("\n" + "="*60 + "\n   SMART PUBLIC TRANSPORT & FARE SYSTEM\n" + "="*60)
    print("1. View Routes")
    print("2. View Available Trips")
    print("3. Book a Ticket")
    print("4. View My Tickets (by phone)")
    print("5. View Fare Comparison")
    print("6. Generate Revenue Report")
    print("7. Export Data & Analytics")
    print("8. 🎲 Generate 5 Test Bookings (Demo Mode)")
    print("9. 👤 Add New Staff User") # NEW MENU OPTION
    print("10. Exit")
    print("="*60)

def setup_sample_data(system: TransportSystem, silent=False):
    if not silent:
        print("\n⚙️ Setting up sample data...")
    
    bus1 = Bus("ABC-123-AB"); bus2 = Bus("XYZ-789-AB")
    minivan1 = Minivan("DAN-456-AB"); taxi1 = SharedTaxi("TAX-111-AB", capacity=4)
    system.add_vehicle(bus1); system.add_vehicle(bus2); system.add_vehicle(minivan1); system.add_vehicle(taxi1)
    
    route1 = Route("R001", "Aba", "Owerri", intermediate_stops=["Umuahia"], distance_km=120.0)
    route2 = Route("R002", "Aba", "Port Harcourt", intermediate_stops=[], distance_km=85.0)
    route3 = Route("R003", "Umuahia", "Enugu", intermediate_stops=["Oji River"], distance_km=95.0)
    system.add_route(route1); system.add_route(route2); system.add_route(route3)
    
    driver1 = Driver("Chukwuemeka Okafor", "0803-123-4567", "LIC-001")
    driver2 = Driver("Ibrahim Musa", "0805-234-5678", "LIC-002")
    driver3 = Driver("Chioma Nwosu", "0806-345-6789", "LIC-003")
    driver4 = Driver("David Okonkwo", "0807-456-7890", "LIC-004")
    system.add_driver(driver1); system.add_driver(driver2); system.add_driver(driver3); system.add_driver(driver4)
    
    today = datetime.now()
    
    system.create_trip(route1, bus1, driver1, today.replace(hour=8, minute=0), "forward")
    system.create_trip(route1, minivan1, driver2, today.replace(hour=10, minute=30), "forward")
    system.create_trip(route2, bus2, driver3, today.replace(hour=9, minute=0), "forward")
    system.create_trip(route3, taxi1, driver4, today.replace(hour=14, minute=0), "forward")
    
    system.create_trip(route1, bus1, driver1, today.replace(hour=16, minute=0), "reverse")
    system.create_trip(route1, minivan1, driver2, today.replace(hour=18, minute=30), "reverse")
    system.create_trip(route2, bus2, driver3, today.replace(hour=17, minute=0), "reverse")
    system.create_trip(route3, taxi1, driver4, today.replace(hour=19, minute=0), "reverse")
    
    if not silent:
        print("\n✓ Sample data setup complete (bidirectional routes)!\n")

def view_routes(system: TransportSystem):
    print("\n📍 AVAILABLE ROUTES (BIDIRECTIONAL):\n" + "-" * 60)
    if not system.routes: print("No routes available"); return
    for i, route in enumerate(system.routes, 1): 
        print(f"{i}. {route}")

def view_trips(system: TransportSystem):
    print("\n🚌 AVAILABLE TRIPS:\n" + "-" * 60)
    if not system.trips: print("No trips scheduled"); return
    for trip in system.trips:
        print(f"\n{trip}")

def book_ticket_interactive(system: TransportSystem):
    print("\n🎫 BOOK A TICKET\n" + "-" * 60)
    
    print("\nEnter passenger details:")
    
    # VALIDATION: Name must not contain numbers
    name = input("Full name: ").strip().title()
    if not name or any(char.isdigit() for char in name):
        handle_invalid_input("Invalid name. Name cannot contain numbers.")
        return
        
    # VALIDATION: Phone must be exactly 11 digits
    phone = input("Phone number: ").strip()
    if not phone.isdigit() or len(phone) != 11:
        handle_invalid_input("Invalid phone number. Must be exactly 11 digits.")
        return
        
    email = input("Email (optional): ").strip()
    
    passenger = system.find_or_create_passenger(name, phone, email)
    print(f"\n✓ Using passenger: {passenger.name} ({passenger.phone})")
    
    print("\nSelect trip:")
    for i, trip in enumerate(system.trips, 1):
        direction = "→" if trip.direction == "forward" else "←"
        print(f"{i}. {trip.trip_id} - {trip.route.name} {direction} ({trip.departure_time.strftime('%H:%M')}) - Available: {trip.available_seats_count}")
    
    try:
        trip_choice = int(input("Enter trip number: ")) - 1
        if trip_choice < 0 or trip_choice >= len(system.trips): 
            handle_invalid_input("Invalid trip number.")
            return
        trip = system.trips[trip_choice]
    except ValueError:
        handle_invalid_input("Please enter a valid number for trip choice.")
        return
    
    if trip.is_full: 
        print("❌ This trip is fully booked!"); return
    
    print(f"\nRoute stops: {' ↔ '.join(trip.route.all_stops)}")
    boarding = input("Boarding stop: ").strip().title()
    alighting = input("Alighting stop: ").strip().title()
    
    try:
        if not trip.route.is_valid_stop(boarding): 
            raise InvalidStopError(boarding, trip.route.name)
        if not trip.route.is_valid_stop(alighting): 
            raise InvalidStopError(alighting, trip.route.name)
        if boarding == alighting:
            print(" Boarding and alighting stops cannot be the same"); return
        
        print(f"\nAvailable seats: {', '.join(trip.get_available_seats())}")
        seat = input("Select seat number: ").strip()
        if not trip.is_seat_available(seat): 
            print(f"❌ Seat {seat} is not available"); return
        
        distance = trip.route.calculate_segment_distance(boarding, alighting)
        fare = FareCalculator.calculate_fare(trip.vehicle, distance)
        print(f"\nFare: ₦{fare:,.2f}")
        
        if input("Confirm booking? (yes/no): ").strip().lower() == 'yes':
            ticket = system.book_ticket(passenger, trip, seat, boarding, alighting)
            print(f"\n✅ Booking successful!\n{ticket}")
        else: 
            print("Booking cancelled")
    except (InvalidStopError, SeatUnavailableError, Exception) as e: 
        print(f"❌ Error: {e}")

def view_my_tickets(system: TransportSystem):
    print("\n🎫 VIEW MY TICKETS\n" + "-" * 60)
    phone = input("Enter phone number: ").strip()
    
    # VALIDATION: Phone must be exactly 11 digits
    if not phone.isdigit() or len(phone) != 11:
        handle_invalid_input("Invalid phone number. Must be exactly 11 digits.")
        return

    passenger = None
    for p in system.passengers:
        if p.phone == phone:
            passenger = p
            break
    
    if not passenger:
        print("❌ No passenger found with that phone number")
        return
    
    tickets = passenger.get_booking_history()
    if not tickets: 
        print("No tickets booked yet"); return
    
    print(f"\nBooking history for {passenger.name} ({phone}):")
    for ticket in tickets: 
        print(ticket)

def view_fare_comparison():
    print("\n💰 FARE COMPARISON\n" + "-" * 60)
    try:
        distance = float(input("Enter distance (km): "))
        comparison = FareCalculator.get_fare_comparison(distance)
        print(f"\nFare comparison for {distance} km:")
        for v_type, fare in comparison.items(): 
            print(f"  {v_type:25} ₦{fare:,.2f}")
        
        # Reset counter on successful valid input
        global invalid_input_count
        invalid_input_count = 0
    except ValueError: 
        handle_invalid_input("Invalid distance. Please enter a number.")

def generate_revenue_report(system: TransportSystem):
    print("\n📊 REVENUE REPORT\n" + "-" * 60)
    report = system.get_revenue_report()
    print(f"Total Revenue: {report['total_revenue']:,.2f}\nTotal Trips: {report['total_trips']}\nTotal Tickets Sold: {report['total_tickets']}")
    print("\nRevenue by Vehicle Type:")
    for v_type, revenue in report['by_vehicle_type'].items(): 
        print(f"  {v_type:25} ₦{revenue:,.2f}")

def run_analytics(system: TransportSystem):
    print("\n📊 RUNNING ANALYTICS ENGINE...\n")
    analytics = TransportAnalytics(system)
    if not analytics.load_data():
        print("⚠️  Cannot run analytics - no data available"); return
    
    system.export_tickets_csv()
    analytics.create_revenue_by_route_chart()
    analytics.create_volume_by_time_chart()
    analytics.create_fare_efficiency_chart()
    analytics.generate_insights()

def main():
    print("\n" + "="*60 + "\n  SMART PUBLIC TRANSPORT & FARE SYSTEM\n  TechRise Cohort 3 - Project 02\n" + "="*60)
    
    # 1. Require Multi-User Authentication
    if not authenticate():
        return
        
    system = TransportSystem("Abia State Transport")
    
    # 2. ALWAYS initialize the base infrastructure
    setup_sample_data(system, silent=True)
    
    # 3. Load saved dynamic state (Passengers, Bookings, Counters)
    load_system_state(system)
    
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-10): ").strip()
            if choice in [str(i) for i in range(1, 11)]:
                global invalid_input_count
                invalid_input_count = 0  # Reset counter on valid menu choice
                
                if choice == "1": 
                    view_routes(system)
                elif choice == "2": 
                    view_trips(system)
                elif choice == "3":
                    book_ticket_interactive(system)
                    save_system_state(system)
                elif choice == "4": 
                    view_my_tickets(system)
                elif choice == "5": 
                    view_fare_comparison()
                elif choice == "6": 
                    generate_revenue_report(system)
                elif choice == "7": 
                    run_analytics(system)
                elif choice == "8": 
                    generate_test_bookings(system, batch_size=5)
                elif choice == "9": 
                    register_user() # Add new user
                elif choice == "10":
                    print("\n👋 Thank you for using Smart Transport System!\nSafe travels! 🚌\n"); 
                    break
            else:
                handle_invalid_input("Invalid choice. Please enter 1-10")
        except KeyboardInterrupt:
            print("\n\n Exiting system..."); 
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()