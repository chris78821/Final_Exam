"""
Plotting by annotating a dictionary and its values
"""

__author__ =  'Chris Thomack'

import matplotlib.pyplot as plt


def annotate_plot(annotations):
    # plt.text(x, y, s, fontdict=None, **kwargs)
    # x,y=floats, s=string, fontdict=None or dict, kwargs= other properties
    plt.text(annotations['position'][0], annotations['position'][1], annotations['string'],
             horizontalalignment=annotations['alignment'][0], verticalalignment=annotations['alignment'][1],
             fontsize=annotations['fontsize'])
    return


if __name__ == "__main__":
    from datetime import datetime
    import numpy as np

    test_annotations = {'string': f"Created by Chris Thomack {datetime.today().isoformat()}",
                        'position': np.array([4.75, 9.5]), 'alignment': ['left', 'bottom'], 'fontsize': 10}
    plt.plot(5, 10)
    plt.text(x=test_annotations['position'][0], y=test_annotations['position'][1], s=test_annotations['string'],
             horizontalalignment=test_annotations['alignment'][0], verticalalignment=test_annotations['alignment'][1],
             fontsize=test_annotations['fontsize'])
    plt.show()