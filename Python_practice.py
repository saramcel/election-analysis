#print("Hello World")
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#90    print(counties[1])
#temperature = int(input("What is the temperature outside? "))
#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

for county in counties:
    print(county)
#use a for loop to print from a dictionary
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    #use a string and concatenation, and make the voters value into a string for printing
    print(county + " county has " + str(voters) + " registered voters.")
#now try the same thing with f-string in the for loop
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    #it prints the same thung but with less code

#multiple lines of printing with f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)