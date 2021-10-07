from PIL import Image
import requests
from bs4 import BeautifulSoup
r = requests.get('https://github.com/NobleLip')
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
images = [Image.open(x) for x in imagesNum]

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGBA', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('Counter.png', "PNG")

