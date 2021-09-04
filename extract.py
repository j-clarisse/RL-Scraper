# Function gets the links and scrapes each for CSV

import requests
from bs4 import BeautifulSoup


def Extract(links):
  cont = input("Continue scraping for CSV? y/n ---> ")
  if (cont.lower() !="y"):
    print("Stopping...")
    exit()

  print(links)
  print(type(links))
  # Create a file 'csvDownloads.txt' to store csv download links
  with open('csvDownloads.txt', 'w') as f:
    # Loop through contents, extract CSV download link
    for c in contents:
      URL = f"https://ballchasing.com{c}#export"
      page = requests.get(URL)
      soup = BeautifulSoup(page.content, "html.parser")
      details_export = soup.find("div", id="details-export")
      data = details_export.find("a",href=True)
      # Print link in file
      print(data['href'], file=f)
