import csv
state = ["Nevada","NV"]
file1 = open('State_Sentiment.csv') 
reader = csv.DictReader(file1)
result ={};
for row in reader:
	location = row["tweet_location"]
	locationarr = location.split()
	for word in locationarr:
		if word in state:
			candidate = row['candidate']
			if row['sentiment'] == "Positive" and candidate != "No candidate mentioned":
				if result[candidate] == "":
					result[candidate] = 0
				else:
					result[candidate] = result[candidate]+1
				print result[candidate]
	

