# Project Class "Introduction to Programming", Wintersemester 2022 Nova SBE

## Project Description
The aim of this project is to implement a prediction algorithm to predict the winner of the world cup 2022 using python.

Class: Introduction to Programming
Team Members: Johanna Schulz, Daniel Weiss, 


### Description of world cup prediction

The prediction algorithm is based data of historic FIFA world cup data. Therefore, the prediction is based on the 21 game results between 1930 and 2018. The data is provided by the FIFA website. The data is stored in a csv file. The data is structured as follows:

We use information about whether the team played at their home or away and how many scores they achieved. 

Because not all teams played the same number of games in the 21 FIFA worldcups, we decided to use the average of the scores of the teams.

#### The prediction algorithm is based on the following assumptions:
1. The probability of winning a game is conditional on the number of goals scored by the team in a world cup game in the past years. There is no information used about recent players or the current form of the teams.
2. 


We will only make a prediction (probability based) about the particular winner for the FIFA worldcup 2022 in Qatar. No predictions about the other games will be made or about the number of goals scored by the teams.




## Project Structure
The project is structured as follows:

```
.
├── README.md
├── data
│   ├── 2018.csv
│   ├── 2018.xlsx
│   ├── 2022.csv
│   ├── 2022.xlsx
│   ├── 2026.csv
│   ├── 2026.xlsx
├── notebooks
│   ├── 2018.ipynb
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
```

## Installation
This project uses python 3.9.13. The recommended way to install it is using [pyenv](https://).

To install the project, clone the repository and install the requirements using pip:

```bash
git clone
cd
pip install -r requirements.txt
```

### Packages used
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [sklearn](https://scikit-learn.org/stable/)
- [plotly](https://plotly.com/python/)
- [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/)
- [ipython](https://ipython.org/)
- [jupyter](https://jupyter.org/)
- [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/)
- [jupyter_contrib_nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/)
- [selenium](https://selenium-python.readthedocs.io/)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://requests.readthedocs.io/en/master/)


## Usage
To run the project, run the following command:

```bash
python src/main.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
