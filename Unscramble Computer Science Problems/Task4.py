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
to_delete = set()
for caller, reciever, _, _ in calls:
    if reciever in result:
        to_delete.add(reciever)
    else:
        result.add(caller)
for caller, reciever, _ in texts:
    to_delete.add(caller)
    to_delete.add(reciever)

result = sorted(result - to_delete)
print("These numbers could be telemarketers: ", *result, sep="\n")



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

