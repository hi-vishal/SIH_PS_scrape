#import warnings
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}
url = "https://sih.gov.in/sih2024PS"
#warnings.filterwarnings("ignore")
r = requests.get(url, headers=headers, verify=False)
with open("sih.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Done Scraping")