
from scraper import WCHistoricScoresScraper
from analyser import WCAnalyser

def intro() -> None:
  print("Welcome to the World Cup Analyser!")
  print("==================================")
  print("This Program will analyse historic World Cup data and provide you with the following information:")
  print("1. Statistics for a team")
  print("2. Predictions for a match")
  print("3. Predictions for the winner of the World Cup")

class WorldCupAnalyer():

  valid_years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018] 

  def __init__(self):
    print("Initializing World Cup Analyser...\n")
    data_scraper = WCHistoricScoresScraper('fevent', 'fhome', 'fscore', 'faway')
    intro()
    print("\nLets start by entering the years you would like to analyse.")
    print("Per default, all years from 1930 to 2018 are available.")
    print("Would you like to use all years? (y/n)")
    use_all_years = input()
    if use_all_years == 'y':
      self.years = self.valid_years
    else:
      self.years = self.get_years()
    print("Getting data for the following years: ", self.years)
    raw_data = data_scraper.getAllData(self.years)
    print("Initializing analyser...")
    self.analyser = WCAnalyser(raw_data)
    print("Great! Now we can start analysing the data.")

  def get_years(self) -> list:
    years = []
    while True:
      year = input("Enter a year (or type 'done' to finish): ")
      if year == 'done':
        break
      elif int(year) not in self.valid_years:
        print("Invalid year!")
      else:
        years.append(int(year))
    return years

  def program_loop(self):
    while True:
      print("\nWhat would you like to do?")
      print("1. Get statistics for a team")
      print("2. Get predictions for a match")
      print("3. Get predictions for the winner of the World Cup")
      print("4. Exit")
      choice = input()
      if choice == '1':
        self.get_team_stats()
      elif choice == '2':
        self.get_match_predictions()
      elif choice == '3':
        print("Not implemented yet :(")
      elif choice == '4':
        break
      else:
        print("Invalid choice!")

  def get_team_stats(self):
    print("Enter the name of the team you would like to get the statistics for.")
    team = input()
    self.analyser.print_team_statistics(team)

  def get_match_predictions(self):
    print("Enter the name of the first team.")
    team1 = input()
    print("Enter the name of the second team.")
    team2 = input()
    self.analyser.predict_outcome(team1, team2)



if __name__ == "__main__":
  WorldCupAnalyer().program_loop()