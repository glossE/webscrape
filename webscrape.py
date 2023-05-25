import os
import requests
import pdfkit
from bs4 import BeautifulSoup


# Path to the wkhtmltopdf executable
# Modify this path based on the installation location of wkhtmltopdf on your system
wkhtmltopdf_path = r'/path/to/wkhtmltopdf'

# Set the path to the wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)


# URL of the webpage to scrape
url = 'https://www.w3schools.com/nodejs'

# Send a GET request to the webpage
response = requests.get(url)
response.raise_for_status()

# Extract the HTML content from the response
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the element(s) containing the data you want to scrape
data = soup.find("div", class_="w3-container")

# Extract the text from the element(s)
text = data.get_text()

# Save the scraped text to a temporary HTML file
with open("temp.html", "w", encoding="utf-8") as file:
    file.write(text)

# Convert the temporary HTML file to PDF
pdfkit.from_file("temp.html", "output.pdf", configuration=config)

# Remove the temporary HTML file
os.remove("temp.html")

print("PDF created successfully!")

