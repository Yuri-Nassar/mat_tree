import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def eda_corr(dataset, usr):
    """
    Exploratory Data Analysis. It generates a plot of correlation matrix of
    all features of a given dataset and a given user.

    Parameters
    ----------
    dataset : pandas.DataFrame
      Dataset of trajectories of a given cluster.
    user : int
      User label in a given cluster.
    """
    df = dataset
    idx = dataset.index
    ds = df[df.tid.isin(idx)]

    if usr is not None:
        ds = ds[ds.label == usr]

    # columns = ['tid', 'time', 'poi', 'type', 'rating', 'label', 'weather']
    columns = ['tid', 'data', 'idVotacao', 'parlamentar']
    ds = ds.drop(columns=columns)
    corr = pd.get_dummies(ds)
    corr = corr.corr()

    plt.figure(figsize=(40, 22))
    plt.imshow(corr, cmap='Blues', interpolation='none', aspect='auto')
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns, rotation='vertical')
    plt.yticks(range(len(corr)), corr.columns)
    plt.suptitle('Correlation between variables', fontsize=15, fontweight='bold')
    plt.grid(False)


def eda(dataset, feature, usr):
    """
    Exploratory Data Analysis. It generates a plot bar of a given feature of
    a given dataset and a given user.

    Parameters
    ----------
    usr
    dataset : pandas.DataFrame
      Dataset of trajectories of a given cluster.
    feature : str
      Feature or Aspect intended for EDA.
    usr : int
      User label in a given cluster.
    """
    df = dataset
    idx = dataset.index

    df_total = df.copy()
    df1 = df[df.tid.isin(idx)]

    if usr is not None:
        df_total = df_total[df_total.label == usr]
        df1 = df1[df1.label == usr]

    df_total.reset_index(inplace=True)
    df1.reset_index(inplace=True)

    place_type_abs = df_total[feature]
    place_type = df1[feature]

    ''' Calculando a frequencia do cluster '''
    values = np.sort(np.unique(place_type_abs))
    freq = np.zeros(len(values))
    ind = 0
    for i in values:
        counter = 0
        for j in range(0, len(place_type)):
            if place_type[j] == i:
                counter = counter + 1
        freq[ind] = counter
        ind = ind + 1

    ''' Calculando a frequencia absoluta '''
    values_abs = np.sort(np.unique(place_type_abs))
    freq_abs = np.zeros(len(values_abs))
    ind_abs = 0
    for k in values_abs:
        counter = 0
        for l in range(0, len(place_type_abs)):
            if place_type_abs[l] == k:
                counter = counter + 1
        freq_abs[ind_abs] = counter
        ind_abs = ind_abs + 1

    relative = []
    for i in range(len(freq)):
        relative.append(f'{(freq[i] / freq_abs[i]) * 100}')

    fig = plt.figure(figsize=(15, 5))
    ax = plt.gca()

    y_pos = np.arange(len(values))
    plt.xticks(y_pos, values)
    plt.bar(y_pos, freq)
    plt.xticks(fontsize=10, rotation='vertical')
    plt.yticks(fontsize=10)
    plt.xlabel("Valores", fontsize=15)
    plt.ylabel("Frequência", fontsize=15)

    for i, p in enumerate(ax.patches):
        ax.text(p.get_x() + p.get_width() / 2., p.get_height(), f'{int(p.get_height())} ({relative[i]:.4}%)',
                fontsize=10, color='black', ha='center', va='bottom')
