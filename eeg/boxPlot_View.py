import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

if __name__ == '__main__':
    who = 'ADHD'
    file = f'./ratio/{who}boxplot/'
    try:
        os.mkdir(file)
    except:
        pass

    feature = [f'./ratio/all_{who}_Theta_High_beta/' + i for i in os.listdir(f'./ratio/all_{who}_Theta_High_beta/')]

    for i, f1 in enumerate(feature):
        if i == 0:
            all = pd.read_csv(f1)
            all = all.rename(columns={'Theta/ High_beta': f'{who}{i}'})
        else:
            disposable = pd.read_csv(f1)
            disposable = disposable.rename(columns={'Theta/ High_beta': f'{who}{i}'})
            all = pd.merge(all, disposable, left_index=True, right_index=True, how='left')
print(all)

# Grouped boxplot
sns.boxplot(data=all)
sns.lineplot(x=range(len(all.columns)), y=90)
sns.lineplot(x=range(len(all.columns)), y=10)
plt.ylabel('Theta/High_beta ratio')
plt.show()
# sns.plt.show()
