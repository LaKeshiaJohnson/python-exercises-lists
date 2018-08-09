players = []

add_players = raw_input("Would you like to add a player to the list? (Yes/No) ")

while add_players.lower() == 'yes':
	name = raw_input("Enter the name of the player to add to the team: ")
	players.append(name)
	add_players = raw_input("Would you like to add another player? (Yes/No) ")


player_number = 1
for player in players:
	print("Player {}: {}".format(player_number, player))
	player_number += 1

goalie = raw_input("Please select the goalkeeper by selecting the player number. (1-{}) ".format(len(players)))

goalie = int(goalie)

print("Great!!! The goalkeeper for the game will be {}.".format(players[goalie - 1]))
