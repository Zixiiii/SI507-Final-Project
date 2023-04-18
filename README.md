# SI507-Final-Project

## Instructions of code:
* You need to change the path of three CSV files to the absolute path of the files on your own device. (players = pd.read_csv(r'*(the path of the whole folder)*/Data/players.csv')
* You can use the function *print_tree* to print out the tree, which can help you see the data structure more clearly.
* After data caching and processing, three datasets needed are prepared:
  * *player.csv*: the name, team, position, basic information of the players
  * *teams.csv*: the conference that a team belongs to
  * *points.csv*: the average points, rebound, assist of the players

## Description of interaction:
The system is an NBA Player Searching System
* Home page: http://127.0.0.1:5000/
* You can select a conference of the player's team, and then choose a position of the player, then select the player's team, and finally click the name of the player to see all the detailed information of this player.
* You can click the *Go back* button in the footer section to go back to the previous page.
* You can click the *Home* button in the footer section to go back to the home page.
* The condition that you have selected is shown on the top in each step.

## Data Structure
The data structure that stores player information is **Tree**
* Layer 1: Tree root(string, All players)
* Layer 2: Conference(string, Western or Eastern Conference)
* Layer 3: Position(string, Guard or Forward)
* Layer 4: Team(string, Team names)
* Layer 5: Player information(dictionary, storing the information of the players)
```
**All players**
   **Western Conference**
     **G**
       **Grizzlies**
         {'PLAYER_NAME': 'Desmond Bane', 'HEIGHT': '6-5', 'WEIGHT': 215, 'COLLEGE': 'TCU', 'COUNTRY': 'USA', 'PTS': 21.6, 'REB': 5.0, 'AST': 4.4}
         {'PLAYER_NAME': 'Dillon Brooks', 'HEIGHT': '6-6', 'WEIGHT': 225, 'COLLEGE': 'Oregon', 'COUNTRY': 'Canada', 'PTS': 14.4, 'REB': 3.3, 'AST': 2.6}
         {'PLAYER_NAME': 'Kennedy Chandler', 'HEIGHT': '5-11', 'WEIGHT': 170, 'COLLEGE': 'Tennessee', 'COUNTRY': 'USA', 'PTS': 2.2, 'REB': 1.0, 'AST': 1.7}
         {'PLAYER_NAME': 'Tyus Jones', 'HEIGHT': '6-2', 'WEIGHT': 196, 'COLLEGE': 'Duke', 'COUNTRY': 'USA', 'PTS': 10.3, 'REB': 2.5, 'AST': 5.2}
         {'PLAYER_NAME': 'Luke Kennard', 'HEIGHT': '6-5', 'WEIGHT': 206, 'COLLEGE': 'Duke', 'COUNTRY': 'USA', 'PTS': 9.1, 'REB': 2.7, 'AST': 1.5}
         {'PLAYER_NAME': 'John Konchar', 'HEIGHT': '6-5', 'WEIGHT': 210, 'COLLEGE': 'Indiana-Purdue Fort Wayne', 'COUNTRY': 'USA', 'PTS': 5.0, 'REB': 4.2, 'AST': 1.3}
         {'PLAYER_NAME': 'Ja Morant', 'HEIGHT': '6-2', 'WEIGHT': 174, 'COLLEGE': 'Murray State', 'COUNTRY': 'USA', 'PTS': 26.4, 'REB': 5.9, 'AST': 8.1}
         {'PLAYER_NAME': 'Vince Williams Jr.', 'HEIGHT': '6-4', 'WEIGHT': 205, 'COLLEGE': 'Virginia Commonwealth', 'COUNTRY': 'USA', 'PTS': 0.9, 'REB': 0.5, 'AST': 0.2}
      ** Jazz**
         {'PLAYER_NAME': 'Ochai Agbaji', 'HEIGHT': '6-5', 'WEIGHT': 215, 'COLLEGE': 'Kansas', 'COUNTRY': 'USA', 'PTS': 7.6, 'REB': 2.1, 'AST': 1.0}
         {'PLAYER_NAME': 'Jordan Clarkson', 'HEIGHT': '6-5', 'WEIGHT': 194, 'COLLEGE': 'Missouri', 'COUNTRY': 'USA', 'PTS': 20.8, 'REB': 4.0, 'AST': 4.4}
         {'PLAYER_NAME': 'Kris Dunn', 'HEIGHT': '6-3', 'WEIGHT': 205, 'COLLEGE': 'Providence', 'COUNTRY': 'USA', 'PTS': 12.3, 'REB': 4.1, 'AST': 5.1}
         {'PLAYER_NAME': 'Talen Horton-Tucker', 'HEIGHT': '6-4', 'WEIGHT': 234, 'COLLEGE': 'Iowa State', 'COUNTRY': 'USA', 'PTS': 10.7, 'REB': 3.2, 'AST': 3.8}
         {'PLAYER_NAME': 'Johnny Juzang', 'HEIGHT': '6-6', 'WEIGHT': 209, 'COLLEGE': 'UCLA', 'COUNTRY': 'USA', 'PTS': 4.8, 'REB': 2.1, 'AST': 0.5}
         {'PLAYER_NAME': 'Collin Sexton', 'HEIGHT': '6-2', 'WEIGHT': 190, 'COLLEGE': 'Alabama', 'COUNTRY': 'USA', 'PTS': 14.3, 'REB': 2.2, 'AST': 2.9}
       ...
     **F**
       ...
   **Western Conference**
     **G**
       ...
     **F**
       ...
```
