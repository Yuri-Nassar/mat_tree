import pandas as pd

from scripts.algorithm.TreeNodeObject import TreeNodeObject
from scripts.algorithm.dashtree import dashtree
from scripts.algorithm.graphic_tree import generate_graphic_tree
from scripts.utils import get_dataset

# df = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/foursquare.csv")

df = get_dataset('fsny_10')

# self = TreeNodeObject(df=df)
# # eda_dashboard('ALL', df, self)
# dashtree(self, df)

# generate_graphic_tree(self, 'path')