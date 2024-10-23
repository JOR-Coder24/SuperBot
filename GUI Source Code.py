import requests
import re
import config
import tkinter as tk
from tkinter import scrolledtext

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
    superhero1_name = superhero1_data.get('Name', 'Unknown')
    superhero2_name = superhero2_data.get('Name', 'Unknown')

    superhero1_score = 0
    superhero2_score = 0

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
            superhero1_score += 1  # Increment score for superhero 1
        elif stat1 < stat2:
            results.append(f"{superhero2_name} has higher {stat}: {stat2} vs {superhero1_name} {stat1}.")
            superhero2_score += 1  # Increment score for superhero 2
        else:
            results.append(f"Both {superhero1_name} and {superhero2_name} have the same {stat}: {stat1}.")

    # Determine winner
    if superhero1_score > superhero2_score:
        results.append(f"\n{superhero1_name} wins {superhero1_score}-{superhero2_score}!")
    elif superhero2_score > superhero1_score:
        results.append(f"\n{superhero2_name} wins {superhero2_score}-{superhero1_score}!")
    else:
        results.append(f"\nIt's a tie with a score of {superhero1_score}-{superhero2_score}!")

    return "\n".join(results)

# GUI function
def chatbot_gui():
    def send_message():
        user_input = entry.get()

        chat_area.insert(tk.END, f"You: {user_input}\n", 'user')  # Insert user text with 'user' tag

        if user_input.lower() == 'exit':
            window.quit()

        match = re.search(r'(what|who|when) (is|are|was) ([\w\s\-]+)(\'s| is|\'| )', user_input, re.IGNORECASE)
        if match:
            character_name = match.group(3).strip()
            superhero_data = get_character_data(character_name)
            extracted_data = extract_superhero_data(superhero_data, character_name)

            if "error" in extracted_data:
                chat_area.insert(tk.END, f"SuperBot: {extracted_data['error']}\n", 'bot')  # Insert bot text with 'bot' tag
            else:
                response = answer_question(extracted_data, user_input)
                chat_area.insert(tk.END, f"SuperBot: {response}\n", 'bot')
        else:
            match = re.search(r'(.+?) vs (.+?): (.+)', user_input, re.IGNORECASE)
            if match:
                character1 = match.group(1).strip()
                character2 = match.group(2).strip()
                comparison_type = match.group(3).strip().lower()

                stats_to_compare = []
                if comparison_type == "fight":
                    stats_to_compare = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
                else:
                    available_stats =  ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']

                    # If the comparison type matches one of the available stats, compare only that stat
                    if comparison_type in available_stats:
                        stats_to_compare = [comparison_type]
                    else:
                        chat_area.insert(tk.END,"SuperBot: I don't understand that comparison. Please specify a valid stat (e.g., 'speed', 'strength').\n",'bot')
                        return

                data1 = get_character_data(character1)
                data2 = get_character_data(character2)

                extracted_data1 = extract_superhero_data(data1, character1)
                extracted_data2 = extract_superhero_data(data2, character2)

                if "error" in extracted_data1:
                    chat_area.insert(tk.END, f"SuperBot: {extracted_data1['error']}\n", 'bot')
                elif "error" in extracted_data2:
                    chat_area.insert(tk.END, f"SuperBot: {extracted_data2['error']}\n", 'bot')
                else:
                    result = compare(extracted_data1, extracted_data2, stats_to_compare)
                    chat_area.insert(tk.END, f"SuperBot: {result}\n", 'bot')
            else:
                chat_area.insert(tk.END, "SuperBot: I didn't understand that. Please ask about a superhero's data.\n", 'bot')

        entry.delete(0, tk.END)

    # Set up the GUI
    window = tk.Tk()
    window.title("Superhero Chatbot")

    # Create a chat area with scroll
    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='normal')
    chat_area.grid(column=0, row=0, columnspan=2, sticky='nsew')  # Make the chat area expand

    # Tag configuration for user and bot text
    chat_area.tag_configure('user', foreground='red')  # User text in red
    chat_area.tag_configure('bot', foreground='blue')   # Bot text in blue

    # Entry widget for user input
    entry = tk.Entry(window, width=50)
    entry.grid(column=0, row=1, sticky='ew')  # Allow entry to expand

    # Send button to process the user input
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.grid(column=1, row=1)

    # Configure row and column weights to allow expansion
    window.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    window.grid_rowconfigure(0, weight=1)     # Allow row 0 to expand
    window.grid_rowconfigure(1, weight=0)     # Row 1 (where the entry and button are) stays fixed

    window.mainloop()

# Start the GUI chatbot
chatbot_gui()
