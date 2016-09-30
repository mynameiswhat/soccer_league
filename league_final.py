import csv

def extract_info():

	#Outputs a lit with the player information extracted from the csv file

    players=[]
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for player in reader:
            players.append(player)
    return players


def identify_experienced_players(players):

	#Creates 2 lists of tuples seperating them into experienced and inexperienced players with their name and guardian's name

    experienced=[]
    inexperienced=[]
    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced.append((player['Name'],player['Guardian Name(s)']))
        else:
            inexperienced.append((player['Name'],player['Guardian Name(s)']))
    return experienced, inexperienced
            

def identify_player_requirements(experienced, inexperienced):

	#Identifies number of experienced and inexperienced player per team and rounds to nearest integer

    required_experienced = round(len(experienced)/3)
    required_inexperienced = round(len(inexperienced)/3)
    required_total = required_experienced + required_inexperienced

    return required_experienced, required_total


def build_team(team, experienced, inexperienced, required_experienced, required_total):

	#Builds teams based on requirements, populates TEAMS dictionary with players
    #The tries in this function anticipate a case where the number of players required may 
    #be rounded, leading to pop an inexistent list object and an IndexError

    player_list = []
    players_in_team = 0 
    try:
      while required_experienced>players_in_team:
          player_list.append(experienced.pop())
          players_in_team += 1
    except IndexError:
      pass
    try:
      while required_total>players_in_team:
          player_list.append(inexperienced.pop())
          players_in_team += 1
    except IndexError:
      pass
    TEAMS[team]=player_list


def build_letters(team, player_and_guardians, practice_time):

	#Builds letters

    for player in player_and_guardians:
        with open(player[0].lower().replace(' ', '_')+'.txt', 'w') as file:
            file.write(
                'Dear {}, \n\n'
                'Your child {} is pretty badass and has been recruited in the {}.\n'
                'Congratulations! \n\n'
                'First practice is at: {}.\n\n'
                'All the best,\n'
                'Quentin Grunenwald'.format(player[1], player[0], team, practice_time)
                )

            
def main():
    players = extract_info()
    experienced, inexperienced = identify_experienced_players(players)
    required_experienced, required_total = identify_player_requirements(experienced, inexperienced)
    for team in TEAMS:
        build_team(team, experienced, inexperienced, required_experienced, required_total)
        build_letters(team, TEAMS[team], PRACTICE[team])


if __name__ == '__main__':
  TEAMS = {
        'Dragons':'', 
        'Sharks':'',
        'Raptors':'',
        }
  PRACTICE = {
        'Dragons': 'March 17, 1pm',
        'Sharks': 'March 17, 3pm',
        'Raptors': 'March 18, 1pm',
        }
  main()