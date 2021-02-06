import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

if __name__ == '__main__':
    who = 'Control'
    choice = 'High'
    count = 5
    file = f'./ratio/{who}boxplot/'
    try:
        os.mkdir(file)
    except:
        pass

    feature = [f'./ratio/all_{who}_Theta_{choice}_beta/' + i for i in
               os.listdir(f'./ratio/all_{who}_Theta_{choice}_beta/')]

    j = 1
    k=1
    for i, f1 in enumerate(feature,start=1):
        print(f1)
        if i == 1:
            all = pd.read_csv(f1)
            all = all.rename(columns={f'Theta/ {choice}_beta': f'{j}-{k}'})
            print(all)
        else:
            disposable = pd.read_csv(f1)
            disposable = disposable.rename(columns={f'Theta/ {choice}_beta': f'{j}-{k}'})
            all = pd.merge(all, disposable, left_index=True, right_index=True, how='left')
        if i % count == 0:
            j += 1
            k=1
        else:
            k+=1

print(all)
print(all.mean())
# Grouped boxplot
b = sns.boxplot(data=all)
sns.lineplot(x=range(len(all.columns)), y=90)
#sns.lineplot(x=range(len(all.columns)), y=10)
"""
plt.vlines(3.5,ymax=len(all),ymin=0)
plt.vlines(7.5,ymax=len(all),ymin=0)
plt.vlines(11.5,ymax=len(all),ymin=0)
plt.vlines(15.5,ymax=len(all),ymin=0)
plt.vlines(19.5,ymax=len(all),ymin=0)
"""
plt.vlines(4.5,ymax=len(all),ymin=0)
plt.vlines(9.5,ymax=len(all),ymin=0)
plt.vlines(14.5,ymax=len(all),ymin=0)
plt.vlines(19.5,ymax=len(all),ymin=0)

b.set_xlabel("X Label", fontsize=10)
b.set_ylabel("Y Label", fontsize=15)
b.set_title('Non-ADHD',fontsize=18)
plt.ylim([0, 300])
plt.ylabel(f'Theta/{choice}_beta ratio (uV ^ 2 / Hz)')
plt.xlabel(f'Number of Non-ADHD')
plt.show()
# sns.plt.show()
