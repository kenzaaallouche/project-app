import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pyautogui
import pandas as pd
import time
@st.cache_data
def data ():
    parameters = ['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']
    dfk= pd.DataFrame(columns=parameters)
    df1=dfk
    dfk.to_excel('data.xlsx')
    dfk
    st.cache_data.clear()
@st.cache_data(experimental_allow_widgets=True)
def tt(input_data):
    st.cache_data.clear()
    if input_data:

        placeholder_2 = st.empty()

        with placeholder_2.form(key = 'my_form', clear_on_submit = True):			

            st.write('Etes-vous sur que toutes les informations sont correctes?',a)
                    
            submit_button = st.form_submit_button(label = 'Ajouter')

            if submit_button:
                        if (len(a)<7):
                            st.warning('Data non valide verifiez vous informations .')
                            st.stop()
                        if (len(a)>7):
                            st.warning('Data non valide verifiez vous informations .')
                            st.stop()
                        new=['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']
                        new_row = pd.DataFrame(a, index=new).T
                        df2 = pd.read_excel('data.xlsx')
                        df2 = pd.concat((df2, new_row),ignore_index=True)
                        df2.to_excel('data.xlsx')
                        st.write('client ajouter avec succes')
                        time.sleep(1)
                        input_data = placeholder.text_area(label = 'Clients', key = '2')
                        placeholder_2.empty()
                        
                        
@st.cache_data(experimental_allow_widgets=True)           
def button():
    
   
    
        df2 = pd.read_excel('data.xlsx')
        df3=df2[['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']].copy()
        
        AgGrid(df3, height=400)
        
def affiche_clients(a,df):
    if not (a):
        st.write('The current costumer', a)
    else:
        #df.loc[len(df)+1]=a
        st.dataframe(df)




col1, col2, col3 = st.columns(3)

with col1:
   st.header("")
   

with col2:
   st.header("")
   #original_title = '<h2 style="font-family:Courier; color:red; font-size: 15px center;">Ajouter Clients</h2>'
   #st.markdown(original_title, unsafe_allow_html=True)
   st.image("a.jpg")
with col3:
   st.header("")
#original_title = '<h2 style="font-family:Courier; color:red; font-size: 15px center;">Ajouter Clients</h2>'
#st.markdown(original_title, unsafe_allow_html=True)  


placeholder = st.empty()

@st.cache_data(experimental_allow_widgets=True)
def g():
    
    input_data = placeholder.text_area( label='',placeholder='inserer clients isi',key = '3')
    return input_data
h=g()
a=h.split("\n")
            


st.cache_data.clear()
tt(h)
df2 = pd.read_excel('data.xlsx')
if len(df2)>0:
        
        df3=df2[['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']].copy()
        
        AgGrid(df3, columns_auto_size_mode=1,editable=True)
        
        

st.cache_data.clear()



    
'''










'''
with st.spinner('Wait for it...'):
    

    if st.button("CLEAN DATA"):
        time.sleep(2)
        data ()
        placeholder.text_area( label='',value='ff')
        
        
        st.experimental_rerun()

        placeholder.empty()