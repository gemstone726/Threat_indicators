import pandas as pd
import streamlit as st

@st.cache
def min_max_mean(df):
    martix = [(df['RCS'].min(), df['SV3'].min(), df['SVA'].min(), df['VMG'].min(),df['Altitude'].min(), df['Distance'].min(), df['Speed'].min()), 
              (df['RCS'].max(), df['SV3'].max(), df['SVA'].max(), df['VMG'].max(),df['Altitude'].max(), df['Distance'].max(), df['Speed'].max()),
              (df['RCS'].mean(), df['SV3'].mean(), df['SVA'].mean(), df['VMG'].mean(),df['Altitude'].mean(), df['Distance'].mean(), df['Speed'].mean()),
              
    ]

    min_max_data = pd.DataFrame(martix, index=list(['Min', 'Max', 'Mean']), columns=list(['RCS', 'SV3', 'SVA', 'VMG', 'Alt', 'Dist', 'Velo']))
    return(min_max_data)