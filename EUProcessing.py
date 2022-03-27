# %%
import pandas as pd
from Frequencies import Frequencies

# %%
# import data with id and raw text
df = pd.read_csv('EurLex_all.csv', usecols=['CELEX', 'act_raw_text'])

# %%
# instantiate frequencies object and get word frequencies
freqs = Frequencies()

# iterate over all raw_text
for doc in df['act_raw_text']:
    freqs.add_freqs(str(doc))

freq_arr = freqs.get_freq_arr()

# %%
freq_df = pd.DataFrame(freq_arr, columns=['word', 'frequency'])

# %%
freq_df = freq_df.sort_values('frequency', axis='index', ascending=False)
freq_df.head(20)

# %%
freq_df.tail(20)

# %%
freq_df.to_csv('EUFrequencies.csv', index=False)


