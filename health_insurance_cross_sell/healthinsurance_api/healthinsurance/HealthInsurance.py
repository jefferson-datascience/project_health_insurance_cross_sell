import pandas as pd
import pickle
import inflection
import json


class HealthInsurance(object):
    
    def __init__(self):
        
        self.home_path = '/'
        self.annual_premium_scaler = pickle.load( open( self.home_path + '/features/annual_premium_scaler.pkl', 'rb' ) )
        self.age_scaler            = pickle.load( open( self.home_path + '/features/age_scaler.pkl', 'rb' ) )
        self.vintage_scaler        = pickle.load( open( self.home_path + '/features/vintage_scaler.pkl', 'rb' ) )

        
    def data_cleaning(self, df1):
        
        snakecase = lambda x: inflection.underscore(x)
        
        # Limpeza dos nomes das colunas
        df1.columns = [snakecase(element) for element in df1.columns.to_list()]
        
        # retorno do dataframe com as keys da coluna organizadas.
        return df1
    
    
    def feature_engineering(self, df2):    
    
        # gender
        df2['gender'] = df2['gender'].apply(lambda x: x.lower())

        # vehicle_damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)

        # vehicle_age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_years' 
                                                      if x == '1-2 Year' else 'below_1_year')
    
        # retorno do dataframe com as variáveis limpas
        return df2
    
    
    def data_preparation(self, df5):
        
        
        #### ----------------------------- RESCALING ----------------------------------------------------- ####
        
        
        # padronização da variável annual_premium
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5[['annual_premium']].values)
        
        # reescala variável age
        df5['age'] = self.age_scaler.transform(df5[['age']].values)
        
        # reescala variável vintage
        df5['vintage'] = self.vintage_scaler.transform(df5[['vintage']].values)
        
        
        #### ----------------------------- ENCODING ----------------------------------------------------- ####

        
        # Frequencily Enconding - region code
        fe_encode_region_code = df5.groupby('region_code').size()/len(df5)
        df5.loc[ : , 'region_code'] = df5['region_code'].map(fe_encode_region_code)
        
        # Order Enconding - vehicle age
        df5 = pd.get_dummies(df5, prefix='vehicle_age', columns=['vehicle_age'])
        
        # Frequency Encoding - policy_sales_channel
        fe_policy_sales_channel = df5.groupby('policy_sales_channel').size()/len(df5)
        df5.loc[ : , 'policy_sales_channel'] = df5['policy_sales_channel'].map(fe_policy_sales_channel)
        
        # Frequencily Encoding - gender
        fe_encode_gender = df5.groupby('gender').size()/len(df5)
        df5.loc[ : , 'gender'] = df5['gender'].map(fe_encode_gender)
        
        # colunas com maiores relevâncias
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 
                         'vehicle_damage', 'policy_sales_channel', 'previously_insured']
        
        # retorno com os dados totalmente preparados 
        return df5[cols_selected]

        
    def prediction(self, model, dataframe_preparation, dataframe_original):
            
        # Lista com as predições realizadas.
        propensity_score = model.predict_proba(dataframe_preparation)
            
        # Criando a coluna propensity_score
        dataframe_original['propensity_score'] = propensity_score[ : , 1].tolist()
            
        # Rankeamento
        dataframe_original = dataframe_original.sort_values(by=['propensity_score'], 
                                                            ascending=False).reset_index(drop=True)

        # colunas importantes
        # dataframe_original = dataframe_original[['id', 'propensity_score']]

        # Criar a coluna ranking
        dataframe_original['ranking'] = dataframe_original.index + 1
            
        # retorno da lista
        return dataframe_original.to_json(orient='records', date_format='iso')
                                                            
                                                            