import os
from bs4 import BeautifulSoup
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

# Path to the "data" directory
data_dir = r"C:\Users\USER\Desktop\Selenium_Test\Test\data"

# Iterate over each file in the "data" directory
for file in os.listdir(data_dir):
    if file.endswith(".html"):
        try:
            # Construct the full file path
            file_path = os.path.join(data_dir, file)

            # Open and read the HTML file
            with open(file_path, "r", encoding="utf-8") as f:
                html_doc = f.read()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_doc, 'html.parser')

            # Find the first h2 tag and extract the title
            t = soup.find("h2")
            if t:
                title = t.get_text()

                # Find the link within the h2 tag (assuming it has an <a> tag)
                l = t.find("a")
                if l and l.has_attr('href'):
                    link = "https://amazon.in/" + l['href']
                else:
                    link = "No link found"

                # Find the span tag with class 'a-price-whole' for the price
                p = soup.find("span", attrs={"class": 'a-price-whole'})
                if p:
                    price = p.get_text(strip=True)
                else:
                    price = "No price found"

                # Append the extracted data to the dictionary
                d['title'].append(title)
                d['price'].append(price)
                d['link'].append(link)

                # Print the title, link, and price
                print(f"Title: {title}")
                print(f"Link: {link}")
                print(f"Price: {price}")
            else:
                print(f"No title found in {file}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

# Convert the dictionary to a DataFrame and save it to a CSV file
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)
