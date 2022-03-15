from random import shuffle
from people_to_consider import people # construct the list of people to draw from
import logging
from datetime import datetime 
import csv

dt = datetime.now() 
logging.basicConfig(filename='run.log', level=logging.DEBUG)
logging.info(f"People in scope on {dt}: {people}")

# shuffle the list
shuffle(people)

# select the top three from the list
selection = people[:3]

# ask user if they want to write to these people
responses = []
for p in selection:
	brk_flg = True
	while brk_flg:
		x = int(input(f"Write to {p} at this time?"))

		if x in [0,1]:
			brk_flg = False
		else:
			print("Invalid response. Use 1 or 0")
	responses.append([dt, p, x])

# print(responses)
# # store in table
with open("history.csv", "a", newline="") as fp:
	writer = csv.writer(fp)
	writer.writerows(responses)

