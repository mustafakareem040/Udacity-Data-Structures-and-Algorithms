"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

result = set()
for income, outcome, _ in texts:
    result.add(income)
    result.add(outcome)
for income, outcome, _, _ in calls:
    result.add(income)
    result.add(outcome)
count = len(result)
print(f'There are {count} different telephone numbers in the records.')

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
