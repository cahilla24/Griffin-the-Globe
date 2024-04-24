import personality_type
import random as rand

def recommend_destinations(mbti_type):
    destinations = {
        "INTJ": ["Kyoto", "Rome"],
        "ENFP": ["Rio de Janeiro", "Bali"],
        "ISTP": ['Yellowstone', 'Patagonia'],
        "INFP": ['Kyoto', 'Florence'],
        "ESTJ": ['Singapore', 'Zurich'],
        "ENFJ": ['Costa Rica', 'South Africa'],
        "ISFP": ['Santorini', 'New Zealand'],
        "ENTJ": ['Machu Picchu', 'Himalayas'],
        "INFJ": ['Bangalore', 'Sedona'],
        "ISTJ": ['Athens', 'Giza'],
        "ESTJ": ['London', 'Washington, D.C.'],
        "ISFJ": ['Barcelona', 'Vienna'],
        "ESFJ": ['Sydney', 'Barcelona'],
        "ISTP": ['Yellowstone', 'Patagonia'],
        "INTP": ['Florence', 'Paris'],
        "ENTP": ['Tokyo', 'Berlin'],
        "ESTP": ['Queenstown', 'Patagonia']
        # Add more destinations for other MBTI types
    }
    return destinations.get(mbti_type, ["No recommendations available for this MBTI type"])

def main():
    # Prompt the user to input their MBTI type
    user_input = input("Enter text to predict personality type: ")
    predicted_type = personality_type.predict_personality(user_input)
    print('MBTI type: ' + predicted_type)

    # Generate recommendations based on the user's MBTI type
    recommendations = recommend_destinations(predicted_type)

    # Display the recommendations to the user
    if recommendations:
        print("Recommended destinations for your MBTI type:")
        one_or_two = rand.randint(0,1)
        destination = recommendations[one_or_two]
        print(destination)
        return destination
    else:
        print("No recommendations available for your MBTI type.")

if __name__ == "__main__":
    main()
