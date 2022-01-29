#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import imblearn
from IPython import get_ipython
from PIL import Image


# In[2]:


model=pickle.load(open('warranty_claim.pkl','rb'))


# In[3]:


header = st.container()
dataset= st.container()
features=st.container()
info=st.container()
matrix ,matrix1= st.columns(2)
mat,mat1=st.columns(2)


# In[4]:


with header :
    st.title('Warranty Claim')


# In[5]:


with dataset:
    st.markdown('* DataSet is about whether the claiment is Fraudulent or Non-Fraudulent*')
    
    st.markdown('** . Raw Dataset contains  358 Rows and 21 columns, it doesn’t have any NAN values , Every Columns has 358 data points . Fraudcolumn is target column else 20 columns are independent ,Data set is combination of categorical , numerical values.“ Fraud “ column is a target column of dataset , which indicate wheather the claimant applied for warrenty is Fraudulent or Not.column consist of 1 and 0 , 1 is Fraudulent 0 is non Fraudulent.**')
    
    st.markdown('***DataSet***')
    df=pd.read_csv('C:\\Users\\piyus\\Documents\\ExcelR project\\WarrantyClaim.csv')
    df


# In[6]:


with features:
    st.header('~ Feature')
    st.markdown('** # Following are the information about featuers in dataset**')
    st.markdown('** . Region 1 ** - 8 regions - NE,NW,SE,SW,E,W,N,S')
    st.markdown('** . State 1** -Names fo state')
    st.markdown('** . Area 1** -Urban,Rural')
    st.markdown('** . City 1** -Hyderabad,Delhi,Goa...')
    st.markdown('** . Consumer profile**/ type 1 -Business customer /Personal')
    st.markdown('** . Product category 1** -Entertainment / Household')
    st.markdown('** . Product type 1** -TV / AC')
    st.markdown('** . Part number** / Issue category 1 0- -No issue / No componenent, 1- repair, 2-replacement')
    st.markdown('** . Claim value 1** -would we have this value during claim process, probably an approximate claim value could be tagged')
    st.markdown('** . Service centre 1 **-Service Centre code (10,11,12,13,14,15)')
    st.markdown('** . Age in days 1** -Age of the product')
    st.markdown('** . Purchased from 1 **-Dealer,Manufacturer,Internet')
    st.markdown('** . Call details 1** -Call duration in minutes')
    st.markdown('** . Purpose 1** -Claim,Complaint,Other')
    st.markdown('** . Fraud** (1 if Fraud else 0) 1 1 or 0 : - Fraud-1 Non-Fraud-0')


# In[ ]:





# In[7]:


st.sidebar.header('claiments information')


# In[8]:


