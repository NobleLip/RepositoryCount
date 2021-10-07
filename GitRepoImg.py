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

imagesToChose = ['0.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
imagesNum = []
for i in Val:
	imagesNum.append(imagesToChose[int(i)])
images = [Image.open(x) for x in imagesNum]

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('Counter.png')

