import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def main():

    if len(sys.argv) != 2:
        print("Kindly enter a valid URL first")
        sys.exit(1)

    url = sys.argv[1].strip()

    if not url.startswith("http"):
        url = "https://" + url

    print("Your entered url is:", url)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")


    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        time.sleep(10)

        html = driver.page_source
        driver.quit()

    except Exception as e:
        print("Couldn't fetch the page:", e)
        return
    
    soup = BeautifulSoup(html, "html.parser")
    # soup = BeautifulSoup(get_response.text,"html.parser")

    
    if(soup.title and soup.title.text):
        titles = soup.title.text
        print("Titles are:")
        print(titles)
    else:
        print("This page contains no title")
    print("\n")
    

    if soup.body:
        body = soup.body.get_text(separator="\n")
        print("Body_text Page is : ")
        print(body)
    else:
        print("This page contains no body tag")



    print("\n")
    links_set =set()
    links = soup.find_all("a")      #BeautifulSoup tag object
    for link in links:
        href = link.get("href")
        if href is not None:
            links_set.add(href)
    
    print("Set of unique links is:")
    # Print all the links
    for link in links_set:
        print(link)





if __name__ == "__main__":
    main()


    
