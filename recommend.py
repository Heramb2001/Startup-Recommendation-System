import streamlit as st
import pickle
import pandas as pd 
similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(startup):
    startups_index=startups[startups['Startup_name'] == startup].index[0]
    distances=similarity[startups_index]
    startups_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:5]
    recommended_startups=[]
    for i in startups_list:
       recommended_startups.append(startups.iloc[i[0]].Startup_name)
    return recommended_startups
startups_dict=pickle.load(open('startupsdict.pkl','rb'))
startups=pd.DataFrame(startups_dict)
st.title("Startup Recommender system")
selected_startup_name=st.selectbox(
    'Hello',
    startups['Startup_name'].values
)
if st.button("Search"):
    recommendations=recommend(selected_startup_name)
    for i in recommendations:
        st.write(i)
    