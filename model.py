import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

print("📂 Veriler yükleniyor...")






# CSV dosyasını oku
df = pd.read_csv("Online_Retail.csv", encoding="ISO-8859-1")

# InvoiceDate'i datetime formatına çevir
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Temizleme
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
df.dropna(inplace=True)

# Toplam harcama
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (df['InvoiceDate'].max() - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']
rfm = rfm[rfm['Monetary'] > 0]

print("📏 Ölçekleniyor...")
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

print("🤖 Model eğitiliyor...")
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(rfm_scaled)

print("💾 Model kaydediliyor...")
joblib.dump(kmeans, "kmeans_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model başarıyla kaydedildi.")
