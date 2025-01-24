import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
import yaml

# params 

def load_params(params_path):
 test_size=yaml.safe_load(open(params_path,'r'))['data_ingestion']['test_size']
 return test_size

# import_data

def read_data(url):
 df = pd.read_csv(url)
 return df

# processing

def process_data(df):
 drop_column_name='tweet_id'
 df.drop(columns=[drop_column_name],inplace=True)
 final_df=df[df['sentiment'].isin(['neutral','love'])]
 final_df['sentiment'].replace({'love':1,'neutral':0},inplace=True)
 return final_df

# output_data

def save_data(data_path,train_data,test_data):
 os.makedirs(data_path)
 train_data.to_csv(os.path.join(data_path,'train.csv'))
 test_data.to_csv(os.path.join(data_path,'test.csv'))

# all in one function

def main():
 test_size=load_params('params.yaml')
 df=read_data('https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv')
 final_df=process_data(df)
 train_df,test_df=train_test_split(final_df,test_size=test_size,random_state=5)
 data_path=os.path.join('data','raw')
 save_data(data_path,train_df,test_df)

if __name__ =='__main__':
  main()








