import requests
from bs4 import BeautifulSoup as bs
import os

#website for scraping images
url = 'https://www.pexels.com/search/dogs/'

#download page to parse
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#locate elements w img tag
image_tags = soup.findAll('img')

#check for and/or make new folder to store imgs
if not os.path.exists('dogs'):
    os.makedirs('dogs')

#cd 
os.chdir('dogs')

x=0

for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('dog-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x+=1
    except:
        pass



