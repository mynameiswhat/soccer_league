import csv

def extract_info():
	players={}
	with open('soccer_players.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for player in reader:
			players[player['Name']]=player
	return players

	#Works, outputs a dictionary with the name of the players as keys

def identify_experienced_players(players):
	experienced={}
	inexperienced={}
	for player in players:
		info = players[player]
		if info['Soccer Experience']=='YES':
			experienced[player]=info['Guardian Name(s)']
		else:
			inexperienced[player]=info['Guardian Name(s)']
		return experienced, inexperienced
			# Good stuff its working, outputs 2 dicts 
			# for experienced and inexperienced players 
			# with their associated guardians

			'''

			ALTERNATIVE CODE, uses list instead of dict when first 
			reading csv and removes redundant need to define name as a key

			players = []
			for player in reader:
				players.append(player)
			return players

			experienced={}
			inexperienced={}
			for player in players:
				if player['Soccer Experience'] == 'YES':
					experienced[player['Name']]=player['Guardian Name(s)']
				else:
					inexperienced[player['Name']]=player['Guardian Name(s)']

			2nd ALTERNATIVE CODE:
			Using tuples for association between player name and guardian

			experienced=[]
			inexperienced=[]
			for player in players:
				if player['Soccer Experience'] == 'YES':
					experience.append(player['Name'],player['Guardian Name(s)'])
				else:
					inexperience.append(player['Name'],player['Guardian Name(s)'])

					#Add experience as boolean as third element of tuple?

			my_list = []
			for player in players:
				if player['Soccer Experience'] == 'YES':
					my_list.append(player['Name'],player['Guardian Name(s)'], True)
				else:
					my_list.append(player['Name'],player['Guardian Name(s)'], False)

					#Length of different lists give me the number of experienced players and inexperienced players. However, one list means it is easier to iterate.
					#Need to define number of experienced players per team and define a while loop to add them to the team

					GO FOR TWO DIFFERENT LISTS WITH TUPLES TO WORK WITH CODE BELOW

					#Pseudo code

							In Main (define teams as a constant list of lists in main function)

					for team in TEAMS:
						execute team_builder(team, required variables)

							Seperate Function

					def team_builder(team as a list, required number of experienced player, required number of players per team)

					a = required number of experienced players
					b = required number of player per team in general

					while a>number of players on team:
						add players from experienced list
					while b>number of players on team:
						add players from the inexperienced list
			'''


def identify_player_requirements():
	experienced_per_team = len(experienced)/3
	inexperienced_per_team = len(inexperienced_per_team)/3
	required_total = required_experienced + required_inexperienced

	return experienced_per_team, required_total


def build_team(team, experienced, inexperienced, required_experienced, required_total):
	player_list = []
	players_in_team = 0 
	while required_experienced>players_in_team:
		player_list.append(experienced.pop())
		players_in_team += 1
	while required_total>players_in_team:
		player_list.append(inexperienced.pop())
		players_in_team += 1
	TEAMS[team]=player_list

	#Test this with players_in_team = len(player_list) or even use this in while loop if possible, removes unnecessary variable

def build_letters(team, player_and_guardians, practice_time):


def main():
	TEAMS = {
		'Dragons': ,
		'Sharks': ,
		'Raptors': ,
		}
	PRACTICE = {
		'Dragons': '1AM ON TUESTDA',
		'Sharks': .....,
		'Raptors': .....,
		}
	extract_info()
	identify_experienced_player(players)
	identify_player_requirements(experienced, inexperienced)
	for team in TEAMS:
		build_team(team, experienced, inexperienced, required_experienced, required_total)
		build_letters(team, TEAMS[team], PRACTICE[team])

		#Store practice time in list? Otherwise iteration probably doesn't work, keep in mind that dictionary order is random!!!!!!
		#Implemented alternative to use another constant dicionary for the practice times, seems like it would work


	build_letters(team, player_and_guardians, practice_time)



if __name__ == '__main__':
	main()