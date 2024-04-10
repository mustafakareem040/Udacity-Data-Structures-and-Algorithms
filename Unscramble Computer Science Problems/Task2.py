"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
result = dict()
for n1, n2, _, d in calls:
    if result.get(n1):
        result[n1] += float(d)
    else:
        result[n1] = float(d)
    if result.get(n2):
        result[n2] += float(d)
    else:
        result[n2] = float(d)

phone_number = max(result, key=result.get)
duration = result[phone_number]
print(f"{phone_number} spent the longest time, {duration} seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

