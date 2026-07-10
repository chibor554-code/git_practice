

import matplotlib.pyplot as plt 
import pandas as pd 
 
df = pd.read_csv('students.csv') 
 
# Bar chart — average score by subject 
avg = df.groupby('subject')['score'].mean() 
 
plt.figure(figsize=(8, 5)) 
plt.bar(avg.index, avg.values, color='steelblue') 
plt.title('Average Score by Subject') 
plt.xlabel('Subject') 
plt.ylabel('Average Score') 
plt.tight_layout() 
plt.savefig('scores_by_subject.png')   # save the chart as a file 
plt.show()                             # display on screen 


