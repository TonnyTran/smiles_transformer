import numpy as np
import pandas as pd
from tqdm import tqdm
from utils import split
from sklearn.model_selection import train_test_split
from build_vocab import build_vocab


def build_corpus(in_path, out_path): # input file: .csv, output file: .txt
    smiles = pd.read_csv(in_path)['canonical_smiles'].values
    with open(out_path, 'a') as f:
        for sm in tqdm(smiles):
            f.write(split(sm)+'\n')
    print('Built a corpus file!')

df = pd.read_table('../data/chembl_24_chemreps.txt')
L = len(df)
print(L)

smiles = df['canonical_smiles'].values

to_drop = []
for i,sm in enumerate(smiles):
    if len(sm)>100:
        to_drop.append(i)
print(len(to_drop))

df_dropped = df.drop(to_drop)
df_dropped = df_dropped.drop(['standard_inchi', 'standard_inchi_key'], axis=1)
L = len(df_dropped)
print(L)

smiles = df_dropped['canonical_smiles'].values
rands = np.random.choice(L, L, replace=False)
test_size = 10000

train, test = train_test_split(df_dropped, test_size=test_size)
test.head()
print(len(test))
print(len(train))

# save train, test and whole dataset
test.to_csv('data/test_24.csv')
train.to_csv('data/train_24.csv')
df_dropped.to_csv('data/chembl_24.csv')

build_corpus(in_path='data/chembl_24.csv', out_path='data/chembl24_corpus.txt')
build_vocab(corpus_path='data/chembl24_corpus.txt', out_path='data/vocab.pkl')