def user_input_features():
    st.header('User Input Features')
    Product_type_AC = st.sidebar.text_input('Product_type_AC', )
    Product_type_TV = st.sidebar.text_input('Product_type_TV', )
    Claim_Value=st.sidebar.text_input('Claim Value',)
    product_Age=st.sidebar.text_input('Product Age',)
    Call_details=st.sidebar.text_input('Call Details',)
    Purchased_from_Internet=st.sidebar.text_input('Purchased_from_Internet',)
    Purchased_from_Manufacturer=st.sidebar.text_input('Purchased_from_Manufacturer',)
    AC_1001_Issue=st.sidebar.text_input('AC_1001_Issue',)
    AC_1002_Issue=st.sidebar.text_input('AC_1002_Issue',)
    AC_1003_Issue=st.sidebar.text_input('AC_1003_Issue',)
    TV_2001_Issue=st.sidebar.text_input('TV_2001_Issue',)
    TV_2002_Issue=st.sidebar.text_input('TV_2002_Issue',)
    TV_2003_Issue=st.sidebar.text_input('TV_2003_Issue',)
    Service_Centre=st.sidebar.text_input('Service_Centre',)
    Consumer_profile_Business=st.sidebar.text_input('Consumer_profile_Business',)
    Consumer_profile_Personal=st.sidebar.text_input('Consumer_profile_Personal',)
    Product_category_Household=st.sidebar.text_input('Product_category_Household',)
    Product_category_Entertainment=st.sidebar.text_input('Product_category_Entertainment',)
    Region_North=st.sidebar.text_input('Region_North',)
    Region_North_East=st.sidebar.text_input('Region_North_East',)
    Region_North_West=st.sidebar.text_input('Region_North_West',)
    Region_South=st.sidebar.text_input('Region_South',)
    Region_South_East=st.sidebar.text_input('Region_South_East',)
    Region_South_West=st.sidebar.text_input('Region_South_West',)
    Region_West=st.sidebar.text_input('Region_West',)
    City_Ahmedabad=st.sidebar.text_input('City_Ahmedabad',)
    City_Bangalore=st.sidebar.text_input('City_Bangalore',)
    City_Bhubaneswar=st.sidebar.text_input('City_Bhubaneswar',)
    City_Chennai=st.sidebar.text_input('City_Chennai',)
    City_Hyderabad=st.sidebar.text_input('City_Hyderabad',)
    City_Kochi=st.sidebar.text_input('City_Kochi',)
    City_Kolkata=st.sidebar.text_input('City_Kolkata',)
    City_Lucknow=st.sidebar.text_input('City_Lucknow',)
    City_Mumbai=st.sidebar.text_input('City_Mumbai',)
    City_New_Delhi=st.sidebar.text_input('City_New_Delhi',)
    City_Vadodara=st.sidebar.text_input('City_Vadodara',)
    City_Vijayawada=st.sidebar.text_input('City_Vijayawada',)
    State_Andhra_Pradesh=st.sidebar.text_input('State_Andhra_Pradesh',)
    State_Delhi=st.sidebar.text_input('State_Delhi',)
    State_Gujarat=st.sidebar.text_input('State_Gujarat',)
    State_Karnataka=st.sidebar.text_input('State_Karnataka',)
    State_Kerala=st.sidebar.text_input('State_Kerala',)
    State_Maharashtra=st.sidebar.text_input('State_Maharashtra',)
    State_Tamil_Nadu=st.sidebar.text_input('State_Tamil_Nadu',)
    State_Uttar_Pradesh=st.sidebar.text_input('State_Uttar_Pradesh',)
    State_West_Bengal=st.sidebar.text_input('State_West_Bengal',)
    Area_Urban=st.sidebar.text_input('Area_Urban',)
    Area_Rural=st.sidebar.text_input('Area_Rural',)
    Purpose_Claim=st.sidebar.text_input('Purpose_Claim',)
    Purpose_Complaint=st.sidebar.text_input('Purpose_Complaint',)
    Data = {'Product_type_AC': Product_type_AC,'Product_type_TV': Product_type_TV, 'Claim Value': Claim_Value,
            'Product Age': product_Age, 'Call Details': Call_details,
             'Purpose_Claim': Purpose_Claim,'Purpose_Complaint': Purpose_Complaint,'Purchased_from_Internet':Purchased_from_Internet,
            'Purchased_from_Manufacturer':Purchased_from_Manufacturer,'Service_Centre':Service_Centre,'AC_1001_Issue':AC_1001_Issue,
            'AC_1002_Issue':AC_1002_Issue
             ,'AC_1003_Issue':AC_1003_Issue,'TV_2001_Issue':TV_2001_Issue,'TV_2002_Issue':TV_2002_Issue,
            'TV_2003_Issue':TV_2003_Issue,'Region_North':Region_North,'Region_North_East':Region_North_East,
            'Region_North_West':Region_North_West,'Region_South':Region_South,'Region_South_East':Region_South_East,
            'Region_South_West':Region_South_West,'Region_West':Region_West,'State_Andhra_Pradesh':State_Andhra_Pradesh,
             'State_Delhi':State_Delhi,'State_Gujarat':State_Gujarat,'State_Karnataka':State_Karnataka,'State_Kerala':State_Kerala,
             'State_Maharashtra':State_Maharashtra,'State_Tamil_Nadu':State_Tamil_Nadu,
        'State_Uttar_Pradesh':State_Uttar_Pradesh,'State_West_Bengal':State_West_Bengal,'Area_Urban':Area_Urban,
            'Area_Rural':Area_Rural,'City_Ahmedabad':City_Ahmedabad,
        'City_Bangalore':City_Bangalore,'City_Bhubaneswar':City_Bhubaneswar,'City_Chennai':City_Chennai,
            'City_Hyderabad':City_Hyderabad,'City_Kochi':City_Kochi,
        'City_Kolkata':City_Kolkata,'City_Lucknow':City_Lucknow,'City_Mumbai':City_Mumbai,'City_New_Delhi':City_New_Delhi,
        'City_Vadodara':City_Vadodara,'City_Vijayawada':City_Vijayawada,'Consumer_profile_Business':Consumer_profile_Business,'Consumer_profile_Personal':Consumer_profile_Personal,
            'Product_category_Household':Product_category_Household,'Product_category_Entertainment':Product_category_Entertainment
   }
    features = pd.DataFrame(Data,index=[0])
    return features
def main():
    
   
    st.sidebar.subheader("Warranty Claim- Fraud Detection")
    
    
    
    
    
    
    
    
    
    html_temp = """
    <div style="background-color:White;padding:10px">
    <h2 style="color:white;text-align:center"> Fraud Detection  </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    df = user_input_features()
    
    
   
           
    st.subheader('Input details')
    st.write(df)
    result = ""
    if st.button("Predict"):
        result = model.predict(df)
    st.success('The prediction is {}'.format(result))
    st.markdown('[0] **Non-Fraudulent**')
    st.markdown('[1] **Fraudulent**')
   
    
    
    

if __name__=='__main__':
    main()


# In[9]:


with info:
    st.header('~ graphical representation ')
    st.markdown('**  # Visualizing different columns with respect to target column **')


# In[10]:


with matrix :
    
    image= Image.open('chart.png')
    st.image(image,'')
    


# In[11]:


with matrix1:
    
    image= Image.open('img.png')
    st.image(image,'')
    


# In[12]:


with mat:
    
    image= Image.open('chart1.png')
    st.image(image,'')


# In[13]:


with mat1:
    
    image= Image.open('chart2.png')
    st.image(image,'')
    

