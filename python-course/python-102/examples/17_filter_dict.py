matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

print(matches)
print("-"*10)

no_draw_results_list = list(
    filter(lambda item: item['home_team_result'] != "Draw", matches))
print(no_draw_results_list)

home_team_winner_list = list(
    filter(lambda item: item["home_team_result"] == "Win", no_draw_results_list))
print(home_team_winner_list)

away_team_winner_list = list(
    filter(lambda item: item["home_team_result"] == "Lose", no_draw_results_list))
print(away_team_winner_list)

home_team_winner = list(
    map(lambda item: item["home_team"], home_team_winner_list))
print(home_team_winner)

away_team_winner = list(
    map(lambda item: item["away_team"], away_team_winner_list))
print(away_team_winner)
