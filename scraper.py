import requests
from bs4 import BeautifulSoup
import sys



def ScrapePlayer(URL):
  cont = input("Continue scraping? y/n ---> ")
  if (cont.lower() !="y"):
    print("Stopping...")
    exit()

  print('Continuing...')
  # Get content from URL
  #URL = "https://ballchasing.com/?player-name=Epic%3A39807794e0b843d4a3d678765c286cbb&sort-by=date&sort-dir=desc"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  # Get first 10 links of replays and print into file 'links.txt'
  with open('links.txt', 'w') as f:
    links = soup.find_all("a", class_="replay-link")
    count = 0
    while (count < 10):
      count+=1
      print(links[count]['href'], file=f)
      #print('hello world!!', file=f)
    #f.close()

  print("All done!!")