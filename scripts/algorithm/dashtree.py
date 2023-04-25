import numpy as np
import pandas as pd

from scripts.algorithm.TreeNodeObject import TreeNodeObject
from scripts.algorithm.check_label import check_label
from scripts.metrics_evaluation.entropy import get_entropy
from scripts.metrics_evaluation.freq_matrix import generate_freq_matrix
from scripts.metrics_evaluation.similarity_matrix import get_similarity_matrix


def dashtree(self, df, exclude_aspects=None):
    """
      Method that calculates the frequency matrix and the clusters generated
      from the division of data based on a split criteria defined in the
      Tree constructor.
    """
    # columns = self.data.drop(['time', 'poi', 'type', 'rating', 'label'], axis=1)
    # dummies = pd.get_dummies(columns, prefix_sep='~')
    # vals = dummies.drop(['tid'], axis=1)
    # self.freqMatrix = pd.pivot_table(dummies, index=['tid'], values=vals.columns, aggfunc=np.sum)
    generate_freq_matrix(self,exclude_aspects)

    if self.relative and self.absolute_frequency_matrix is None:
        self.absolute_frequency_matrix = self.freqMatrix.sum()
        dt = [res for res in self.freqMatrix.mean()]
        self.absolute_frequency_matrix = pd.DataFrame(columns=['mean'], data=dt, index=self.freqMatrix.columns)

    # Condição de parada
    if (self.trajList.size <= 1 or (self.maxTrajPerGroup > 0 and self.trajList.size < self.maxTrajPerGroup) or
            (0 < self.maxDepth <= self.depth)):
        self.parentName = str(self.data.tid.unique().size)
        self.done = 'Yes'
        check_label(self, 'c', self.depth)
        self.df_dict[str(self.id)] = self.freqMatrix
        self.nodeLabel[self.depth].append(self.id)
        print(f"self.done: {self.done}; self.parentName: {self.parentName}; nodeLabel: [self.depth={self.depth}.append(self.id={self.id})]")#degub

        idx = self.df_dict[str(self.id)].index
        df_filter = df[df.tid.isin(idx)]
        self.df_leaves[str(self.id)] = df_filter

        self.temporario += get_entropy(df_filter) * len(df_filter.tid.unique())
        self.clusters += 1

        self.dendrogram_dict[str(self.id)] = []

        return 0

    self.nodeNum += 1
    self.source.append(self.nodeNum)

    minVar = -1

    if self.relative:
        dt = [res for res in self.freqMatrix.sum() / len(df)]
        self.threshold = pd.DataFrame(columns=['mean'], data=dt, index=self.freqMatrix.columns)
    else:
        dt = [res for res in self.freqMatrix.mean()]
        self.threshold = pd.DataFrame(columns=['mean'], data=dt, index=self.freqMatrix.columns)

    self.variance = {}
    left_dict = {}
    right_dict = {}
    feature_list, initial_var, var_red = [], [], []
    reducao = {}
    split_value = {}
    muitas_result = {}
    msm_result = {}

    for col in self.freqMatrix.columns:

        if col in self.skipVal:
            continue

        left, left_idx, right, right_idx = [], [], [], []

        for i, reg in enumerate(self.freqMatrix[col]):
            if reg < self.threshold['mean'][col]:
                left.append(reg)
                left_idx.append(i)
            else:
                right.append(reg)
                right_idx.append(i)

        self.left_group[col] = left
        self.right_group[col] = right

        left_dict[col] = left_idx
        right_dict[col] = right_idx

        self.variance[col] = {
            "initial": self.freqMatrix[col].var(),
            "left": np.var(left),
            "right": np.var(right)
        }

        if self.split == 'var_red':

            save_df = self.freqMatrix.copy()
            save_df.reset_index(drop=True, inplace=True)
            esquerda = save_df.loc[save_df.index.isin(left_dict[col])]
            direita = save_df.loc[save_df.index.isin(right_dict[col])]

            for c in self.freqMatrix.columns:
                initial_variance = self.freqMatrix[c].var()
                variance_reduction = initial_variance - abs((np.var(esquerda[c]) - np.var(direita[c])) / 2)
                reducao[c] = variance_reduction
            split_value[col] = sum(reducao.values()) / len(self.freqMatrix.columns)

        elif self.split == 'muitas':

            traj_left = [t for i, t in enumerate(self.freqMatrix.index.values) if i in left_dict[col]]
            esquerda = self.data.loc[self.data['tid'].isin(traj_left)]
            traj_right = [t for i, t in enumerate(self.freqMatrix.index.values) if i in right_dict[col]]
            direita = self.data.loc[self.data['tid'].isin(traj_right)]

            similarity_mean_node_muitas_esquerda = get_similarity_matrix(esquerda, 'MUITAS')
            try:
                similarity_mean_node_muitas_esquerda = sum(similarity_mean_node_muitas_esquerda.mean()) / len(
                    similarity_mean_node_muitas_esquerda)
            except Exception as ex:
                similarity_mean_node_muitas_esquerda = sum(similarity_mean_node_muitas_esquerda.mean()) / 1

            similarity_mean_node_muitas_direita = get_similarity_matrix(direita, 'MUITAS')
            similarity_mean_node_muitas_direita = sum(similarity_mean_node_muitas_direita.mean()) / len(
                similarity_mean_node_muitas_direita)

            muitas_media = (similarity_mean_node_muitas_esquerda + similarity_mean_node_muitas_direita) / 2

            muitas_result[col] = muitas_media

        elif self.split == 'msm':

            traj_left = [t for i, t in enumerate(self.freqMatrix.index.values) if i in left_dict[col]]
            esquerda = self.data.loc[self.data['tid'].isin(traj_left)]
            traj_right = [t for i, t in enumerate(self.freqMatrix.index.values) if i in right_dict[col]]
            direita = self.data.loc[self.data['tid'].isin(traj_right)]

            similarity_mean_node_msm_esquerda = get_similarity_matrix(esquerda, 'MSM')
            try:
                similarity_mean_node_msm_esquerda = sum(similarity_mean_node_msm_esquerda.mean()) / len(
                    similarity_mean_node_msm_esquerda)
            except Exception as ex:
                similarity_mean_node_msm_esquerda = sum(similarity_mean_node_msm_esquerda.mean()) / 1
            similarity_mean_node_msm_direita = get_similarity_matrix(direita, 'MSM')
            similarity_mean_node_msm_direita = sum(similarity_mean_node_msm_direita.mean()) / len(
                similarity_mean_node_msm_direita)

            msm_media = (similarity_mean_node_msm_esquerda + similarity_mean_node_msm_direita) / 2

            msm_result[col] = msm_media

        elif self.split == "binary":

            differenceBetweenGroups = np.abs(len(right) - len(left))
            if minVar == -1 or differenceBetweenGroups < minVar:
                minVar = differenceBetweenGroups
                self.division = col

        elif self.split == "minVariance":

            calcMinVar = (self.variance[col]["left"] + self.variance[col][
                "right"]) / 2;  # average variance between groups
            if minVar == -1 or calcMinVar < minVar:
                minVar = calcMinVar
                self.division = col

        else:  # self.split == 'max_red'
            calcMinVar = self.variance[col]['initial'] - (self.variance[col]["left"] + self.variance[col][
                "right"]) / 2  # average variance between groups

            if calcMinVar > minVar:
                minVar = calcMinVar
                self.division = col

    if self.split == 'muitas':
        self.division = max(muitas_result, key=muitas_result.get)
    elif self.split == 'msm':
        self.division = max(msm_result, key=msm_result.get)
    elif self.split == 'var_red':
        self.division = max(split_value, key=split_value.get)

    asp, val = self.division.split('~')
    print(f"asp: {asp}; val: {val}")#degub
    self.thresholdVal = self.threshold['mean'][self.division]
    check_label(self, f'{asp} {val}', self.depth)

    if self.division not in self.skipVal:
        self.skipVal.append(self.division)

    self.value[self.depth].extend([len(self.left_group[self.division]), len(self.right_group[self.division])])
    self.nodeLabel[self.depth].append(self.id)
    print(f"nodeLabel: [self.depth={self.depth}].append(self.id={self.id})")#degub
    self.df_dict[str(self.id)] = self.freqMatrix

    self.parentName = asp + "\n[" + val + "]"
    print(f"parentName: {self.parentName}")#degub

    print("chamar func para nó da ESQUERDA")#degub
    traj_left = [t for i, t in enumerate(self.freqMatrix.index.values) if i in left_dict[self.division]]
    self.left = TreeNodeObject(self.data.loc[self.data['tid'].isin(traj_left)], self)
    dashtree(self.left, df)
    # self.left.dashTree()
    self.leftChildName = self.left.parentName
    print(f"leftChildName: {self.leftChildName}; left.id: {self.left.id}")#degub

    self.dendrogram_dict[str(self.id)].append(self.left.id)

    print("chamar func para nó da DIREITA")#degub
    traj_right = [t for i, t in enumerate(self.freqMatrix.index.values) if i in right_dict[self.division]]
    self.right = TreeNodeObject(self.data.loc[self.data['tid'].isin(traj_right)], self)
    dashtree(self.right, df)
    # self.left.dashTree()
    self.rightChildName = self.right.parentName

    self.dendrogram_dict[str(self.id)].append(self.right.id)
