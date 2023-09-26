import pandas as pd

data = pd.read_csv('results_new.csv')

with open('results_new.md', 'w') as f:
    for i in range(len(data)):
        f.write('### Question: ' + data['Questions'][i] + '\n')
        f.write('#### Old Answer: ' + '\n' + '- ' + data['Expected Answers'][i] + '\n')
        f.write('#### New Answer: ' + '\n' + '- ' + data['Bot Answers'][i] + '\n')
        f.write('---' + '\n')
