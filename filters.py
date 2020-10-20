import streamlit as st


#need to add something for velo when im not so lazy

def filters(drone_df, all_df):
    rcs = st.sidebar.slider('Select Range of RCS Filter', -100, 100, (0,8),1)
    sv3 = st.sidebar.slider('Select Range of SV3 Filter',-100, 300,(0,2),1)
    sva = st.sidebar.slider('Select Range of SVA Filter',0, 1000,(23,139),1)
    vmg = st.sidebar.slider('Select Range of VMG Filter',-1.0, 1.0,(-.8,.9),0.1)
    alt = st.sidebar.slider('Select Range of Altitude Filter',-100, 1000,(100,200),10)
    dist = st.sidebar.slider('Select Range of Distance Filter',0, 8000,(0,3000),100)
    speed = st.sidebar.slider('Select Range of Velocity Filter',0, 100,(9,11),1)
    
    drone_df = drone_df[(drone_df['RCS'] >= rcs[0])]
    drone_df = drone_df[(drone_df['RCS'] <= rcs[1])]
    drone_df = drone_df[(drone_df['SV3'] >= sv3[0])]
    drone_df = drone_df[(drone_df['SV3'] <= sv3[1])]
    drone_df = drone_df[(drone_df['SVA'] >= sva[0])]
    drone_df = drone_df[(drone_df['SVA'] <= sva[1])]
    drone_df = drone_df[(drone_df['VMG'] >= vmg[0])]
    drone_df = drone_df[(drone_df['VMG'] <= vmg[1])]
    drone_df = drone_df[(drone_df['Altitude'] >= alt[0])]
    drone_df = drone_df[(drone_df['Altitude'] <= alt[1])]
    drone_df = drone_df[(drone_df['Distance'] >= dist[0])]
    drone_df = drone_df[(drone_df['Distance'] <= dist[1])]
    drone_df = drone_df[(drone_df['Speed'] >= speed[0])]
    drone_df = drone_df[(drone_df['Speed'] <= speed[1])]


    all_df = all_df[(all_df['RCS'] >= rcs[0])]
    all_df = all_df[(all_df['RCS'] <= rcs[1])]
    all_df = all_df[(all_df['SV3'] >= sv3[0])]
    all_df = all_df[(all_df['SV3'] <= sv3[1])]
    all_df = all_df[(all_df['SVA'] >= sva[0])]
    all_df = all_df[(all_df['SVA'] <= sva[1])]
    all_df = all_df[(all_df['VMG'] >= vmg[0])]
    all_df = all_df[(all_df['VMG'] <= vmg[1])]
    all_df = all_df[(all_df['Altitude'] >= alt[0])]
    all_df = all_df[(all_df['Altitude'] <= alt[1])]
    all_df = all_df[(all_df['Distance'] >= dist[0])]
    all_df = all_df[(all_df['Distance'] <= dist[1])]
    all_df = all_df[(all_df['Speed'] >= speed[0])]
    all_df = all_df[(all_df['Speed'] <= speed[1])]

    return(drone_df, all_df)
 

def velo_filter(drone_df, all_df):
    velo = st.sidebar.slider('Select Range of Velocity Filter',-100, 100,(-25,75))
    return(velo[0],velo[1])