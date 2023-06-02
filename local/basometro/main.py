import pandas as pd
import os

from local.basometro.dashboard.TreeNodeObject import TreeNodeObject
from local.basometro.dashboard.dashtree import dashtree
from local.basometro.dashboard.graphic_tree import generate_graphic_tree
from local.basometro.methods.sankey import sankey

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

df = pd.read_csv("../../dataset/basometro/2022-09-28_6M_specific.csv")
# df_muitas = pd.read_csv(
#     "https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/muitas_top_10.csv")
# df_msm = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/msm_top_10.csv")
# df_edr = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/edr_top_10.csv")
# df_lcss = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/lcss_top_10.csv")
#parametros
# split = binary, minVariance, var_red, max_red
split = 'var_red'
# max_traj_per_group
max_traj_per_group = 50
# max_depth = Tamanho de nós até chegar na folha
max_depth = 3
self = TreeNodeObject(df=df, split=split, max_traj_per_group=max_traj_per_group,  max_depth=max_depth)
# eda_dashboard('ALL', df, self)
dashtree(self, df)

# generate_graphic_tree(self, 'path')

sankey(self, 'C:\\Users\\P01062\\PycharmProjects\\mat_tree\\images\\sankey\\')

#dataset_exploration(5, df)

## Silhouette score e os índices
## de Calinski-Harabasz e Davies-Bouldin
