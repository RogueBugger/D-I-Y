
from selenium import webdriver

pages = 10

url = 'https://ww2.naruspot.tv/watch/naruto-episode-1-dubbed/'
path_to_chrome = ''
driver = webdriver.Chrome(path)
for page in range(1,pages):
    url = f'https://ww2.naruspot.tv/watch/naruto-episode-{page}-dubbed/'
    driver.get(url)
button = driver.find_element_by_id('buttonID')
button.click()






