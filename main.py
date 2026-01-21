from func.scrape import scrape
from func.extract import extract
from func.send_email import send_email
from func.read import read
from func.store import store
import time

url = "http://programmer100.pythonanywhere.com/tours/"

def main():
    scraped = scrape(url)
    print(scraped)
    extracted = extract(scraped)
    contents = read()

    if extracted != "No upcoming tours" and extracted not in contents:
        store(extracted)
        send_email()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
