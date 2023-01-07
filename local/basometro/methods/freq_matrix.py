import numpy as np
import pandas as pd


def generate_freq_matrix(self):
    # weather_ = ['label']
    weather_ = ['data', 'idVotacao', 'parlamentar']
    columns = self.data.drop(weather_, axis=1)

    dummies = pd.get_dummies(columns, prefix_sep='~')
    vals = dummies.drop(['tid'], axis=1)
    self.freqMatrix = pd.pivot_table(dummies, index=['tid'], values=vals.columns, aggfunc=np.sum)
