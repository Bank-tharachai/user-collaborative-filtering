import pandas as pd
import numpy as np
import math

Ratings=pd.read_csv("/home/4/16B09737/Documents/src/user-collaborative-filtering/tour_score.csv")

Mean = Ratings.groupby(['user_id'], as_index=False,sort=False).mean().rename(columns={'rating':'rating_mean'})

[['user_id','rating_mean']]

Ratings = pd.merge(Ratings,Mean,on='user_id',how='left',sort=False)
Ratings['rating_adjusted']=Ratings['rating']-Ratings['rating_mean']
Ratings

distinct_users=np.unique(Ratings['user_id'])
