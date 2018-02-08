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

    with open("teams.txt", 'w') as txtfile:
        for i in range(len(teams)):
            txtfile.write(teams[i]['Team'] + '\n')
            txtfile.write("{}, {}, {}\n".format(teams[i]['Players'][0], teams[i]['Players'][2], teams[i]['Players'][3]))
