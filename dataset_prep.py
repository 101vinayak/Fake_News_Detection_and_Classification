import pandas as pd
import numpy as np

def dataset():
    
    data1_fake = pd.read_csv('Datasets/572515_1037534_bundle_archive/Fake.csv')
    
    data1_fake = data1_fake[['title','text','subject']]
    data1_fake.columns = ['Headline','Body','Label']
    data1_fake.loc[:,'Label'] = 0
    
    data1_real = pd.read_csv('Datasets/572515_1037534_bundle_archive/True.csv')
    
    data1_real = data1_real[['title','text','subject']]
    data1_real.columns = ['Headline','Body','Label']
    data1_real.loc[:,'Label'] = 1
    
    data1 = data1_fake.append(data1_real, ignore_index=True)
    data1 = data1.sample(frac=1)
    
    data2 = pd.read_csv('Datasets/6410_9356_bundle_archive/data.csv')

    data2 = data2[['Headline','Body','Label']]
    data2.columns = ['Headline','Body','Label']
    data2 = data2.sample(frac=1)
    
    data1.append(data2, ignore_index=True)
    data = data1.sample(frac=1)
    
    data.to_csv('Dataset.csv', index=False)
    loc = 'Dataset.csv'
    
    return loc