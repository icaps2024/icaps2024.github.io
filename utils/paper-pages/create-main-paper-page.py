import numpy as np
import pandas as pd
import os
import re
import math

def isNaN(value):
	if value!=value:
		return true
	# else:
	# 	return false

linkData = pd.read_excel('PaperDetails.xlsx', header=1)
scheduleData = pd.read_csv('../schedule-data/paper_details.csv',header=0)

with open('../../_posts/2022-02-20-papers-v2.html', 'r') as file :
  filedata = file.read()

for i in range(len(scheduleData['#'])):
	title = scheduleData['Title'][i]
	#paper_id = linkData['Paper ID'][list(linkData['Title']).index(title)]
	paper_id = scheduleData['#'][i]
	filedata = filedata.replace(title, "<a href='http://icaps22.icaps-conference.org/papers/" + str(paper_id) + "/index.html'>" + title +'</a>')


# with open('../../_posts/2022-02-20-papers.html', 'w') as file:
#   file.write(filedata)

file1= open('journal_track_papers.html','w')
file1.write("<h1>Journal Presentation Track Papers</h1> \n")
for i in range(len(scheduleData['#'])):
	title = scheduleData['Title'][i]
	#paper_id = linkData['Paper ID'][list(linkData['Title']).index(title)]
	paper_id = scheduleData['#'][i]
	authors = scheduleData['Authors'][i]
	if paper_id>350:
		file1.write("<div class='paper'><span class='authors'><span>" + authors+"</span>. </span><span class='title'><a href='http://icaps22.icaps-conference.org/papers/"+str(paper_id)+"/index.html'>"+title+"</a> </span></div>"+"\n")
file1.close()
