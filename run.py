# FINAL
from scraper import ScrapePlayer
from extract import Extract

#player = input("What is your player string? ")
player = "Epic%3a39807794e0b843d4a3d678765c286cbb"

URL = f"https://ballchasing.com/?player-name={player}&sort-by=date&sort-dir=desc"
print(URL)

#print("https://ballchasing.com/?player-name=Epic%3A39807794e0b843d4a3d678765c286cbb&sort-by=date&sort-dir=desc")

# Run Scraper with URL
#ScrapePlayer(URL)

# Get list of links
with open('links.txt', 'r') as f:
  contents = f.read().splitlines() 
  #print(contents)

Extract(contents)