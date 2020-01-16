import pandas as pd
import re
from statsmodels.stats.proportion import proportions_ztest

print("Is poetic language more colorful than regular language? We'll take all of poetryfoundation.org's poems")
print("and counted how many words were color-related. Then we'll test this against normal english vocabulary. \n")
print("First, calculating percentage of poetry words which are 'colorful'...\n")

df = pd.read_csv('kaggle_poem_dataset.csv')
df['Content'] = df['Content'].astype(str)

text = ''
for i in range(len(df.index)):
    text += df.iloc[i,4] + ' '
text = re.sub('\\n|\\t',' ',text)
text = re.sub('\\|\\xa0','',text)
text = text.lower()

colors = re.findall('white|yellow|blue|red|green|black|brown|azure|ivory|teal|silver|purple|navy|gray|orange|maroon|charcoal|aquamarine|coral|fuchsia|crimson|cyan',text)
words = re.split(' ',text)

print('The percentage of colorful words in poems: '+str(round(len(colors)/len(words)*100,2))+"%.\n")
print("Next, calculating percentage of text message words which are 'colorful'...\n")

df2 = pd.read_csv("spam.csv", encoding = 'latin-1',usecols=[0,1])
df2.columns=['target','text']
df2['text'] = df2['text'].astype(str)

messages = ''
for i in range(len(df2.index)):
    messages += df2.iloc[i,1] + ' '

messages = re.sub('\\n|\\t',' ',messages)
messages = re.sub('\\|\\xa0','',messages)
messages = messages.lower()

colorsM = re.findall('white|yellow|blue|red|green|black|brown|azure|ivory|teal|silver|purple|navy|gray|orange|maroon|charcoal|aquamarine|coral|fuchsia|crimson|cyan',messages)
wordsM = re.split(' ',messages)
print('The percentage of colorful words in messages: '+str(round(len(colorsM)/len(wordsM)*100,2))+"%.")

stat, pval = proportions_ztest([len(colors),len(colorsM)], [len(words),len(wordsM)])
print("If we calculate a simple two sample z-test for proportions, we find..")
print("z = "+str(round(stat,2))+", and the p-value = "+str(pval)+".\n")
print("And so we see that poetic language is, in fact, far more colorful than normal texting language.")
