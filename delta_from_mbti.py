import spacy
from datetime import datetime
import deltaURL
import webbrowser
import destination_from_mbti

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def extract_entities(user_input):
    doc = nlp(user_input)
    entities = {
        "departure_city": None,
        "departure_date": None
    }
    for ent in doc.ents:
        if ent.label_ == "GPE":
            if entities["departure_city"] is None:
                entities["departure_city"] = ent.text
        elif ent.label_ == "DATE":
            entities["departure_date"] = ent.text
    return entities

def main():
    print("Welcome to Griffin the Globe: Personal Travel Assistant!")
    while True:
        user_input = input("Please enter your departure city and departure date to begin your journey: ")
        entities = extract_entities(user_input)
        print(entities)
        if entities["departure_city"] and entities["departure_date"]:
            departure_city = entities["departure_city"].strip().upper()
            departure_date_str = entities["departure_date"].strip()

            # Attempt to parse the date string into a datetime object
            try:
                departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d")
            except ValueError:
                try:
                    departure_date = datetime.strptime(departure_date_str, "%B %d %Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in either 'YYYY-MM-DD' or 'Month DD YYYY' format.")
                    continue

            # Format the parsed date into 'YYYY-MM-DD' format
            departure_date_formatted = departure_date.strftime("%Y-%m-%d")

            destination_city = destination_from_mbti.main()
            print(destination_city)

            delta_url = deltaURL.main(departure_city, destination_city, departure_date_formatted)
            print("URL:", delta_url)
            print("Redirecting to Delta Airlines website...")
            webbrowser.open(delta_url)
            exit()
        else:
            print("Sorry, I couldn't understand your input. Please try again.")

if __name__ == "__main__":
    main()
