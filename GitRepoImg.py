from PIL import Image
import requests
from bs4 import BeautifulSoup

import argparse

parser = argparse.ArgumentParser(description="Generate repo count image from GitHub profile.")
parser.add_argument('username', help='GitHub profile username')
args = parser.parse_args()


r = requests.get('https://github.com/'+args.username)
Soup = BeautifulSoup(r.text, 'html.parser')
Val = Soup.find_all(class_='Counter')
for i in Val:
	for j in i:
		Val = j
		break
	break
## Get Repo Number Done
Val = list(str(Val))

imagesToChose = ['Imgs/0.png','Imgs/1.png','Imgs/2.png','Imgs/3.png','Imgs/4.png','Imgs/5.png','Imgs/6.png','Imgs/7.png','Imgs/8.png','Imgs/9.png']
imagesNum = []
for i in Val:
	imagesNum.append(imagesToChose[int(i)])
images = []
for x in range(len(imagesNum)):
	images.append(Image.open(imagesNum[x]))
	images[x].convert("RGBA")


widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGBA', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('Counter.png', "PNG")

