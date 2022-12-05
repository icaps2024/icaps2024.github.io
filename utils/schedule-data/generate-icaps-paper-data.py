import pandas as pd
import numpy as np
import csv

def read_csv_to_dataframe(file_location):
	df = pd.read_csv(file_location)
	return df

def write_csv_to_dataframe(data, file_location):
	data.to_csv(file_location, header=True, index=False)


if __name__=="__main__":
	abstract_file_loc = "abstracts of papers + journals.csv"
	paper_file_loc = "paper_data.csv"
	session_file_loc = "session_data.csv"

	abstract_df = pd.read_csv(abstract_file_loc, encoding='ISO-8859-1')
	paper_df = read_csv_to_dataframe(paper_file_loc)
	session_df = read_csv_to_dataframe(session_file_loc)

	abstract_details = {} # paper id with abstract
	for id in range(len(abstract_df['paper_id'])):
		abstract_details[abstract_df['paper_id'][id]] = [abstract_df['abstract'][id]]

	session_details = {} # every session has following items [day, hour, duration, title]
	for id in range(len(session_df['session_code'])):
		session_details[session_df['session_code'][id]] = []
		session_details[session_df['session_code'][id]].append(session_df['session_day'][id]) # day
		session_details[session_df['session_code'][id]].append(session_df['session_hour'][id]) # hour
		session_details[session_df['session_code'][id]].append(session_df['session_duration'][id]) # duration
		session_details[session_df['session_code'][id]].append(session_df['session_title'][id]) # title

	updated_paper_data = {}
	paper_keys = ["#", "Authors", "Title", "Presenter","Track", "Session1", "Session2", "Session1_title", "Session2_title", "Session1_date", "Session2_date", "Session1_time", "Session2_time", "Session1_duration", "Session2_duration"]#, "Abstract"]
	for k in paper_keys:
		updated_paper_data[k] = []
	
	for id in range(len(paper_df['paper_id'])):
		updated_paper_data["#"].append(paper_df['paper_id'][id])
		updated_paper_data["Authors"].append(paper_df['paper_authors'][id])
		updated_paper_data["Title"].append(paper_df['paper_title'][id])
		# updated_paper_data["Abstract"].append(abstract_details[paper_df['paper_id'][id]][0])
		updated_paper_data["Track"].append(paper_df['paper_track'][id])
		updated_paper_data["Presenter"].append(paper_df['paper_presenter'][id])
		updated_paper_data["Session1"].append(paper_df['paper_session_1'][id])
		updated_paper_data["Session2"].append(paper_df['paper_session_2'][id])
		updated_paper_data["Session1_title"].append(session_details[paper_df['paper_session_1'][id]][3])
		updated_paper_data["Session2_title"].append(session_details[paper_df['paper_session_2'][id]][3])
		updated_paper_data["Session1_date"].append(session_details[paper_df['paper_session_1'][id]][0])
		updated_paper_data["Session2_date"].append(session_details[paper_df['paper_session_2'][id]][0])
		updated_paper_data["Session1_time"].append(session_details[paper_df['paper_session_1'][id]][1])
		updated_paper_data["Session2_time"].append(session_details[paper_df['paper_session_2'][id]][1])
		updated_paper_data["Session1_duration"].append(session_details[paper_df['paper_session_1'][id]][2])
		updated_paper_data["Session2_duration"].append(session_details[paper_df['paper_session_2'][id]][2])

	paper_write_loc = "paper_details.csv"	
	write_csv_to_dataframe(pd.DataFrame.from_dict(updated_paper_data), paper_write_loc)

	