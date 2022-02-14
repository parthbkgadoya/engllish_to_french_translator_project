import pandas as pd
import re

# # load the data
df_english = pd.read_csv('small_vocab_en.csv', sep = '/t', names = ['english'])
df_french = pd.read_csv('small_vocab_fr.csv', sep = '/t', names = ['french'])

# function to remove punctuations
def remove_punc(x):
    return re.sub('[!#?,.:";]', '', x)

df = pd.concat([df_english, df_french], axis = 1)

df['french'] = df['french'].apply(remove_punc)
df['english'] = df['english'].apply(remove_punc)

# df = pd.read_csv("english_to_french_full_data_small_cleaned.csv")
df = df.reset_index()
df = df.assign(translation = df.apply(lambda x: {'en': x.english, 'fr': x.french},axis=1))

df.rename({'index':'id'}, axis=1, inplace=True)
dfnew = df.drop(['english', 'french'], axis=1)
dfnew.to_json("small_data_DS_format_v2.json",orient='records', lines=True)