import requests
import random
from bs4 import BeautifulSoup

user_agent_list = [
    # Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    # Firefox
    "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
]

# Main func that downloads the images in images folder
# Used pgSLideshow from github to show as slideshow
# This function downloads 10 images you can change the counter
# Having a good connection helps
# Used requests to get html and bs4 to parse links
# urllib to download images
def download_images(query):
    url = (
        "https://www.bing.com/images/search?q="
        + query
        + "&qs=n&form=QBILPG&sp=-1&pq=&sc=1-0&sk=&cvid=614998763FC2470EA5F3AE69AEB0D3AF"
    )

    r = requests.head(url, allow_redirects=True)

    r = requests.get(r.url, headers={"User-Agent": random.choice(user_agent_list)})
    print(r.url)

    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("a", class_="iusc")
    img_links = []
    import ast

    print(r.url)
    for link in links:
        img_links.append(ast.literal_eval(link["m"])["murl"])
    import urllib

    for img in img_links[:10]:
        name = ""
        i = len(img) - 1
        while img[i] != "/":
            if img[i] == "+":
                name += " "
            else:
                name += img[i]
            i -= 1
        name = name[::-1].lower()
        print(name)
        try:
            urllib.request.urlretrieve(img, "images/" + name)
        except:
            pass


def show_images():
    global e
    from glob import glob
    import os

    for i in glob("images/*"):
        try:
            os.remove(i)
        except:
            pass
    query = e.get()
    download_images(query)

    import pgSlideShow

    pgSlideShow.main("images/.")


from tkinter import *

root = Tk()

root.title("Name")

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root, text="okay", command=show_images)
b.pack(side="bottom")
root.mainloop()
