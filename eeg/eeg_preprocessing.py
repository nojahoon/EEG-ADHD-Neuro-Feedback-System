import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as mat
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
import time
import os
from singledispatchmethod import singledispatchmethod


class preprocessing():

    def __init__(self, csv_path=None, frame=None, features=False):
        self.features = features
        self.outlier_size = 0
        self.return_csv_frame(csv_path, features)
        self.B = 0
        if frame is not None:
            self.csv_frame = frame
        for i in self.csv_frame.columns:
            self.csv_frame[i] = self.csv_frame[i].astype(float)

    def concat_frame(self, compare_csv_data_path: list):
        if isinstance(compare_csv_data_path, list):
            user = []
            for i in compare_csv_data_path:
                user.append(pd.read_csv(i))
            user = pd.concat(user)
        else:
            user = pd.read_csv(compare_csv_data_path)
        return user

    @singledispatchmethod
    def return_csv_frame(self, csv_path, features=None):
        pass

    @return_csv_frame.register(str)
    def _(self, csv_path, features=None):
        self.csv_frame = pd.read_csv(csv_path)[features]
        self.file_name = csv_path.split('/')[-1]

    @return_csv_frame.register(list)
    def _(self, csv_path, features=None):
        self.csv_frame = self.concat_frame(csv_path)[features]
        self.file_name = 'concat_ADHD_DataSet.csv'

    @property
    def original_frame(self):
        return self

    @original_frame.setter
    def setter_original_frame(self, frame):
        self.csv_frame = frame
        return self.csv_frame

    def StdScaler(self):
        ss = StandardScaler()
        self.result = ss.fit_transform(self.csv_frame)
        self.scaled_data_frame = pd.DataFrame(columns=self.features)
        for col, feature in enumerate(self.features):
            self.scaled_data_frame[feature] = [x[col] for x in self.result]
        return self.scaled_data_frame

    def Remove_Outlier(self, outlier_size=3, reset=True):

        if reset == True and outlier_size != self.outlier_size:
            self.outlier_size = outlier_size
            self.outlier_data_frame = self.csv_frame.copy(deep=True)

        for feature in self.features:
            self.outlier_data_frame = self.outlier_data_frame[
                (abs(self.outlier_data_frame[feature] - np.mean(self.outlier_data_frame[feature])) / np.std(
                    self.outlier_data_frame[feature]) <= outlier_size)]
        return self

    def chk_feature_graph(self, select_type='original', feature=None, manuel_size=0, show=False, savimg=False,
                          file_index=0,
                          file_name=None, original_compare=False, compare_csv_data_path=None):

        if select_type == 'original' or original_compare == True:
            A = plt.scatter(self.csv_frame.index, self.csv_frame[feature], label='ADHD')
            plt.legend(loc='lower right')
        if select_type == 'outlier':
            if manuel_size != 0:
                self.Remove_Outlier(outlier_size=manuel_size)
            A = plt.scatter(self.outlier_data_frame.index, self.outlier_data_frame[feature], label='Limit')
            plt.legend(loc='lower right', )
        if select_type == 'StdScaler':
            A = plt.scatter(self.scaled_data_frame.index, self.scaled_data_frame[feature])

        if compare_csv_data_path != None:
            user = self.concat_frame(compare_csv_data_path)
            A = plt.scatter(user.index, user[feature])

        if feature == None:
            raise Exception('feature 미설정')

        plt.tight_layout()
        plt.title(f'{feature} feature', fontsize=15)
        if show == True:
            plt.show()
        if savimg == True:
            plt.savefig(f'./{file_name}/{select_type}_compare_feature{file_index}.png')
        if show == False and savimg == False:
            return A
        return self

    def make_csv(self, type='original', frame=None, savpath='', index=0):

        if type == 'original':
            self.csv_frame.to_csv(f'./{savpath}/v{index}p.csv', index=False)
        if type == 'scaled':
            self.scaled_data_frame.to_csv(f'./{savpath}/scaled_v{index}p.csv', index=False)
        if type == 'outlier':
            self.outlier_data_frame.to_csv(f'./{savpath}/outlier_v{index}p.csv', index=False)
        if frame != None and type == 'manuel':
            self.outlier_data_frame.to_csv(f'./{savpath}/v{index}p.csv', index=False)

    def make3D_Graph(self, select_type='original', ):
        plt.figure(figsize=(5, 3.5))
        ax = plt.subplot(1, 1, 1, projection='3d')
        ax.scatter(self.csv_frame[self.features[0]], self.csv_frame[self.features[1]], self.csv_frame[self.features[2]],
                   cmap='Green', label='ADHD')
        ax.set_xlabel(self.features[0], fontsize=15)
        ax.set_ylabel(self.features[1], fontsize=15)
        ax.set_zlabel(self.features[2], fontsize=15)
        ax.legend(loc='lower right')
        plt.show()
        return ax

    def Single_Compare_Graph(self, select_type='original', manuel_size=0, show=False, savimg=False, file_index=0,
                             file_name=None, original_compare=False, compare_csv_data_path=None):
        fig, axs = plt.subplots(3, 3, figsize=(15, 15))
        axs = axs.flat

        ce = cycle(self.features)
        for i, ax in enumerate(axs):
            if i % 3 == 0:
                feature1 = next(ce)
            feature2 = next(ce)
            if select_type == 'original' or original_compare == True:
                A = ax.scatter(self.csv_frame[feature1], self.csv_frame[feature2])
                ax.set_xlim(min(self.csv_frame[feature1] - 100), max(self.csv_frame[feature1]) + 100)
                ax.set_ylim(min(self.csv_frame[feature2] - 100), max(self.csv_frame[feature2]) + 100)

            if select_type == 'outlier':
                if manuel_size != 0:
                    self.Remove_Outlier(outlier_size=manuel_size)
                A = ax.scatter(self.outlier_data_frame[feature1], self.outlier_data_frame[feature2])
                if original_compare == False:
                    ax.set_xlim(min(self.outlier_data_frame[feature1] - 100),
                                max(self.outlier_data_frame[feature1]) + 100)
                    ax.set_ylim(min(self.outlier_data_frame[feature2] - 100),
                                max(self.outlier_data_frame[feature2]) + 100)
            if select_type == 'StdScaler':
                self.StdScaler()
                A = ax.scatter(self.scaled_data_frame[feature1], self.scaled_data_frame[feature2])
                ax.set_xlim(min(self.scaled_data_frame[feature1] - 100), max(self.scaled_data_frame[feature1]) + 100)
                ax.set_ylim(min(self.scaled_data_frame[feature2] - 100), max(self.scaled_data_frame[feature2]) + 100)
            if compare_csv_data_path != None:
                if isinstance(compare_csv_data_path, str):
                    user = pd.read_csv(compare_csv_data_path)
                else:
                    user = self.concat_frame(compare_csv_data_path)
                A = ax.scatter(user[feature1], user[feature2])
            # fig.suptitle('Correlation by sensor', fontsize=30,  y=0.98)
            ax.set_xlabel(feature1, fontsize=15)
            ax.set_ylabel(feature2, fontsize=15)

        fig.tight_layout()
        if show == True:
            plt.show()
        if savimg == True:
            plt.savefig(f'./{file_name}/{select_type}_compare_feature{file_index}.png')
        if show == False and savimg == False:
            return axs
        return self

    def corr(self, select_type='original', manuel_size=0, savimg=False, show=False, file_name=None, file_index=0,
             ret=False):
        if select_type == 'original':
            B = self.csv_frame.corr(method='pearson')
        elif select_type == 'outlier':
            if manuel_size != 0:
                self.outlier_data_frame = self.Remove_Outlier(outlier_size=manuel_size)['frame']
            B = self.outlier_data_frame.corr(method='pearson')
            print(B)
        elif select_type == 'StdScaler':
            B = self.scaled_data_frame.corr(method='pearson')

        self.B = B
        if ret == True:
            return
        plt.figure(figsize=(15, 15))
        ax = plt.axes()
        ax.set_title('Correlation by sensor', fontsize=30)
        corr_matrix = sns.heatmap(data=B, annot=True, fmt='.2f', cmap='Blues', ax=ax)
        if show == True:
            plt.show()
        if savimg == True:
            plt.savefig(f'./{file_name}/corr{file_index}.png')
        if show == False and savimg == False:
            return corr_matrix
        return self


    def create_label(self, outlier_size, remove_size, savpath='', index=0):
        self.csv_frame['ADHD'] = 0
        print(1)
        for i in self.csv_frame.index:
            try:
                for feature in self.features:
                    if abs(self.csv_frame.loc[i, feature] - np.mean(
                            self.csv_frame[feature])) / np.std(
                        self.csv_frame[feature]) > remove_size:
                        self.csv_frame.loc[i, 'ADHD'] = 2
                        break
                    if abs(self.csv_frame.loc[i, feature] - np.mean(
                            self.csv_frame[feature])) / np.std(
                        self.csv_frame[feature]) > outlier_size:
                        self.csv_frame.loc[i, 'ADHD'] = 1
                        break
            except IndexError:
                pass

        self.csv_frame = self.csv_frame[self.csv_frame['ADHD'] != 2]
        print(self.csv_frame)
        self.make_csv(index=index, savpath=savpath)


