
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

class WCHistoricScoresScraper:
  """
  This class is used to scrape the historic scores of the world cup
  """

  def __init__(self, table_class:str, col1_class: str, col2_class: str, col3_class: str) -> None:
    """
    Initialize the class

    Parameters
    ----------
    table_class : str
        The class of the table
    col1_class : str
        The class of the first column (team 1)
    col2_class : str
        The class of the second column (score)
    col3_class : str
        The class of the third column (team 2)
        
    Returns
    -------
    None
    """
    self.table_class = table_class
    self.col1_class = col1_class
    self.col2_class = col2_class
    self.col3_class = col3_class
    
    self.fStringWebpage = f'https://en.wikipedia.org/wiki/<year>_FIFA_World_Cup'

  def getWebpage(self, year: int) -> str:
    """
    This method is used to get the webpage of the year
    """
    return self.fStringWebpage.replace('<year>', str(year))

  def getSoup(self, year: int) -> BeautifulSoup:
    """
    This method is used to get the soup of the year

    Parameters
    ----------
    year: int
      The year to get the soup from

    Returns
    -------
    BeautifulSoup
      The soup of the year :D
    """
    return BeautifulSoup(requests.get(self.getWebpage(year)).text, 'html.parser')

  def getTables(self, year: int) -> BeautifulSoup:
    """
    This method is used to get the table of the year

    Parameters
    ----------
    year: int
      The year to get the tables from

    Returns
    -------
    BeautifulSoupTables
      The table of the year
    """
    return self.getSoup(year).find_all('table', class_=self.table_class)

  def getTableAsDataframe(self, year: int) -> pd.DataFrame:
    """
    This method is used to convert the tables to a dataframe

    Parameters
    ----------
    year: int
      The year to get the dataframe from

    Returns
    -------
    pd.DataFrame
      The dataframe of the year
    """
    tables = self.getTables(year)
    data = []
    for table in tables:
      col1 = table.find('th', class_=self.col1_class).get_text()
      col2 = table.find('th', class_=self.col2_class).get_text()
      col3 = table.find('th', class_=self.col3_class).get_text()
      data.append({'col1': col1, 'col2': col2, 'col3': col3, 'year': year})
    return cleanDataframe(pd.DataFrame(data))

  def getAllData(self, years: list) -> pd.DataFrame:
    """
    This method is used to get all the dataframes of the years

    Parameters
    ----------
    years: list
      The list of years to get the dataframes from

    Returns
    -------
    pd.DataFrame
      The dataframe of all the years
    """
    dataframes = []
    for year in years:
      dataframes.append(self.getTableAsDataframe(year))
    return pd.concat(dataframes)

def cleanDataframe(df: pd.DataFrame) -> pd.DataFrame:
  """
  This method is used to clean the dataframe

  Parameters
  ----------
  df : pd.DataFrame
    The dataframe to clean

  Returns
  -------
  pd.DataFrame
    The cleaned dataframe
  """
  #find the character before - in col2
  df['score_team1'] = df['col2'].apply(lambda x: extractScore(x, 0))
  df['score_team2'] = df['col2'].apply(lambda x: extractScore(x, 1))

  #rename col1 to team1 and col3 to team2
  df.rename(columns={'col1': 'team1', 'col3': 'team2'}, inplace=True)

  #drop col2
  df.drop(columns=['col2'], inplace=True)

  return df

def extractScore(scoreString: str, scorePos: int) -> int:
  """
  This method is used to extract the score from a string

  Parameters
  ----------
  scoreString : str
    The string containing the score
  scorePos : int
    The position of the score to extract

  Returns
  -------
  int
    The score
  """
  #check if there is a - in the string
  if '–' in scoreString:
    extractScore = scoreString.split('–')[scorePos][0]
    #check if the score is a number
    if extractScore.isnumeric():
      return int(extractScore)
  print(f'Error: {scoreString} is not a valid score')
  return np.nan

class CurrentWCScrapper:
  """
  This class is used to scrape data from the current world cup
  """

  def __init__(self, year:int = 2022, group_order: list[str] = None) -> None:
    """
    Initialize the class

    Parameters
    ----------
    year : int, optional
        The year of the world cup, by default 2022

    Returns
    -------
    None
    """
    if (group_order == None):
      self.group_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    else:
      self.group_order = group_order

    self.year = year

    self.fStringWebpage = f'https://en.wikipedia.org/wiki/<year>_FIFA_World_Cup'

  def getWebpage(self, year: int) -> str:
    """
    This method is used to get the webpage of the year
    """
    return self.fStringWebpage.replace('<year>', str(year))

  def getSoup(self, year: int) -> BeautifulSoup:
    """
    This method is used to get the soup of the year

    Parameters
    ----------
    year: int
      The year to get the soup from

    Returns
    -------
    BeautifulSoup
      The soup of the year :D
    """
    return BeautifulSoup(requests.get(self.getWebpage(year)).text, 'html.parser')

  def getTables(self, year: int) -> BeautifulSoup:
    """
    This method is used to get the table of the year

    Parameters
    ----------
    year: int
      The year to get the tables from

    Returns
    -------
    BeautifulSoupTables
      The table of the year
    """
    all_matches = self.getSoup(year).find_all('table', class_='wikitable')
    #only keep the tables with the position
    all_matches = [table for table in all_matches if table.find('abbr', text='Pos')]
    return all_matches
  
  def createDictTable(self, year: int) -> dict[pd.DataFrame]:
    """
    This method is used to create a dictionary with the tables of the year

    Parameters
    ----------
    year: int
      The year to get the tables from

    Returns
    -------
    dict[pd.DataFrame]
      The dictionary with the group tables of the year
    """
    all_tables = self.getTables(year)
    assert len(all_tables) == len(self.group_order), 'The number of tables is not equal to the number of groups'

    dict_tables = {}
    for i in range(len(all_tables)):
      try:
        df = pd.read_html(str(all_tables[i]))[0]
      except:
        print(f'Error: table {i} ({self.group_order[i]}) could not be converted to a dataframe')
      #rename the second column to team
      df.rename(columns={df.columns[1]: 'Team'}, inplace=True)
      dict_tables[self.group_order[i]] = df

    return dict_tables




  

  