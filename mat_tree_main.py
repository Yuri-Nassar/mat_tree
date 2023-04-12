import pandas as pd

from scripts.algorithm.TreeNodeObject import TreeNodeObject
from scripts.algorithm.dashtree import dashtree
from scripts.algorithm.graphic_tree import generate_graphic_tree
from scripts.utils import get_dataset

# df = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/foursquare.csv")

df = get_dataset('fsny_10')
## print(df.head())

### var: exclude_aspects
### A list of aspects to exclude for clustering or a empty list to use all aspects.
### e.g.: exclude_aspects = [] # use all aspects
###       exclude_aspects = ['day', 'weather', 'root_type'] # exclude aspects for fsny
###       exclude_aspects = ['data', 'idVotacao', 'parlamentar'] # exclude aspects for basometro
exclude_aspects = ['day', 'weather', 'root_type']

self = TreeNodeObject(df=df)
# # eda_dashboard('ALL', df, self)
dashtree(self, df, exclude_aspects)

# generate_graphic_tree(self, 'path')