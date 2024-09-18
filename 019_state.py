# Video alternative: https://vimeo.com/954334376/0c486313d0#t=625

# Here's a mindbender for you:

a = 10
b = 20
a = b
print(f"a is {a}")
print(f"b is {b}")

# @TASK: What does that output? And why? Take a guess, then
# run the code and see.
a = 10 # value 10 is assigned to a
b = 20 # value 20 is assigned to b
a = b # telling python whatever value is B should now be assigned to a
#when we instruct python to print b, the value remains 20 has it has not changed
20
20

# Was it what you expected?
#Yes

# Try to puzzle it out, and then move on to
# 020_state_tables.py
