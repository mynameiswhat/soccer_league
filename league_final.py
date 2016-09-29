import csv

def extract_info():
    players={}
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for player in reader:
            players[player['Name']]=player
    return players

    #Outputs a dictionary with the name of the players as keys and information from the csv file as values

def identify_experienced_players(players):
    experienced=[]
    inexperienced=[]
    for player in players:
        info = players[player]
        if info['Soccer Experience'] == 'YES':
            experienced.append((info['Name'],info['Guardian Name(s)']))
        else:
            inexperienced.append((info['Name'],info['Guardian Name(s)']))
    return experienced, inexperienced
            
    #Creates 2 lists of tuples seperating them into experienced and inexperienced players with their name and guardian's name

def identify_player_requirements(experienced, inexperienced):
    required_experienced = round(len(experienced)/3)
    required_inexperienced = round(len(inexperienced)/3)
    required_total = required_experienced + required_inexperienced

    return required_experienced, required_total

    #Look at rounding the number of players required
    #Identifies number of experienced and inexperienced player per team and rounds to nearest integer

def build_team(team, experienced, inexperienced, required_experienced, required_total):
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

    #Test this with players_in_team = len(player_list) or even use this in while loop if possible, removes unnecessary variable
    #Builds teams based on requirements, populates TEAMS dictionary with players
    #The tries in this function anticipate a case where the number of players required may be rounded, leading to pop an inexistent list object and an IndexError


def build_letters(team, player_and_guardians, practice_time):
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

            #Builds letters
            
def main():
    players = extract_info()
    experienced, inexperienced = identify_experienced_players(players)
    required_experienced, required_total = identify_player_requirements(experienced, inexperienced)
    for team in TEAMS:
        build_team(team, experienced, inexperienced, required_experienced, required_total)
        build_letters(team, TEAMS[team], PRACTICE[team])

        #Implemented alternative to use another constant dicionary for the practice times, seems like it would work


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