# Project Class "Introduction to Programming", Wintersemester 2022 Nova SBE

As part of the course "Introduction to Programming" we learned the basics of programming in Python. 
This repository holds the final project of the course.
We were asked to come up with a project idea and implement it in Python.

## Project Idea
With the World Cup 2022 in Qatar beeing a big topic in the moment we write this, we wanted to create a tool that allows to predict the winner.
Instead of using fancy machine learning algorithms, we decided to use a simple algorithm in form of a poisson distribution to calculate the probability of a team winning a match. To do so we used the world cup data from all matches played starting from 1930.

## Project Structure
The project is structured as follows:
```
.
├── README.md
├── notebooks
│   ├── Web_Crawler_Worldcup_data.ipynb
│   ├── World_Cup_Data_Analysis.ipynb
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── analyser.py
│   ├── scraper.py
```

## Installation
This project uses python 3.9.13. The recommended way to install it is using [pyenv](https://).

To install the project, clone the repository and install the requirements using pip:

```bash
git clone
cd
pip install -r requirements.txt
```

## Run the project
To run the project, run the following command:

```bash
python src/main.py
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
