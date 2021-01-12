import os
import glob
import pandas as pd

# list all filenames ending with '.EVE' extension in the 'games' folder of the current working directory
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# sort the files by name
game_files.sort()

# column headers to be passed in to pd.read_csv function
# header_list = ['type', 'multi2', 'multi3',
#                'multi4', 'multi5', 'multi6', 'event']

# empty list where dataframes will be appended to
game_frames = []


# iterate through filenames and read into dataframes, append into the game_frames list above
for game_file in game_files:

    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3',
                                               'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)


# concat gameframes
games = pd.concat(game_frames)

# clean up data  - some entries in multi 5 column have '??' - replace with empty string
games.loc[games['multi5'] == '??', 'multi5'] = ''

# extract identifiers
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

# forward fill ids
identifiers = identifiers.fillna(method='ffill')

# assign new names for columns in identifier dataframe
identifiers.columns = ['game_id', 'year']

# concatenate identifiers dataframe to the games dataframe
games = pd.concat([games, identifiers], axis=1, sort=False)

# fill in all NaN values with ' ' (single space empty string)
games = games.fillna(' ')

# make type column categorical to save memory
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])


print(games.head())
