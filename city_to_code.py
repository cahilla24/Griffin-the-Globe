import csv

def search_city_code(csv_file, city_name):
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if city_name.strip().upper() in row[0].strip().upper():
                return row[1].strip()
    return None

def get(city_name):
    csv_file = 'city_to_code.csv'  
    city_code = search_city_code(csv_file, city_name)
    if city_code:
        print(f"The airport code for {city_name} is: {city_code}")
        return city_code
    else:
        print(f"Sorry, the airport code for {city_name} is not available.")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get(city_name)
