from matplotlib import pyplot as plt

from local.basometro.methods.eda import eda, eda_corr


def eda_dashboard(user, df, self):
    # dataset_ = self.df_dict[df]
    if user == 'ALL':
        # for parameter in drop.columns:
        #     print('plotting ' + parameter)
        #     eda(df, parameter, usr=None)
        #     plt.savefig('C:\\Users\\P01062\\PycharmProjects\\mat_tree\\images\\eda\\' + parameter + '.png')
        eda_corr(df, usr=None)
        plt.savefig('C:\\Users\\P01062\\PycharmProjects\\mat_tree\\images\\eda\\correlation.png')
    else:
        eda(df, 'root_type', usr=user)
        eda(df, 'day', usr=user)
        # eda_corr(df, usr=user)
        # plt.show()
