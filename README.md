# Superbot
Welcome to SuperBot, a chatbot designed to provide information about various superheroes and villains from multiple universes, including DC, Marvel, Star Wars, and IDW. With SuperBot, you can ask questions about superhero profiles, compare characters, and explore their unique attributes.

Data extracted from SuperheroAPI( https://superheroapi.com/index.html )-you need a GitHub account to gain access to it.

Features:

Retrieve detailed information about superheroes, including:
    
    Full Name
    Alter Egos
    Aliases
    Place of Birth
    First Appearance
    Publisher
    Alignment
    Gender
    Race
    Height
    Weight
    Eye Color
    Hair Color
    Power Stats (Intelligence, Strength, Speed, Durability, Power, Combat)
    Group Affiliation
    Relatives

    
Compare two superheroes based on their stats.
Interactive chatbot interface for user engagement.
Supports various question formats.

## Inputs
Retrieve Superhero Data: You can ask questions such as:
"What is Batman's full name?"
"Who is Spider-Man's publisher?"

Compare Superheroes: You can compare superheroes by typing:
"Batman vs Superman: fight"
"Batman vs Superman: Intelligence"

Full Profile: Request a full profile(all of the above info) by asking:
"What is Iron Man's full profile?"

More detail on what can be called in "Data Used.txt"



## Requirements:
Python 3.x
requests library
An API key from Superhero API

Retrieve Superhero Data: You can ask questions such as:
"What is Batman's full name?"
"Who is Spider-Man's publisher?"


Compare Superheroes: You can compare superheroes by typing:
"Batman vs Superman: fight"
"Batman vs Superman: Intelligence"

Full Profile: Request a full profile(all of the above info) by asking:
"What is Iron Man's full profile?"

More detail on what can be called in "Data Used.txt"


## Warning
There is an issue with the program in that it is unable to distinguish between characters with the same "superhero name". For example, if you want to ask for Batman's details, it will provide you with Terry McGinnis. This is because whoever made the API didn't distinguish in "name" value for certain characters(did for others though-i.e Flash, Flash II, Flash III). I have been unable to figure out how to get past this so far. If you see this and have any ideas, let me know.


