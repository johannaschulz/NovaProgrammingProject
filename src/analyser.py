import pandas as pd
from scipy.stats import poisson

def create_master_dataframe(data: pd.DataFrame) -> pd.DataFrame:
  """Create a master dataframe from the raw data.
  Args:
    data (pd.DataFrame): The raw data.
  Returns:
    pd.DataFrame: The master dataframe.
  """
  #make sure there are no empty values
  data['team1'] = data['team1'].str.strip()
  data['team2'] = data['team2'].str.strip()
  #calculate all goals
  data['total_goals'] = data['score_team1'] + data['score_team2']

  return data

def create_teams_dataframe(data: pd.DataFrame) -> pd.DataFrame:
  """
  Create a dataframe with all teams and their statistics.
  
  Parameters
  ----------
  data : pd.DataFrame
    The master dataframe.
  
  Returns
  -------
  pd.DataFrame
    The dataframe with all teams and their statistics.
  """

  data_team1 = data[['team1', 'score_team1', 'score_team2', 'total_goals','year']].rename(columns={'team1': 'team', 'score_team1': 'score', 'score_team2': 'opponent_score'})
  data_team2 = data[['team2', 'score_team2', 'score_team1', 'total_goals','year']].rename(columns={'team2': 'team', 'score_team2': 'score', 'score_team1': 'opponent_score'})
  return pd.concat([data_team1, data_team2])



class WCAnalyser:

  def __init__(self, data: pd.DataFrame):
    self.rawdata = data

    self.master_data = create_master_dataframe(self.rawdata)
    self.teams_data = create_teams_dataframe(self.master_data)

    self.strength = self.teams_data[['team','score','opponent_score']].groupby(['team']).mean()

  def print_team_statistics(self, team: str) -> None:
    """Get the statistics for a team.
    Args:
      team (str): The team name.
    Returns:
      pd.DataFrame: The statistics for the team.
    """
    if team not in self.teams_data['team'].unique():
      print(f"Team {team} not found!")
      return

    total_games_played = self.teams_data[self.teams_data['team'] == team].shape[0]
    total_goals_scored = self.teams_data[self.teams_data['team'] == team]['score'].sum()
    total_goals_conceded = self.teams_data[self.teams_data['team'] == team]['opponent_score'].sum()
    total_wins = self.teams_data[(self.teams_data['team'] == team) & (self.teams_data['score'] > self.teams_data['opponent_score'])].shape[0]
    total_losses = self.teams_data[(self.teams_data['team'] == team) & (self.teams_data['score'] < self.teams_data['opponent_score'])].shape[0]
    total_draws = self.teams_data[(self.teams_data['team'] == team) & (self.teams_data['score'] == self.teams_data['opponent_score'])].shape[0]
    if(total_losses == 0):
      win_loss_ratio = total_wins
    else:
      win_loss_ratio = total_wins / total_losses
    average_goals_scored = self.teams_data[self.teams_data['team'] == team]['score'].mean()
    average_goals_conceded = self.teams_data[self.teams_data['team'] == team]['opponent_score'].mean()
    average_goals_per_game = self.teams_data[self.teams_data['team'] == team]['total_goals'].mean()
    average_goals_diff = average_goals_scored - average_goals_conceded
    average_score = self.teams_data[self.teams_data['team'] == team]['score'].sum() / self.teams_data[self.teams_data['team'] == team].shape[0]
    number_of_world_cups = self.teams_data[self.teams_data['team'] == team]['year'].unique().shape[0]
    print(f"\n\nStatistics for {team}:")
    print("=====================================")
    print(f"Total Games Played: {total_games_played}")
    print(f"Total Goals Scored: {total_goals_scored}")
    print(f"Total Goals Conceded: {total_goals_conceded}")
    print(f"Total Wins: {total_wins}")
    print(f"Total Losses: {total_losses}")
    print(f"Total Draws: {total_draws}")
    print(f"Win/Loss Ratio: {win_loss_ratio}")
    print(f"Average Goals Scored: {average_goals_scored}")
    print(f"Average Goals Conceded: {average_goals_conceded}")
    print(f"Average Goals per Game: {average_goals_per_game}")
    print(f"Average Goals Difference: {average_goals_diff}")
    print(f"Average Score: {average_score}")
    print(f"Number of World Cups: {number_of_world_cups}")
    print("=====================================")

  def get_team_strength(self, team: str) -> float:
    """Get the strength of a team.
    Args:
      team (str): The team name.
    Returns:
      float: The strength of the team.
    """
    if team not in self.strength.index:
      print(f"Team {team} not found!")
      return

    return self.strength.loc[team]

  def predict_outcome(self,team1:str,team2:str) -> tuple:
    if team1 in self.strength.index and team2 in self.strength.index:
        # goals_scored * goals_conceded
        lamb_home = self.strength.at[team1,'score'] * self.strength.at[team2,'opponent_score']
        lamb_away = self.strength.at[team2,'score'] * self.strength.at[team1,'opponent_score']
        prob_home, prob_away, prob_draw = 0, 0, 0
        for x in range(0,11): #number of goals home team
            for y in range(0, 11): #number of goals away team
                p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_home += p
                else:
                    prob_away += p
        
        points_home = 3 * prob_home + prob_draw
        points_away = 3 * prob_away + prob_draw
        print(f"Probability of {team1} winning: {prob_home}")
        print(f"Probability of {team2} winning: {prob_away}")
        return (points_home, points_away)
    else:
        print(f"Team {team1} or {team2} not found!")
        return (0, 0)

  




    

