import requests
from bs4 import BeautifulSoup
import csv
import os

# Let autopilot take the wheel for this os command
#Looks for directory and creates
output_dir = 'web_scraping_assignments'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

characters = ["SpongeBob", "Patrick", "Squidward", "Mr. Krabs", "Plankton", "Sandy", "Gary", "Mrs. Puff", "Karen", "Pearl", "Sam", "Bubble Bass", "Mermaid Man", "Barnacle Boy", "DoodleBob", "Larry", "Squilliam", "Dutchman", "Fred"]
character_counts = {character: 0 for character in characters}

url = "https://spongebob.fandom.com/wiki/List_of_episodes"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


episode_list = soup.find_all('div', class_='mw-parser-output') #found correct on inspect

for episode in episode_list:
    description = episode.get_text().lower()  

    for character in character_counts:
        
        character_counts[character] += description.count(character.lower())


for character, count in character_counts.items():
    print(f"{character}: {count} mentions")

# Save to CSV
with open('web_scraping_assignments/character_counts.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Character", "Count"])
    writer.writeheader()
    for character, count in character_counts.items():
        writer.writerow({"Character": character, "Count": count})
