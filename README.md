# SI507-Final-Project

## Instructions of code:
* You need to change the path of three CSV files to the absolute path of the files on your own device. (players = pd.read_csv(r'*(the path of the whole folder)*/Data/players.csv')
* You can use the function *print_tree* to print out the tree, which can help you see the data structure more clearly.
* After data caching and processing, three datasets needed are prepared:
  * player.csv: the name, team, position, basic information of the players
  * teams.csv: the conference that a team belongs to
  * points: the average points, rebound, assist of the players

## Description of interaction:
The system is an NBA Player Searching System
* Home page: http://127.0.0.1:5000/
* You can select a conference of the player's team, and then choose a position of the player, then select the player's team, and finally click the name of the player to see all the detailed information of this player.
* You can click the *Go back* button in the footer section to go back to the previous page.
* You can click the *Home* button in the footer section to go back to the home page.
* The condition that you have selected is shown on the top in each step.
