import pandas as pd
import os

from local.basometro.dashboard.TreeNodeObject import TreeNodeObject
from local.basometro.dashboard.dashtree import dashtree
from local.basometro.dashboard.graphic_tree import generate_graphic_tree
from local.basometro.methods.sankey import sankey

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

df = pd.read_csv("../../dataset/basometro/basometro.csv", delimiter=';', encoding='iso-8859-1')
# df_muitas = pd.read_csv(
#     "https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/muitas_top_10.csv")
# df_msm = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/msm_top_10.csv")
# df_edr = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/edr_top_10.csv")
# df_lcss = pd.read_csv("https://raw.githubusercontent.com/Yuri-Nassar/mat_tree/master/dataset/top_10/lcss_top_10.csv")
#parametros
# split = binary, minVariance, var_red, max_red
# split = 'var_red'
# split = 'binary'
# split = 'minVariance'
# split = 'max_red'
# max_traj_per_group
splits = ['binary', 'minVariance', 'var_red']
max_traj_per_group = 50
# max_depth = Tamanho de nós até chegar na folha
# max_depth = 8
max_depths = [3, 4, 5, 6, 7, 8]
out_aspects = ['data', 'idVotacao', 'parlamentar', 'UF']
for max_depth in max_depths:
    for split in splits:
        self = TreeNodeObject(df=df, split=split, max_traj_per_group=max_traj_per_group,  max_depth=max_depth)
        dashtree(self, df, out_aspects)
        generate_graphic_tree(self, 'C:\\Users\\P01062\\PycharmProjects\\mat_tree\\images\\trees')
        sankey(self, 'C:\\Users\\P01062\\PycharmProjects\\mat_tree\\images\\sankey\\')

## Silhouette score e os índices
## de Calinski-Harabasz e Davies-Bouldin
