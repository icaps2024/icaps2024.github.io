import pandas as pd
import numpy as np
import csv

def read_csv_to_dataframe(file_location):
	df = pd.read_csv(file_location)
	return df

def write_csv_to_dataframe(data, file_location):
	data.to_csv(file_location, header=True, index=False)


if __name__=="__main__":
	schedule_file_loc = "schedule.csv"
	paper_file_loc = "paper_data.csv"
	session_file_loc = "session_data.csv"

	schedule_df = pd.read_csv(schedule_file_loc, encoding='ISO-8859-1')
	paper_df = read_csv_to_dataframe(paper_file_loc)
	session_df = read_csv_to_dataframe(session_file_loc)

	session_details = {} # every session has following items [day, hour, duration, title, paperIds]
	for id in range(len(session_df['session_code'])):
		session_details[session_df['session_code'][id]] = []
		session_details[session_df['session_code'][id]].append(session_df['session_day'][id]) # day
		session_details[session_df['session_code'][id]].append(session_df['session_hour'][id]) # hour
		session_details[session_df['session_code'][id]].append(session_df['session_duration'][id]) # duration
		session_details[session_df['session_code'][id]].append(session_df['session_title'][id]) # title
		paperIds = str(int(session_df['paper_1'][id])) + ", " + str(int(session_df['paper_2'][id])) + ", " + str(int(session_df['paper_3'][id]))
		if not np.isnan(session_df['paper_4'][id]):
			paperIds = paperIds + ", " + str(int(session_df['paper_4'][id]))
		if not np.isnan(session_df['paper_5'][id]):
			paperIds = paperIds + ", " + str(int(session_df['paper_5'][id]))
		session_details[session_df['session_code'][id]].append(paperIds) # paperIds

	updated_schedule_data = {}
	paper_keys = ["Slot", "Time", "Day", "Weekday",	"Type", "Session1", "Session2", "Session1_title", "Session2_title", "Session1_papers", "Session2_papers"]
	for k in paper_keys:
		updated_schedule_data[k] = []
	
	for id in range(len(schedule_df['Slot'])):
		updated_schedule_data["Slot"].append(schedule_df['Slot'][id])
		updated_schedule_data["Time"].append(schedule_df['Time'][id])
		updated_schedule_data["Day"].append(schedule_df['day'][id])
		updated_schedule_data["Weekday"].append(schedule_df['weekday'][id])
		updated_schedule_data["Type"].append(schedule_df['type'][id])
		updated_schedule_data["Session1"].append(schedule_df['session1'][id])
		updated_schedule_data["Session2"].append(schedule_df['session2'][id])
		try:
			updated_schedule_data["Session1_title"].append(session_details[schedule_df['session1'][id]][3])
			updated_schedule_data["Session1_papers"].append(session_details[schedule_df['session1'][id]][4])
		except KeyError:
			updated_schedule_data["Session1_title"].append(np.nan)
			updated_schedule_data["Session1_papers"].append(np.nan)
		try:
			updated_schedule_data["Session2_title"].append(session_details[schedule_df['session2'][id]][3])
			updated_schedule_data["Session2_papers"].append(session_details[schedule_df['session2'][id]][4])
		except KeyError:
			updated_schedule_data["Session2_title"].append(np.nan)
			updated_schedule_data["Session2_papers"].append(np.nan)

	schedule_write_loc = "icaps_schedule_details.csv"	
	write_csv_to_dataframe(pd.DataFrame.from_dict(updated_schedule_data), schedule_write_loc)

	