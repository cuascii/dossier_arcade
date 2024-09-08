# -*- coding: utf-8 -*-
"""Dossier Task 1.ipynb

Automatically generated by Colab.


# Creating a Soup Element and getting all the data
"""

# importing libraries
import requests
from bs4 import BeautifulSoup

# declaring url to scrape the data from
url = "https://christuniversity.in"

# scraping the data from the website
response = requests.get(url)

# creating the soup element
soup = BeautifulSoup(response.text, "html.parser")

"""# Finding the desired output using soup and pandas library"""

# Gathering all the link ('a') tags available in the website
links = soup.find_all("a")
print(f"Number of links: {len(links)}")
for link in links:
    print(link.get("href"))

# Gathering all the image ('img') tags available in the website
images = soup.find_all("img")
print(f"Number of images: {len(images)}")
for image in images:
    print(image.get("src"))

# importing pandas library for storing the output in a tabular form
import pandas as pd

# Creating DataFrame using the pandas library
df = pd.DataFrame(columns=["Link Type", "URL"])

# Adding the values into the dataframe
for link in links:
    df = df._append({"Link Type": "Link", "URL": link.get("href")}, ignore_index=True)

for image in images:
    df = df._append({"Link Type": "Image", "URL": image.get("src")}, ignore_index=True)

print(df)

# removing all the null values from the dataframe
df.dropna(inplace=True)

# removing all the values that is not a link or a src
df = df[df["URL"].str.startswith("https://")]
print(df)

# Calculating the number of links and images in the website
df["Link Type"].value_counts().to_csv("Original_Links_Count.csv")

# removing all the duplicate links from the datframe
df.drop_duplicates(subset=["URL"], inplace=True)
print(df)

df["Link Type"].value_counts().to_csv("Update_Links_Count.csv")

# Saving the dataframe into a csv file
df.to_csv("Links_Output.csv", index=False)
