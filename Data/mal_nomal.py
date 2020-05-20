import pandas as pd
from collections import Counter

data=pd.read_csv("C:/Users/ycjy0/Documents/_cho/capstone/4-1/DataSet/2nd_answer.csv",names=["name", "class"], sep=",", dtype='unicode')
an_id=data["name"]
an_class=data["class"]

count = Counter(an_class) 
print(count)

lst=[]
lst2=[]
true=1;

for i, row in data.iterrows(): 
	if (row['class']=='1') :
		lst.append({'name': row["name"], 'class':row["class"]} )
	else :
		lst2.append({'name': row["name"], 'class':row["class"]} )
#	else :
#		lst2.append({'name': n, 'class': c})

df=pd.DataFrame(lst)
df2=pd.DataFrame(lst2)
df.to_csv('C:/Users/ycjy0/Documents/_cho/capstone/4-1/DataSet/mal_nomal/mal_2nd.csv')
df2.to_csv('C:/Users/ycjy0/Documents/_cho/capstone/4-1/DataSet/mal_nomal/nomal_2nd.csv')
print(df, df2)
