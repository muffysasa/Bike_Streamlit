import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.title("Analisis Data Peminjaman Sepeda Pengguna Biasa dan Langganan")


st.subheader('Pertanyaan Bisnis')
st.write("1. Bagaimana pola pengguna biasa dan pelanggan pada setiap jam?")
st.write("2. Apakah ada hubungan cuaca/iklim terhadap pengguna tiap jam?")
st.write("3. Apakah ada hubungan antara jenis pengguna terhadap cuaca?")

hour = pd.read_csv("data_bike.csv") #panggil data
hour_sum_user = hour.groupby('start_hour')['cnt'].sum().reset_index()

col_sum = ['casual','registered']
byhour = hour.groupby('start_hour')[col_sum].sum().reset_index()

byseason = hour.groupby('season')[col_sum].sum().reset_index()
byweather = hour.groupby('weathersit')[col_sum].sum().reset_index()

byday = hour.groupby('weekday')[col_sum].sum().reset_index()
order_day = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
byday['weekday'] = pd.Categorical(byday['weekday'], categories=order_day, ordered=True)
byday = byday.sort_values(by='weekday')



with st.sidebar:
    st.subheader('Jumlah Pengguna Sepeda')
    col1, col2 = st.columns(2)
    
    with col1:
        total_registered = hour['registered'].sum()
        st.metric("Pengguna Langganan", value=total_registered)

    with col2:
        total_casual = hour['casual'].sum()
        st.metric("Pengguna Biasa", value=total_casual)


    

    
       

#Grafik 1
st.subheader('Grafik jumlah pengguna sepeda pada setiap jam')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    hour_sum_user['start_hour'],
    hour_sum_user['cnt'],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

#Grafik 1 & 2
st.subheader('Grafik jumlah peminjaman sepeda pada pengguna "Langganan" dan "Biasa" setiap jam')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
ax[0].plot(
    byhour['start_hour'],
    byhour['registered'],
    marker='o', 
    linewidth=2,
    color="#6aa84f"
)
ax[0].tick_params(axis='y', labelsize=20)
ax[0].tick_params(axis='x', labelsize=15)
 
ax[1].plot(
    byhour['start_hour'],
    byhour['casual'],
    marker='o', 
    linewidth=2,
    color="#674ea7"
)
ax[1].tick_params(axis='y', labelsize=20)
ax[1].tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

#Grafik 4 & 5
st.subheader('Grafik Penggunaan Sepeda berdasarkan Musim')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
ax[0].bar(
    byseason['season'],
    byseason['registered'],
    color="#6aa84f"
)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=35)

ax[1].bar(
    byseason['season'],
    byseason['casual'],
    color="#674ea7"
)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=35)
st.pyplot(fig)

#Grafik 6 & 7
st.subheader('Grafik Penggunaan Sepeda berdasarkan Cuaca')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
ax[0].bar(
    byweather['weathersit'],
    byweather['registered'],
    color="#6aa84f"
)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=35)

ax[1].bar(
    byweather['weathersit'],
    byweather['casual'],
    color="#674ea7"
)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=35)
st.pyplot(fig)

#Grafik 8 & 9
st.subheader('Grafik Penggunaan Sepeda berdasarkan Hari')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
ax[0].bar(
    byday['weekday'],
    byday['casual'],
    color="#6aa84f"
)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', rotation = 45, labelsize=35)

ax[1].bar(
    byday['weekday'],
    byday['registered'],
    color="#674ea7"
)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', rotation = 45, labelsize=35)
st.pyplot(fig)


st.subheader('Conclusion')
st.write("1. Jumlah pengguna biasa menggunakan sepeda banyak digunakan pada pukul 13.00-17.00 mencapai lebih dari 50.000 pengguna biasa. Sedangkan pengguna langganan menggunakan sepeda banyak digunakan pada 2 waktu yaitu pukul 08.00 mencapai lebih 240.000 dan pukul 17.00-18.00 mencapai lebih 260.000.")
st.write("2. Pengguna biasa dan langganan memiliki pola terhadap cuaca yang sama dalam menggunakan sepeda yaitu terbanyak digunakan saat cuaca cerah berawan dan tidak ada yang menggunakan sepeda saat cuaca hujan berat.")
st.write("3. Pengguna biasa dan langganan memiliki pola terhadap musim yang sama dalam menggunakan sepeda yaitu terbanyak digunakan saat musim gugur dan panas. Namun pengguna pelanggan juga menggunakan saat musim dingin dengan jumlah hampir sama saat musim panas sekitar 710.000 pengguna langganan.")
st.write(" ")
st.write("(-) Jumlah pengguna sepeda langganan lebih banyak daripada pengguna sepeda biasa. Pengguna langganan memiliki pola menggunakan sepeda saat working day (monday-friday). Sedangkan pengguna biasa memiliki pola menggunakan sepeda saat weekend day (saturday & sunday)")


