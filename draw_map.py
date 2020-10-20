import pandas as pd
import streamlit as st
import pydeck as pdk 

red = '[255,0,0]'
yellow = '[255,255,0]'
lime_green = '[69,229,33]'

def lat_long(non_filtered_df,filtered_df,not_drone_df,track_id):

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=pdk.ViewState(
            latitude=1.327768,
            longitude=103.982339,
            zoom=15,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=not_drone_df,
                get_position='[lon, lat]',
                get_color= yellow,
                get_radius=15,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=non_filtered_df,
                get_position='[lon, lat]',
                get_color= lime_green,
                get_radius=15,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=filtered_df,
                get_position='[lon, lat]',
                get_color= red,
                get_radius=15,
            ),

        ],
    ))