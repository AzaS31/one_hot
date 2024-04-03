import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_columns = pd.unique(data['whoAmI']) 
one_hot = pd.DataFrame({col: (data['whoAmI'] == col).astype(int) for col in one_hot_columns})

print(one_hot.head())

