import pandas as pd
from flask import Flask,render_template
import requests
app = Flask(__name__)

'''
1. Data caching and processing

The data caching code and the JSON file accessed is in folder "Caching". 

After data caching and processing, three datasets needed are prepared:
* player.csv: the name, team, position, basic information of the players
* teams.csv: the conference that a team belongs to
* points: the average points, rebound, assist of the players
'''
players = pd.read_csv(r'/Users/zixizhou/Desktop/SI507/Assignment/Project/Final Project/Project code/Data/players.csv')
players.drop(['Unnamed: 0'],axis=1,inplace=True)
teams = pd.read_csv(r'/Users/zixizhou/Desktop/SI507/Assignment/Project/Final Project/Project code/Data/teams.csv')
teams.drop(['Unnamed: 0'],axis=1,inplace=True)
points = pd.read_csv(r'/Users/zixizhou/Desktop/SI507/Assignment/Project/Final Project/Project code/Data/points.csv')
points.drop(['Unnamed: 0'],axis=1,inplace=True)
players['POSITION'] = players['POSITION'].replace(['G-F','F-C','C-F','F-G'], ['G','F','C','F'])
players['POSITION'] = players['POSITION'].replace(['C'], ['F'])
players_and_teams = players.merge(teams,left_on='TEAM_NAME',right_on='TEAM_NAME')
players_and_teams_and_points = players_and_teams.merge(points[['PERSON_ID','PTS','REB','AST']],left_on='PERSON_ID',right_on='PERSON_ID')
players_and_teams_and_points = players_and_teams_and_points.rename(columns={"Conference": "CONFERENCE"})
players_and_teams_and_points['PLAYER_NAME'] = players_and_teams_and_points['PLAYER_FIRST_NAME'] + ' ' + players_and_teams_and_points['PLAYER_LAST_NAME']
whole = players_and_teams_and_points[['PLAYER_NAME','TEAM_CITY','TEAM_NAME','TEAM_ABBREVIATION','CONFERENCE','POSITION','HEIGHT','WEIGHT','COLLEGE','COUNTRY','PTS','REB','AST']]

'''
2. Data Structure - Tree
'''
class NonBinTree:

    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))

    def print_node(self):
        return self.val

    def __repr__(self):
        return f"({self.val}): {self.nodes}"
    
def print_tree(player_tree, level=0):
    print("  " * level, player_tree.val)
    for node in player_tree.nodes:
        print_tree(node, level + 1)

def add_team(player_tree,west_or_east,team_list):
    for conference in player_tree.nodes:
        if conference.val == west_or_east:
            for position in conference.nodes:
                for team in team_list:
                    position.add_node(team)

def add_player(players,player_tree):
    for i in range(len(players)):
        for conference in player_tree.nodes:
            if conference.val == players.loc[i,'CONFERENCE']:
                for position in conference.nodes:
                    if position.val == players.loc[i,'POSITION']:
                        for team in position.nodes:
                            if team.val == players.loc[i,'TEAM_NAME']:
                                player_info = {}
                                player_info['PLAYER_NAME'] = players.loc[i,'PLAYER_NAME']
                                player_info['HEIGHT'] = players.loc[i,'HEIGHT']
                                player_info['WEIGHT'] = players.loc[i,'WEIGHT']
                                player_info['COLLEGE'] = players.loc[i,'COLLEGE']
                                player_info['COUNTRY'] = players.loc[i,'COUNTRY']
                                player_info['PTS'] = players.loc[i,'PTS']
                                player_info['REB'] = players.loc[i,'REB']
                                player_info['AST'] = players.loc[i,'AST']
                                team.add_node(player_info)

'''
3. Interaction and Presentation
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conference/<con>')
def Conferences(con):
    for conference in player_tree.nodes:
        if conference.val == con:
            return render_template('conference.html',conference_tree=conference,conference_name=con)

@app.route('/conference/<con>/position/<pos>')
def Positions(con,pos):
    for conference in player_tree.nodes:
        if conference.val == con:
            for position in conference.nodes:
                if position.val == pos:
                    return render_template('position.html',position_tree=position,conference_name=con,position_name=pos)

@app.route('/conference/<con>/position/<pos>/team/<t>')
def Teams(con,pos,t):
    for conference in player_tree.nodes:
        if conference.val == con:
            for position in conference.nodes:
                if position.val == pos:
                    for team in position.nodes:
                        if team.val == t:
                            return render_template('team.html',team_tree=team,conference_name=con,position_name=pos,team_name=t)

@app.route('/conference/<con>/position/<pos>/team/<t>/player/<p>')
def Players(con,pos,t,p):
    for conference in player_tree.nodes:
        if conference.val == con:
            for position in conference.nodes:
                if position.val == pos:
                    for team in position.nodes:
                        if team.val == t:
                            for player in team.nodes:
                                if player.val['PLAYER_NAME'] == p:
                                    return render_template('player.html',player_dict=player.val,conference_name=con,position_name=pos,team_name=t,player_name=p)

         
if __name__ == '__main__': 
    player_tree = NonBinTree('All players')

    player_tree.add_node('Western Conference')
    player_tree.add_node('Eastern Conference')
    for node in player_tree.nodes:  
        node.add_node('G')
        node.add_node('F')
    Western_team_list = teams[teams['Conference'] == 'Western Conference'].TEAM_NAME
    Eastern_team_list = teams[teams['Conference'] == 'Eastern Conference'].TEAM_NAME
    add_team(player_tree,'Western Conference',Western_team_list)
    add_team(player_tree,'Eastern Conference',Eastern_team_list)
    add_player(whole,player_tree)
    # print_tree(player_tree)
    
    print('starting Flask app', app.name)  
    app.run(debug=True)