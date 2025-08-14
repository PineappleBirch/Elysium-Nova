import csv
import json
from faker import Faker

# Initializing the Faker generator
fake = Faker()


# --- Data Models ---

def create_user():
    """
    Generates a single fake user with realistic data.
    """
    return {
        "user_id": fake.uuid4(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "address": fake.street_address(),
        "city": fake.city(),
        "country": fake.country(),
        "join_date": fake.iso8601()
    }


def create_product():
    """
    Generates a single fake product.
    """
    return {
        "product_id": fake.uuid4(),
        "product_name": fake.bs().title(),  # Generates a business-style name
        # Corrected: Increased left_digits to 4 to accommodate a max_value of 1000
        "price": round(fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=10, max_value=1000), 2),
        "description": fake.catch_phrase()
    }


# --- Data Generation ---

def generate_data(model_func, count):
    """
    Generic function to generate a list of data using a given model.
    """
    return [model_func() for _ in range(count)]


# --- Data Saving ---

def save_to_csv(data, filename):
    """
    Saves a list of dictionaries to a CSV file.
    """
    if not data:
        print("No data to save.")
        return
    headers = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully saved {len(data)} records to {filename}")


def save_to_json(data, filename):
    """
    Saves a list of dictionaries to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print(f"Successfully saved {len(data)} records to {filename}")


# --- Main execution block ---

if __name__ == "__main__":
    # Generating 100 fake users and saving to CSV
    user_list = generate_data(create_user, 100)
    save_to_csv(user_list, "output/users.csv")

    print("-" * 20)  # Separator

    # Generating 50 fake products and saving to JSON
    product_list = generate_data(create_product, 50)
    save_to_json(product_list, "output/products.json")