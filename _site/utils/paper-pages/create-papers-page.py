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
abstractData = pd.read_csv('../schedule-data/Icaps_papers_abstract.csv',header=0, encoding='latin-1')
# abstractData2 = pd.read_csv('../schedule-data/abstract_papers_journals.csv', header=0)
scheduleData = pd.read_csv('../schedule-data/paper_details.csv',header=0)
# print (linkData.keys())
# print (abstractData.keys())
#abstractData["PaperIDInt"]=[]
for i in range(len(abstractData['PaperID'])):
	intPaperData = re.sub("[^0-9]", "", abstractData['PaperID'][i])
	abstractData["PaperID"][i] = str(intPaperData)
# print (list(abstractData["PaperID"]))
pdfData = pd.read_csv('icaps_pdfs.csv',header=0)

# for i in range(len(pdfData['Title'])):
# 	pdfData['Title'][i] = pdfData['Title'][i].lower()
for i in range(len(pdfData['Title'])):
	intPaperData = re.sub("[^0-9]", "", pdfData['Paper ID'][i])
	pdfData["Paper ID"][i] = str(intPaperData)

videoData = pd.read_csv('paperid-to-videoid.csv',header=0,delimiter=";")
print (videoData.keys())
for i in range(len(linkData['Paper ID'])):
	if not isNaN(str(linkData['Paper ID'][i])):
		paper_id = linkData['Paper ID'][i]
		video_feed = videoData["VideoID"][list(videoData["PaperID"]).index((int(paper_id)))]

		pdflink = ""
		# if int(paper_id) < 351:
		pdflink = pdfData['pdf link'][list(pdfData['Paper ID']).index(str(int(paper_id)))]

		if not os.path.exists('../../papers/'+str(int(linkData['Paper ID'][i]))+'/'):
			os.mkdir('../../papers/'+str(int(linkData['Paper ID'][i]))+'/')

		paper_id = linkData['Paper ID'][i]
		abstract = ""
		try:
			abstract_paper_ID_index = list(abstractData['PaperID']).index(str(int(paper_id)))
			abstract = abstractData["Abstract"][abstract_paper_ID_index]
		except:
			print (paper_id)
			# abstract_index2 = list(abstractData2['paper_id']).index(str(int(paper_id)))
			# abstract = abstractData2["abstract"][abstract_ndex2]
		schedule_paper_ID_index = list(scheduleData['#']).index(paper_id)
		f2=open('../../papers/'+str(int(linkData['Paper ID'][i]))+'/'+'index.html','w')
		f2.write("---\ntitle: paper-"+str(int(linkData['Paper ID'][i]))+"\nlayout: page\n---"+"\n")
		f2.write("<head>\n<style>\ndiv1 {\n  background-color: lightgrey;\n  width: 30px;\n  border: 1px solid green;\n  padding: 5px;\n  margin: 1px;\n}\n")
		f2.write(".button {\n  border: none;\n  color: white;\n  padding: 6px 6px;\n  text-align: center;\n  text-decoration: none;\n  display: inline-block;\n  font-size: 16px;\n  margin: 4px 2px;\n  transition-duration: 0.4s;\n  cursor: pointer;\n}")
		f2.write(".button1 {\n  background-color: white; \n  color: black; \n  border: 2px solid #008CBA;\n}\n.button1:hover {\n  background-color: #008CBA;\n  color: white;\n}")
		f2.write(".button2 {\n  background-color: white;\n  color: black; \n  border: 2px solid red;\n}\n.button2:hover {\n  background-color: red;\n  color: white;\n}\n</style>\n</head>\n")

		f2.write("<div class='container'>\n  <div class='row'>\n      <div class='3u 12u(mobile)'>\n      <section>\n       ")
		# if int(paper_id) < 351:
		f2.write("<button class='button button2' onclick=\" window.open('"+pdflink+"','_blank')\"><input type='image' src='../../images/hyperlink-logo.png' width='14' height='13'> PDF</button>\n")

		f2.write("<br><br><h3 class='top'>Talk Sessions: </h3>\n")
		f2.write("<button class='button button1' onclick=\" window.open('"+str('http://icaps22.icaps-conference.org/schedule#')+str(scheduleData["Session1"][schedule_paper_ID_index])+"','_blank')\"><input type='image' src='../../images/hyperlink-blue.png' width='14' height='13'>June "+str(20+int(scheduleData["Session1_date"][schedule_paper_ID_index]))+", Session "+str(scheduleData["Session1"][schedule_paper_ID_index])+"</button>\n")
		f2.write("<button class='button button1' onclick=\" window.open('"+str('http://icaps22.icaps-conference.org/schedule#')+str(scheduleData["Session2"][schedule_paper_ID_index])+"','_blank')\"><input type='image' src='../../images/hyperlink-blue.png' width='14' height='13'>June "+str(20+int(scheduleData["Session2_date"][schedule_paper_ID_index]))+", Session "+str(scheduleData["Session2"][schedule_paper_ID_index])+"</button>\n")
		f2.write("<br><br><h3 class='top'>Poster Sessions: </h3>\n")
		f2.write("<button class='button button2' onclick=\" window.open('"+str('http://icaps22.icaps-conference.org/posters/')+str(linkData['Poster PDF Name'][i])+"','_blank')\"><input type='image' src='../../images/hyperlink-logo.png' width='14' height='13'> Poster</button><br><br>\n")
		f2.write("<div1> June "+str(20+ int(linkData['Day1_id'][i]))+", Booth "+str(int(linkData['Posterid_day1'][i]))+"</div1> <br><br>\n")
		f2.write("<div1> June "+str(20+int(linkData['Day2_id'][i]))+", Booth "+str(int(linkData['Posterid_day2'][i]))+"</div1> <br><br>\n")
		f2.write("</section>\n </div>\n")

		f2.write("<div class='9u 12u(mobile)'>\n    <section>\n      <header>\n        <h1 class='top'>"+scheduleData['Title'][schedule_paper_ID_index]+"</h1>\n        <h3>"+scheduleData['Authors'][schedule_paper_ID_index]+"</h3>\n      </header>\n<b>Abstract:</b> "+abstract+"<br><br>\n")
		f2.write("<div id='presentation-embed-"+str(video_feed)+"'></div>\n")
		f2.write("<script src='https://slideslive.com/embed_presentation.js'></script>\n<script>\n")
		f2.write("embed = new SlidesLiveEmbed('presentation-embed-"+str(video_feed)+"', { \n presentationId: '"+str(video_feed)+"',\n autoPlay: false,\n verticalEnabled: true, \n   });\n</script>\n")
		f2.write("<h4><p style='color:red'><sup>*</sup>This password protected talk video will only be available after it was presented at the conference.</p></h4>")
		f2.write("</section>\n  </div>\n  </div>\n</div>")

		f2.close()
		if paper_id==373:
			break

