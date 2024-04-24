import webbrowser
import city_to_code

def get_airport_code(city_name):
    return city_to_code.get(city_name)

def generate_delta_url(departure_city, destination_city, departure_date):
    # Base URL for Delta Airlines flight search
    base_url = "https://www.delta.com/flight-search/book-a-flight"
    
    # Constructing the URL with parameters
    delta_url = f"{base_url}?originCity={departure_city}&destinationCity={destination_city}&departureDate={departure_date}"
    
    return delta_url

def main(departure_city, destination_city, departure_date):
    # Get airport codes
    departure_code = get_airport_code(departure_city)
    destination_code = get_airport_code(destination_city)

    if departure_code and destination_code:
        # Generate Delta URL
        delta_url = generate_delta_url(departure_code, destination_code, departure_date)

        print("Redirecting to Delta Airlines website...")
        print("URL:", delta_url)
        webbrowser.open(delta_url)
    else:
        print("Airport codes not found for provided cities.")

if __name__ == "__main__":
    departure_city=input('depart')
    destination_city=input('arrive')
    departure_date=input('date')
    main(departure_city, destination_city, departure_date)
