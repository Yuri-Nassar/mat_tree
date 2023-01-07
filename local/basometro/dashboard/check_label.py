import itertools


def check_label(self, label, depth):
    """
    Method used to verify cluster aspect label in order to avoid duplicate
    names in Sankey Diagram.

    Parameters
    ----------
    self
    label : str
      Cluster aspect label.
    depth : int
      Cluster depth level.
    """

    items = list(itertools.chain.from_iterable(dict(self.label).values()))

    if label in items:
        if '#' in label:
            label, num = label.split('#')
            label += f'#{int(num) + 1}'
        else:
            label += f'#1'
            check_label(self, label, depth)
    else:
        self.label[depth].append(label)
