import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player',
                 'count', 'pitches', 'event', 'game_id', 'year']
