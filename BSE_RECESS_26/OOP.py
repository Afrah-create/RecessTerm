# generate_csv.py
import csv
import random
from faker import Faker

def create_user_data_csv(filename="user_data.csv", num_rows=1000):
    """Generate a CSV file with fake user data"""
    fake = Faker()
    
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
              "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
              "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
              "Indianapolis", "San Francisco", "Seattle", "Denver", "Washington"]
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Email", "Age", "City", "Purchase_Amount"])
        
        for _ in range(num_rows):
            name = fake.name()
            email = fake.email()
            age = random.randint(18, 80)
            city = random.choice(cities)
            purchase_amount = round(random.uniform(10, 500), 2)
            writer.writerow([name, email, age, city, purchase_amount])
    
    print(f"✅ Created '{filename}' with {num_rows} rows of data!")

if __name__ == "__main__":
    # Install faker if needed: pip install faker
    try:
        create_user_data_csv()
    except ImportError:
        print("⚠️  Faker not installed. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "faker"])
        create_user_data_csv()