
# Online Retail Müşteri Segmentasyonu

Bu proje, bir e-ticaret sitesinin müşteri verilerini kullanarak **K-Means kümeleme algoritmasıyla** müşteri segmentasyonu yapmayı amaçlar.

## 🔍 Kullanılan Veri Seti
- Online Retail Dataset (UCI / Kaggle)

https://archive.ics.uci.edu/dataset/352/online+retail

## ⚙️ Kullanılan Adımlar
1. Verilerin temizlenmesi
2. Müşteri bazlı özellik mühendisliği
3. Verilerin ölçeklenmesi
4. K-Means algoritmasıyla kümeleme
5. PCA ile görselleştirme

## 🧠 Kullanılan Kütüphaneler
- pandas
- numpy
- matplotlib
- sklearn

## 📊 Sonuç
Müşteriler farklı alışveriş davranışlarına göre gruplara ayrıldı. Bu segmentler, pazarlama stratejileri ve ürün önerileri için kullanılabilir.

## 🚀 Çalıştırmak için
```bash
pip install pandas numpy matplotlib scikit-learn
```

Notebook dosyasını açarak adımları çalıştırabilirsiniz
.
# 🛍️ Online Retail Müşteri Segmentasyonu

Bu proje, bir e-ticaret şirketinin müşteri verilerine dayanarak **K-Means algoritmasıyla müşteri segmentasyonu** yapar ve bunu kullanıcı arayüzü ile sunar. Kullanıcılar **RFM (Recency, Frequency, Monetary)** bilgilerini girerek hangi müşteri segmentine ait olduklarını görebilirler.

## 📁 Veri Seti
- **Kaynak:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- İçerik: Sipariş numarası, tarih, müşteri ID’si, ürün bilgisi ve fiyatlar

## ⚙️ Kullanılan Adımlar

1. Verilerin temizlenmesi (eksik değerler, negatif alışverişler)
2. **RFM (Recency, Frequency, Monetary)** değişkenlerinin hesaplanması
3. Verilerin ölçeklenmesi (`StandardScaler`)
4. **K-Means algoritmasıyla** segmentasyon
5. Modelin `.pkl` dosyası olarak kaydedilmesi
6. **Streamlit arayüzü** ile son kullanıcıya segment tahmini

## 🧠 Kullanılan Kütüphaneler

- `pandas`
- `numpy`
- `scikit-learn`
- `joblib`
- `streamlit`

## 💾 Dosyalar

| Dosya              | Açıklama                                  |
|--------------------|-------------------------------------------|
| `model.py`         | Verileri işler, RFM hesaplar ve modeli kaydeder |
| `kmeans_model.pkl` | Eğitilmiş K-Means modeli                  |
| `scaler.pkl`       | Verileri ölçeklemek için kullanılan nesne |
| `app.py`           | Streamlit arayüzü                         |
| `requirements.txt` | Projede kullanılan Python kütüphaneleri  |

## ▶️ Uygulamayı Çalıştırmak İçin

### 🔧 1. Gereksinimleri Kur:
```bash
pip install -r requirements.txt
📌 Örnek Kullanım
Kullanıcıdan şu bilgiler alınır:

Recency: Son alışverişten bu yana geçen gün sayısı

Frequency: Toplam alışveriş sayısı

Monetary: Toplam harcama

Model bu bilgilere göre müşteri segmentini tahmin eder:

🧠 Bu müşteri Segment 2 grubuna aittir.



🧪 Geliştirilebilir Alanlar
Elbow method ile en uygun küme sayısını dinamik belirleme

PCA veya t-SNE ile görsel segment analizi

Her segment için detaylı müşteri profili oluşturma

Streamlit'e segment özet bilgileri ekleme


📝 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Eğitim ve akademik amaçlarla serbestçe kullanılabilir.