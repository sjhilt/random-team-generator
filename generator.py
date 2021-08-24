#################################
#
# Author: Stephen Hilt
# Date: 8/24/2021
# Purpose: To Randomly Generate Teams
#   based on a CSV with a given format 
#   which an example is seen in this project
#################################
import random
import csv
import os

# Define the number of teams, in this case 6
teams = { "1":[],
	"2":[],
	"3":[],
	"4":[],
	"5":[],
	"6":[]
	}

# To keep track of the player rankings as added to the team
teamScore = {"1":0,
	"2":0,
	"3":0,
	"4":0,
	"5":0,
	"6":0
	}

# The Team Captians of each Team, this will be used for printing info
teamCaptians = {"1": "CAP 1",
	"2": "CAP 2",
	"3": "CAP 3",
	"4": "CAP 4",
	"5": "CAP 5",
	"6": "CAP 6"
	}
# player rankings based on a 3 teir scale 
playerRanks = {"1": [],
	"2":[],
	"3":[]
	}

# Add the Captians and Protected Players by Team # from CSV 
# change the CSV as needed but this will be the template name to test with
with open('random_league.csv') as csvfile, open('non_protected.csv', 'w') as writefile:
  # Read the file in
	playerReader = csv.reader(csvfile)
  # Set up a file writer to make a tmp CSV with out those protected
	writer = csv.writer(writefile)
  # Init Value 
	numPlayers = 0
  # Loop through the file, and find anyone who is 'protected' add them to the team
  # if they are not protected add them to a temp CSV 
	for row in playerReader: 
    # count the number of lines in the CSV as players
		numPlayers += 1
    # a variable to be used to ensure we only put the player in one place or the other. 
		trigered = 0
		for counter in range(1,7):
			if row[6] == str(counter):
				teams[str(counter)].append(row[0])
				teamScore[str(counter)] += int(row[5])
				trigered = 1
			elif not row[6] and trigered == 0:
				if row[0] != "Name":
					writer.writerow(row[:6])
					trigered = 1
# Now we know the total number of players, lets print the number
# and the max number of teams
print("Total Number of Players: %s" % numPlayers)
maxPlayers = round(numPlayers/len(teams))
print("Max Players Per Team: %s" % maxPlayers)


#Add the players to dicts based on their ranking
with open("non_protected.csv") as csvfile:
	playerReader = csv.reader(csvfile)
	for row in playerReader:
		if row[5] == "1" or row[5] == "0":
			playerRanks["1"].append(row[0])
		elif row[5] == "2":
			playerRanks["2"].append(row[0])
		elif row[5] == "3":
			playerRanks["3"].append(row[0])
# Randomly assign players ranked 1 to a team but ensure all teams do not go over the max number 
for player in playerRanks["1"]: 
	teamPlacement = random.choice(list(teams.keys()))
	placedPlayer = 0
	while placedPlayer == 0:
		if len(teams[teamPlacement]) <= maxPlayers and teamScore[teamPlacement] < 10:
			teams[teamPlacement].append(player)
			teamScore[teamPlacement] += 1
			placedPlayer = 1
		else: 
			teamPlacement = random.choice(list(teams.keys()))
## Randomly assign players ranked 2 to a team but ensure all teams do not go over the max number 
for player in playerRanks["2"]: 
	teamPlacement = random.choice(list(teams.keys()))
	placedPlayer = 0
	while placedPlayer == 0:
		if len(teams[teamPlacement]) <= maxPlayers and teamScore[teamPlacement] < 15:
			teams[teamPlacement].append(player)
			teamScore[teamPlacement] += 1
			placedPlayer = 1
		else: 
			teamPlacement = random.choice(list(teams.keys()))
# Randomly assign players ranked 3 to a team but ensure all teams do not go over the max number 
for player in playerRanks["3"]: 
	teamPlacement = random.choice(list(teams.keys()))
	placedPlayer = 0
	while placedPlayer == 0:
		if len(teams[teamPlacement]) <= maxPlayers and teamScore[teamPlacement] < 15:
			teams[teamPlacement].append(player)
			teamScore[teamPlacement] += 1
			placedPlayer = 1
		else: 
			teamPlacement = random.choice(list(teams.keys()))
      
## OUTPUT 
print("\n------ Player Ranks -----\n--\n--")
print("----------- 1's --------")
for player in playerRanks["1"]:
	print("+ --- %s" % player)
print("\n\n----------- 2's --------")
for player in playerRanks["2"]:
	print("+ --- %s" % player)
print("\n\n----------- 3's --------")
for player in playerRanks["3"]:
	print("+ --- %s" % player)
print("\n\n-\n-\n--------- TEAMS ARE ---------\n-\n-")
print("\n\nTeam %s: Player # %s: Team Score: %s" % (teamCaptians["1"], len(teams["1"]), teamScore["1"]))
for player in teams["1"]:
	print("+ --- %s" % player)
print("\n\nTeam %s: Player # %s: Team Score: %s" % (teamCaptians["2"], len(teams["2"]), teamScore["2"]))
for player in teams["2"]:
	print("+ --- %s" % player)
print("\n\nTeam %s: Player # %s: Team Score: %s" % (teamCaptians["3"], len(teams["3"]), teamScore["3"]))
for player in teams["3"]:
	print("+ --- %s" % player)
print("\n\nTeam %s: Player # %s: Team Score: %s" % (teamCaptians["4"], len(teams["4"]), teamScore["4"]))
for player in teams["4"]:
	print("+ --- %s" % player)
print("\n\nTeam %s: Player # %s: Team Score: %s" % (teamCaptians["5"], len(teams["5"]), teamScore["5"]))
for player in teams["5"]:
	print("+ --- %s" % player)
print("\n\nTeam %s: Player # %s: Team Score: %s" % (teamCaptians["6"], len(teams["6"]), teamScore["6"]))
for player in teams["6"]:
	print("+ --- %s" % player)

os.remove("non_protected.csv")
