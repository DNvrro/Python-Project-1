import csv

if __name__ == "__main__":
    #lists containing experienced players & noobs
    exp_players = []
    noobs = []

    #list of  teams


    teams = [
        {'Team': "Dragons", 'Players': []},
        {'Team': "Sharks", 'Players': []},
        {'Team': "Raptors", 'Players': []}
    ]



    #Open the csv file
    with open("soccer_players.csv") as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        roster = list(player_reader)

        #sort experienced players from noobs
        for player in roster:
            if player["Soccer Experience"] == 'YES':
                exp_players.append(player)
            else:
                noobs.append(player)
        #assign experienced players to each team
        for player in exp_players:
            if len(teams[0]['Players']) < 3:
                teams[0]['Players'].append(player)
            elif len(teams[1]['Players']) < 3:
                teams[1]['Players'].append(player)
            else:
                teams[2]['Players'].append(player)
        #assign noobs to each team
        for player in noobs:
            if len(teams[0]['Players']) < 6:
                teams[0]['Players'].append(player)
            elif len(teams[1]['Players']) < 6:
                teams[1]['Players'].append(player)
            else:
                teams[2]['Players'].append(player)


    #this function enables the teams to be extracted from
    #their lists and written to the text file in the specified
    #format
    def teams_text_writer(player_list):
        with open("teams.txt", 'a') as file:
            file.write(player_list["Team"] + '\n')
            for player in player_list['Players']:
                player_string = ''
                player_string += player['Name'] + ', '
                player_string += player['Soccer Experience'] + ', '
                player_string += player['Guardian Name(s)']
                file.write(player_string + '\n')
                file.write('\n')

    teams_text_writer(teams[0])
    teams_text_writer(teams[1])
    teams_text_writer(teams[2])
