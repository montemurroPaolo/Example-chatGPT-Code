import os
import csv
import requests
import progressbar
from datetime import datetime

# Create a folder with the current date
now = datetime.now()
date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
os.mkdir(f"C:/Users/monte/OneDrive/Desktop/scrapingr/{date_time}")

# Read the csv file
with open('C:/Users/monte/OneDrive/Desktop/scrapingr/links.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    links = [row[0] for row in csv_reader]

# Remove "\n" from all the links
links = [link.replace('\n', '') for link in links]

# Select only the rows from links.csv that have an extension .gifv, .mp4, .jpg or .png, and need to start with https:// or www.
links = [link for link in links if link.endswith(('.gifv', '.mp4', '.jpg', '.png')) and (link.startswith('https://') or link.startswith('www.'))]

# If the extension of the link provided terminates in ".gifv" modify the link to ".mp4": example https://i.imgur.com/f3c19QC.gifv becomes https://i.imgur.com/f3c19QC.mp4
links = [link.replace('.gifv', '.mp4') if link.endswith('.gifv') else link for link in links]

# Create a progress bar
bar = progressbar.ProgressBar(maxval=len(links), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

# Download the files
for i, link in enumerate(links):
    response = requests.get(link)
    file_name = link.split('/')[-1]
    with open(f"C:/Users/monte/OneDrive/Desktop/scrapingr/{date_time}/{file_name}", 'wb') as file:
        file.write(response.content)
    bar.update(i+1)
    print(f"downloaded {link} {i+1} out of {len(links)}")

bar.finish()