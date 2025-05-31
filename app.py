# app.py

import streamlit as st
import numpy as np
import joblib

# Model ve scaler yükle
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🛍️ Online Retail Müşteri Segmentasyonu")

st.markdown("Müşterinin Recency, Frequency, Monetary bilgilerini girin:")

# Kullanıcı girişi
recency = st.number_input("Recency (Son alışveriş gün farkı)", min_value=0)
frequency = st.number_input("Frequency (Sipariş sayısı)", min_value=0)
monetary = st.number_input("Monetary (Toplam harcama)", min_value=0)

if st.button("Segmenti Tahmin Et"):
    input_data = np.array([[recency, frequency, monetary]])
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]
    st.success(f"🧠 Bu müşteri Segment {cluster} grubuna aittir.")