def Combination_Compare_Graph(frames: list, show=False):
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    axs = axs.flat
    ce = cycle(frames[0].columns)
    for i, ax in enumerate(axs):
        if i % 3 == 0:
            feature1 = next(ce)
        feature2 = next(ce)
        for frame in frames:
            ax.scatter(frame[feature1], frame[feature2])
        ax.set_xlabel(feature1)
        ax.set_ylabel(feature2)
        ax.set_feature("")
    if show == True:
        plt.show()
    else:
        return axs


if __name__ == '__main__':

    label = [f'a{i}' for i in range(41)]
    feature = ['./All_channel_Control_DataSet/' + i for i in os.listdir('All_channel_Control_dataSet')]
    average = 0
    for i, l in enumerate(feature):
        try:
            a = preprocessing(l,
                              features=['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T7',
                                        'T8',
                                        'P7',
                                        'P8', 'Fz', 'Cz', 'Pz'])
            a.corr(show=False, ret=True)
            average += a.B
            print(average / (i + 1))

        except FileNotFoundError:
            pass
        else:
            print(l)
            pass
    plt.show()
    ax = plt.axes()
    ax.set_title('Mean Correlation by Control', fontsize=30)
    corr_matrix = sns.heatmap(data=average / (i + 1), annot=True, fmt='.2f', cmap='Blues', ax=ax)
    plt.show()
