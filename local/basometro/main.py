import pandas as pd

from local.basometro.dashboard.TreeNodeObject import TreeNodeObject
from local.basometro.dashboard.dashtree import dashtree
from local.basometro.dashboard.graphic_tree import generate_graphic_tree

df = pd.read_csv("../../dataset/basometro/2022-09-28_6M_specific.csv")
# df_muitas = pd.read_csv(
#     "https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/muitas_top_10.csv")
# df_msm = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/msm_top_10.csv")
df_edr = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/edr_top_10.csv")
df_lcss = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/lcss_top_10.csv")

self = TreeNodeObject(df=df)
# eda_dashboard('ALL', df, self)
dashtree(self, df)

generate_graphic_tree(self, 'path')

# dataset_exploration(5, df)

# Silhouette score e os índices
# de Calinski-Harabasz e Davies-Bouldin
