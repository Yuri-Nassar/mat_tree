import math


def get_entropy(dataset):
    """
      Calculates the entropy value of a given dataset.

      Parameters
      ----------
      dataset : pandas.DataFrame
        Dataset of trajectories of a given cluster

      Returns
      -------
      Float
        Entropy value of a given cluster.
    """
    df1 = dataset.copy()
    entropy_dict = {}
    for e in df1.label.unique():
        num_traj = df1[df1.label == e].tid.unique()
        entropy_dict[e] = len(num_traj)
    total = sum(entropy_dict.values())

    entropy_value = 0
    for key, value in entropy_dict.items():
        p = value / total
        entropy_value += p * math.log2(p)

    try:
        max_entropy = math.log2(len(df1.label.unique()))
        return -entropy_value / max_entropy
    except Exception as e:
        return -entropy_value