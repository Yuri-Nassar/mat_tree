import itertools
from collections import defaultdict
from copy import deepcopy

from local.basometro.dashboard.set_level import set_level


class TreeNodeObject:
    """
      A class used to represent a node in a Tree.

      Attributes
      ----------
      TODO

      Methods
      -------
      set_level: Defines the cluster label.
      check_label: Method used to verify cluster aspect label in order to avoid
                   duplicate names in Sankey Diagram.
      sankey: Creates a sankey diagram from class dataset. Sankey diagram is a
              type of flow diagram in which the width of the arrows is
              proportional to the flow rate.
      eda: Exploratory Data Analysis. It generates a plot bar of a given feature of
            a given dataset and a given user.
      eda_corr: Exploratory Data Analysis. It generates a plot of correlation
                matrix of all features of a given dataset and a given user.
      get_similarity_matrix: Creates the distance matrix of the trajectories of
                             a given cluster using the given similarity metric.
      get_entropy: Calculates the entropy value of a given dataset.
      dashboard: Displays the result dashboard.
      show: Shows info about each cluster node.
      graphicTree: Shows info about each cluster node in the tree generated by Digraph
                  plot.
      dashTree: Method that calculates the frequency matrix and the clusters
                generated from the division of data based on a split criteria
                defined in the Tree constructor.

    """

    # Select option in dashboard
    SELECT = 'Select Node'
    ALL = 'ALL'
    HEATMAP = 'HEATMAP'

    # Sankey diagram params
    label = defaultdict(list)
    value = defaultdict(list)
    source = []

    id_dict = defaultdict(list)
    id_list = []

    # Params to label tree nodes
    nodeNum, targetNum = -1, -1
    nodeLabel = defaultdict(list)

    # 1. Dictionary of all nodes dataframes
    # 2. Dictionary of all leaves nodes dataframes
    df_dict = {}
    df_leaves = {}

    ############################################################################
    # Frequency matrix for the initial dataset
    absolute_frequency_matrix = None
    relative = True

    ############################################################################
    temporario = 0
    clusters = 0
    dendrogram_dict = defaultdict(list)

    ############################################################################
    var_dict = {}
    id_iter = itertools.count()

    temp = {}

    def __init__(self, df, par=None):
        """DOC - __init__"""

        self.parent = par
        self.parentName = ''
        self.data = df
        self.left = None
        self.leftChildName = ''
        self.right = None
        self.rightChildName = ''
        self.done = 'No'
        self.freqMatrix = None
        self.variance = None
        self.threshold = None
        self.left_group = {}
        self.right_group = {}

        self.division = ''
        self.thresholdVal = None
        self.maxTrajPerGroup = 50
        self.maxDepth = 8

        if par == None:
            # binary, minVariance, var_red, max_red
            self.split = 'var_red'
        else:
            self.split = par.split

        self.trajList = self.data.tid.unique()
        self.useCol = ['day', 'weather', 'root_type']

        if self.parent is not None:
            self.skipVal = deepcopy(self.parent.skipVal)
        else:
            self.skipVal = []

        if self.parent is None:
            self.depth = 0
        else:
            self.depth = par.depth + 1

        if par is None:
            self.id = f'Lvl {self.depth}'
        else:
            self.id = set_level(self.id_dict, self.depth)
