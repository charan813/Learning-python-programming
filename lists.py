# DON'T TOUCH THIS PLEASE!
people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

# Change "Hanna" to "Hannah"
people[0] = "Hannah"
# Change "Geoffrey" to "Jeffrey"
people[-2] = "Jeffrey"
# Change "aparna" to "Aparna" (capitalize it)
people[-1] = people[-1].capitalize()

print(people)

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ' '
for s in sounds:
    result += s.upper()
    print(result)

print(result)
# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
# Run the tests to make sure you've done this correctly!
print(instructors)
