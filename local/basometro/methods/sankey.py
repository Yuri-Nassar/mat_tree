import itertools
from datetime import datetime

import plotly.graph_objects as go


def sankey(cls, path):
    """
      Creates a sankey diagram from class dataset. Sankey diagram is a type of
      flow diagram in which the width of the arrows is proportional to the
      flow rate.
    """

    label = list(itertools.chain.from_iterable(cls.label.values()))
    value = list(itertools.chain.from_iterable(cls.value.values()))
    source = [val for val in cls.source for _ in (0, 1)]
    target = [tar for tar in range(1, len(source) + 1)]

    link = dict(source=source, target=target, value=value)

    node = dict(label=label, pad=50, thickness=5)
    data = go.Sankey(link=link, node=node)
    fig = go.Figure(data)
    file = 'sankey-{}Levels-{}-{}.png'.format(cls.maxDepth, datetime.now().strftime("%d-%m-%Y-%H-%M-%S"), cls.split)
    fig.write_image(format='png', file=path + file)
    fig.show()
