import random
from typing import runtime_checkable

nouns = ["Python", "JavaScript", "Java", "C++", "React", "HTML", "Computer Vision", "IoT", "Machine Learning"]

products = ["Web-Scraper", "Music-player", "User-Interface", "Game", "GUI app", "Software", "App", "Website", "API", "Algorithm",
"Health tracker", "To-Do app"]

print("\nPython Project Recommendor\n\n")

bool = True

def recommend():
    noun = random.choice(nouns)
    product = random.choice(products)
    print(f"Project Idea: Build a {product} using {noun}!")


while(bool):
    recommend()
    again = str(input("Do you want another idea? (Y/N): "))
    if(again == 'y' or again == 'Y'):
        bool = True
    if(again == 'n' or again == 'N'):
        bool = False


