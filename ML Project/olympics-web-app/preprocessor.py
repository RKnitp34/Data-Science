import pandas as pd
athelet_df = pd.read_csv('athlete_events.csv')
regions_df= pd.read_csv('noc_regions.csv')
df = athelet_df.merge(regions_df , how ='left' , on ='NOC')  
def preprocess():
    global df 
    df =df[ df['Season']=='Summer']
    df.drop_duplicates(inplace = True)
    df = pd.concat([df,pd.get_dummies(df['Medal'])] , axis = 1)
    return df 
   

