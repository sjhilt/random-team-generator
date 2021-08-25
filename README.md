# Random Team Generator
This is used to randomly generate teams based off a ranking system (1-3) for players.

1) Reads in from CSV
2) Adds protected people to the team ID from CSV 
3) Reads in players based on their rankings 
4) Randomly assigns people to a team
5) Keeps track of a 'team' score to ensure one team isn't to loaded
6) Keeps teams to roughly the same size so its not only one team everyone is being placed on.
7) Keeps teams around the same score based on skills placed on the team. 
8) Prints out the information to be assigned as teams. 

# Sample Output 
```Total Number of Players: 51
Max Players Per Team: 8

------ Player Ranks -----
--
--
----------- 1's --------
+ --- Cynthia Robinson
+ --- David Powell
+ --- Steve Diaz
+ --- Chris Collins
+ --- George Allen
+ --- Sarah Russell
+ --- Sean Reed
+ --- Maria Lewis
+ --- Jane Simmons
+ --- Fred Turner
+ --- Samuel Alexander
+ --- Clarence Patterson
+ --- Nicholas Nelson
+ --- Steven Perez
+ --- William Ward


----------- 2's --------
+ --- Jason Coleman
+ --- Mary Wright
+ --- Rebecca Butler
+ --- Doris Hughes
+ --- Robert Rivera
+ --- Joyce Henderson
+ --- Lisa Howard
+ --- Eric Richardson
+ --- Stephen Parker
+ --- Stephanie Morgan
+ --- Teresa Ross
+ --- Diana Hernandez
+ --- Karen Adams


----------- 3's --------
+ --- Julia Martinez
+ --- Carl Garcia


-
-
--------- TEAMS ARE ---------
-
-


Team CAP 1: Player # 9: Team Score: 14
+ --- Bobby Long
+ --- Pamela Baker
+ --- Louise Thomas
+ --- Sarah Russell
+ --- Jason Coleman
+ --- Doris Hughes
+ --- Robert Rivera
+ --- Stephen Parker
+ --- Julia Martinez


Team CAP 2: Player # 8: Team Score: 12
+ --- Christina Perry
+ --- Joseph Morris
+ --- Jack Kelly
+ --- Anne Wood
+ --- Steven Perez
+ --- Rebecca Butler
+ --- Diana Hernandez
+ --- Carl Garcia


Team CAP 3: Player # 9: Team Score: 14
+ --- Martin Bailey
+ --- Albert Mitchell
+ --- Kenneth Jones
+ --- Margaret Lee
+ --- Sean Reed
+ --- Samuel Alexander
+ --- William Ward
+ --- Joyce Henderson
+ --- Eric Richardson


Team CAP 4: Player # 6: Team Score: 8
+ --- Alan Wilson
+ --- Anthony Gray
+ --- Jane Simmons
+ --- Clarence Patterson
+ --- Stephanie Morgan
+ --- Karen Adams


Team CAP 5: Player # 9: Team Score: 10
+ --- Ronald Watson
+ --- Eugene Rodriguez
+ --- Sandra Scott
+ --- Cynthia Robinson
+ --- David Powell
+ --- Steve Diaz
+ --- Chris Collins
+ --- George Allen
+ --- Maria Lewis


Team CAP 6: Player # 8: Team Score: 12
+ --- James Sanders
+ --- Lori Gonzales
+ --- Michelle Lopez
+ --- Fred Turner
+ --- Nicholas Nelson
+ --- Mary Wright
+ --- Lisa Howard
+ --- Teresa Ross
