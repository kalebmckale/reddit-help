"""
Question about Empty Dictionaries

I'm working on a loop and empty dictionaries, I want to do if the dictionary is empty, then do this, elif the dictionary isn't empty do a comparison on an entry in the dictionary if it doesn't match, then do this; else do this. It doesn't seem to be working anyone know how to do that... I'm pulling data from the NHL game api and trying to work on how to calculate a goalie individual saves (so working on what happens when a goalie gets pulled from the game).  
"""


def update_dict(play, home_team, gamepk):
    if play["result"]["event"] == "Shot":
        if play["players"][-1]["playerType"] == "Goalie":
            team_name = play["team"]["name"]
            if team_name == home_team:
                player_id = play["players"][-1]["player"]["id"]
                if any(self.away_saves_dict.values()):
                    home_saves += 1
                    self.away_saves_dict.update(
                        game_id=gamepk,
                        player_id=player_id,
                        saves_made=home_saves,
                    )
                    print(self.away_saves_dict["player_id"])
                elif player_id != self.away_saves_dict["player_id"]:
                    self.away_saves_dict.update(
                        player_id=self.away_saves_dict["pulled_player_id"],
                        saves_made=self.away_saves_dict["pulled_player_saves"],
                    )
                    home_saves = 1
                else:
                    home_saves += 1
                    self.away_saves_dict["saves_made"] = home_saves
