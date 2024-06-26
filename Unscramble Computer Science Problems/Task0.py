"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    target = texts[0]
    print(f'First record of texts, {target[0]} texts {target[1]} at time {target[2]}')

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    target = calls[-1]
    print(f"Last record of calls, {target[0]} calls {target[1]} at time {target[2]}, lasting {target[3]} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

