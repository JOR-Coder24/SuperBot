import requests
import re
import config

def get_character_data(character_name):
    your_api_key = config.SUPERHERO_API_KEY
    url = f'https://superheroapi.com/api/{your_api_key}/search/{character_name}'
    response = requests.get(url)
    return response.json()


def extract_superhero_data(data, character_name):
    if 'results' in data and data['results']:
        # Filter results by the queried character name
        for superhero in data['results']:
            if superhero['name'].lower() == character_name.lower():
                return {
                    "Name": superhero['name'],
                    "Full Name": superhero['biography']['full-name'],
                    "Alter Egos": superhero['biography']['alter-egos'],
                    "Aliases": superhero['biography']['aliases'],
                    "Place of Birth": superhero['biography']['place-of-birth'],
                    "First Appearance": superhero['biography']['first-appearance'],
                    "Publisher": superhero['biography']['publisher'],
                    "Alignment": superhero['biography']['alignment'],
                    "Gender": superhero['appearance']['gender'],
                    "Race": superhero['appearance']['race'],
                    "Height": superhero['appearance']['height'],
                    "Weight": superhero['appearance']['weight'],
                    "Eye Color": superhero['appearance']['eye-color'],
                    "Hair Color": superhero['appearance']['hair-color'],
                    "Intelligence": superhero['powerstats']['intelligence'],
                    "Strength": superhero['powerstats']['strength'],
                    "Speed": superhero['powerstats']['speed'],
                    "Durability": superhero['powerstats']['durability'],
                    "Power": superhero['powerstats']['power'],
                    "Combat": superhero['powerstats']['combat'],
                    "Group Affiliation": superhero['connections']['group-affiliation'],
                    "Relatives": superhero['connections']['relatives'],
                }
    return {"error": "Character not found"}


def answer_question(superhero_data, question):
    question = question.lower()
    if "full name" in question:
        return f"Full name: {superhero_data.get('Full Name', 'Unknown')}"
    elif "alter ego" in question:
        return f"Alter egos: {superhero_data.get('Alter Egos', 'Unknown')}"
    elif "aliases" in question:
        return f"Aliases: {superhero_data.get('Aliases', 'Unknown')}"
    elif "place of birth" in question:
        return f"Place of birth: {superhero_data.get('Place of Birth', 'Unknown')}"
    elif "first appearance" in question:
        return f"First appearance: {superhero_data.get('First Appearance', 'Unknown')}"
    elif "publisher" in question:
        return f"Publisher: {superhero_data.get('Publisher', 'Unknown')}"
    elif "alignment" in question:
        return f"Alignment: {superhero_data.get('Alignment', 'Unknown')}"
    elif "gender" in question:
        return f"Gender: {superhero_data.get('Gender', 'Unknown')}"
    elif "race" in question:
        return f"Race: {superhero_data.get('Race', 'Unknown')}"
    elif "height" in question:
        return f"Height: {superhero_data.get('Height', 'Unknown')}"
    elif "weight" in question:
        return f"Weight: {superhero_data.get('Weight', 'Unknown')}"
    elif "eye color" in question:
        return f"Eye color: {superhero_data.get('Eye Color', 'Unknown')}"
    elif "hair color" in question:
        return f"Hair color: {superhero_data.get('Hair Color', 'Unknown')}"
    elif "intelligence" in question:
        return f"Intelligence: {superhero_data.get('Intelligence', 'Unknown')}"
    elif "strength" in question:
        return f"Strength: {superhero_data.get('Strength', 'Unknown')}"
    elif "speed" in question:
        return f"Speed: {superhero_data.get('Speed', 'Unknown')}"
    elif "durability" in question:
        return f"Durability: {superhero_data.get('Durability', 'Unknown')}"
    elif "power" in question:
        return f"Power: {superhero_data.get('Power', 'Unknown')}"
    elif "combat" in question:
        return f"Combat: {superhero_data.get('Combat', 'Unknown')}"
    elif "stats" in question:
        stats = (
            f"Intelligence: {superhero_data.get('Intelligence', 'Unknown')}, "
            f"Speed: {superhero_data.get('Speed', 'Unknown')}, "
            f"Durability: {superhero_data.get('Durability', 'Unknown')}, "
            f"Power: {superhero_data.get('Power', 'Unknown')}, "
            f"Combat: {superhero_data.get('Combat', 'Unknown')}"
        )
        return f"Stats: {stats}"
    elif "group affiliation" in question:
        return f"Group affiliation: {superhero_data.get('Group Affiliation', 'Unknown')}"
    elif "relatives" in question:
        return f"Relatives: {superhero_data.get('Relatives', 'Unknown')}"
    elif "full profile" in question:
        full_profile = (
            f"Full Name: {superhero_data.get('Full Name', 'Unknown')}\n"
            f"Alter Egos: {superhero_data.get('Alter Egos', 'Unknown')}\n"
            f"Aliases: {superhero_data.get('Aliases', 'Unknown')}\n"
            f"Place of Birth: {superhero_data.get('Place of Birth', 'Unknown')}\n"
            f"First Appearance: {superhero_data.get('First Appearance', 'Unknown')}\n"
            f"Publisher: {superhero_data.get('Publisher', 'Unknown')}\n"
            f"Alignment: {superhero_data.get('Alignment', 'Unknown')}\n"
            f"Gender: {superhero_data.get('Gender', 'Unknown')}\n"
            f"Race: {superhero_data.get('Race', 'Unknown')}\n"
            f"Height: {superhero_data.get('Height', 'Unknown')}\n"
            f"Weight: {superhero_data.get('Weight', 'Unknown')}\n"
            f"Eye Color: {superhero_data.get('Eye Color', 'Unknown')}\n"
            f"Hair Color: {superhero_data.get('Hair Color', 'Unknown')}\n"
            f"Intelligence: {superhero_data.get('Intelligence', 'Unknown')}\n"
            f"Strength: {superhero_data.get('Strength', 'Unknown')}\n"
            f"Speed: {superhero_data.get('Speed', 'Unknown')}\n"
            f"Durability: {superhero_data.get('Durability', 'Unknown')}\n"
            f"Power: {superhero_data.get('Power', 'Unknown')}\n"
            f"Combat: {superhero_data.get('Combat', 'Unknown')}\n"
            f"Group Affiliation: {superhero_data.get('Group Affiliation', 'Unknown')}\n"
            f"Relatives: {superhero_data.get('Relatives', 'Unknown')}"
        )
        return f"Full Profile:\n{full_profile}"
    else:
        return "I don't understand the question. Please ask about specific superhero data."


