import streamlit as st
import ee
import requests

# 1. GEE Yetkilendirme
# ee.Authenticate() # İlk çalıştırmada bir kez gerekir
ee.Initialize()

st.title("Tahtalı Barajı Dijital Su İkizi")

# 2. Sidebar (Girdiler)
st.sidebar.header("Parametreler")
cekilen_su = st.sidebar.slider("Günlük Şehir Çekimi (m³)", 200000, 300000, 250000)

# 3. Hava Durumu API Entegrasyonu (Örnek)
api_key = "SENIN_API_ANAHTARIN"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Menderes,TR&appid={api_key}&units=metric"
weather_data = requests.get(weather_url).json()
sicaklik = weather_data['main']['temp']

# 4. Hesaplama Motoru (Senin GEE verilerinle)
alan = 12087740 # m2 (GEE'den bulduğumuz değer)
buharlasma = alan * (sicaklik * 0.0002) # Basit bir katsayı modeli
toplam_kayip = buharlasma + cekilen_su

# 5. Dashboard Gösterimi
st.metric("Günlük Toplam Su Azalışı", f"{toplam_kayip:,.0f} m³")
st.write(f"Şu an Menderes'te sıcaklık {sicaklik}°C. Buharlaşma etkisi dahil edildi.")
