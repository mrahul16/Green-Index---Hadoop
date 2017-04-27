import csv
from PIL import Image
import numpy as np

jpgs = ["green", "thar", "cubbon", "cubbonpark", "myarea"]
counter = 0

print("Starting conversion of {} images".format(len(jpgs)))
for jpg in jpgs:
	img = Image.open("../img/" + jpg + "/" + jpg + ".jpg")
	p = np.array(img)

	with open('generated/'+jpg+'.rgb', 'w', newline='') as csvfile:
		rgbwriter = csv.writer(csvfile)
		for row in p:
			for column in row:
				rgbwriter.writerow(column)

	counter += 1
	print("{}/{} Converted {}.jpg".format(counter, len(jpgs), jpg))