def compare(superhero1_data, superhero2_data, stats):
    results = []
    superhero1_name = superhero1_data.get('Name', 'Unknown')  # Use 'Name' for superhero name
    superhero2_name = superhero2_data.get('Name', 'Unknown')  # Use 'Name' for superhero name

    for stat in stats:
        stat = stat.lower()

        # Try to convert stats to integers, handle missing or invalid stats
        try:
            stat1 = int(superhero1_data.get(stat.capitalize(), 0))  # Default to 0 if stat is missing
        except ValueError:
            stat1 = 0  # Handle cases where stat might not be a number

        try:
            stat2 = int(superhero2_data.get(stat.capitalize(), 0))  # Default to 0 if stat is missing
        except ValueError:
            stat2 = 0  # Handle cases where stat might not be a number

        if stat1 > stat2:
            results.append(f"{superhero1_name} has higher {stat}: {stat1} vs {superhero2_name} {stat2}.")
        elif stat1 < stat2:
            results.append(f"{superhero2_name} has higher {stat}: {stat2} vs {superhero1_name} {stat1}.")
        else:
            results.append(f"Both {superhero1_name} and {superhero2_name} have the same {stat}: {stat1}.")

    return "\n".join(results)

def chatbot():
    print("""Welcome! I am SuperBot, the Superhero Chatbot! I have data on heroes and villains from many universes, including DC, Marvel, Star Wars and IDW. 
    I have info about hundreds of characters.
    Ask away.
    Type 'exit' to leave.""")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Extract the superhero's name from the question
        match = re.search(r'(what|who|when) (is|are|was) ([\w\s\-]+)(\'s| is|\'| )', user_input, re.IGNORECASE)
        if match:
            character_name = match.group(3).strip()  # Group 3 captures the name including spaces
            superhero_data = get_character_data(character_name)
            extracted_data = extract_superhero_data(superhero_data, character_name)

            if "error" in extracted_data:
                print(f"Superbot: {extracted_data['error']}")
            else:
                response = answer_question(extracted_data, user_input)
                print(f"Superbot: {response}")
            continue  # Skip to the next iteration after handling the question

        # Handle comparison questions
        match = re.search(r'(.+?) vs (.+?): (.+)', user_input, re.IGNORECASE)
        if match:
            character1 = match.group(1).strip()
            character2 = match.group(2).strip()
            comparison_type = match.group(3).strip().lower()

            stats_to_compare = []
            if comparison_type == "fight":
                stats_to_compare = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']

            data1 = get_character_data(character1)
            data2 = get_character_data(character2)

            extracted_data1 = extract_superhero_data(data1, character1)
            extracted_data2 = extract_superhero_data(data2, character2)

            if "error" in extracted_data1:
                print(f"Superbot: {extracted_data1['error']}")
            elif "error" in extracted_data2:
                print(f"Superbot: {extracted_data2['error']}")
            else:
                result = compare(extracted_data1, extracted_data2, stats_to_compare)
                print(f"Superbot: {result}")
        else:
            print("Superbot: I didn't understand that. Please ask about a superhero's data.")


# Start the chatbot
chatbot()
