print("******************************************************************************")

# Exercise 3.1


def collect_data():
    """Collects and validates user input"""
    records = []  # List to store multiple records

    while True:
        user_data = {}  # Dictionary to store a single record
        user_data["Name"] = input("Enter your name: ")
        user_data["Age"] = int(input("Enter your age: "))
        user_data["Annual Income"] = float(input("Enter your annual income: "))
        user_data["Years of Education"] = int(input("Enter your years of education: "))
        records.append(user_data)  # Add record to the list

        # Ask the user if they want to continue
        proceed = input("Do you want to add another record? (yes/no): ").strip().lower()
        if proceed != "yes":
            break

    return records

# Collect data
data_records = collect_data()

# Print all records
print("\n--- All Collected Data ---")
for index, record in enumerate(data_records, start=1):
    print(f"\nRecord {index}:")
    for key, value in record.items():
        if key == "Annual Income":
            print(f"{key}: ${value:,.2f}")  # Format income for readability
        else:
            print(f"{key}: {value}")


print("**********************************************************************")

##### Exercise 3.2
# BMI Calculator

def calculate_bmi(weight, height):
    """Calculate BMI and return rounded result"""
    return round(weight / (height ** 2), 2)

# Get user inputs
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Print result
print(f"\nYour BMI is: {bmi:.2f}")