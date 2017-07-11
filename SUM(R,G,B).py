from __future__ import print_function
from PIL import Image, ImageFilter
import numpy as np
import math
import os
import sys
import csv

def load_images(folder,image):
	R=0
	G=0
	B=0
	image = os.path.join(folder,image)
	im = Image.open(image)
	pix = im.load()
	width, height = im.size
	for i in range(width):
		for j in range(height):
			R+=pix[i,j][0]
			G+=pix[i,j][1]
			B+=pix[i,j][2]        

	tab = [R,G,B,width,height,float(im.size[0])/im.size[1],os.path.getsize(image)/1024]
	print (tab)
	
def main():

	with open('test.csv','rb') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			i = 0
			while i < len(row[25]):
				if row[25][i] == '\"':
					#print (row[25][i-3]+', '+row[25][i+1:i+11])
					load_images('thumb',row[25][i+1:i+11])
					i=i+12
				i+=1
	
	
main()