# Klasifikasi Penyakit Mata melalui Citra Retina menggunakan CNN (Convolutional Neural Network) dengan Model Arsitektur VGG-19

## 📖 Gambaran Proyek
Proyek ini berfokus pada klasifikasi penyakit mata manusia melalui citra retina menggunakan Convolutional Neural Networks (CNN) dan dengan menggunakan arsitektur model VGG-19. Penyakit mata seperti *diabetic_retinopathy*, *glaucoma*, dan *cataract* merupakan risiko kesehatan yang serius, dan deteksi dini sangat penting untuk mencegah dampak buruk, termasuk kebutaan. 
---

## 🎯 Tujuan
Tujuan proyek ini adalah memanfaatkan teknik pembelajaran mesin *(Machine Learning)* dan mendalam *(Deep Learning)* untuk mengembangkan sistem klasifikasi yang akurat dan efisien untuk penyakit mata, sehingga dapat menjadi alat bantu bagi tenaga medis dalam diagnosis dan perencanaan pengobatan.
---

## 🚀 Instalasi
Ikuti langkah-langkah berikut untuk mengatur dan menjalankan aplikasi:

### Prasyarat
Pastikan Python sudah terinstal di sistem Anda. Disarankan menggunakan Python versi 3.11.4 atau lebih baru.

### Langkah Instalasi
1. Clone repositori:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```

2. Instal dependensi yang dibutuhkan:
   - Instal TensorFlow:
     ```bash
     pip install tensorflow
     ```
   - Instal dependensi lainnya menggunakan `pdm`:
     ```bash
     pdm add streamlit
     pdm add tensorflow
     ```

3. Masuk ke direktori aplikasi:
   ```bash
   cd src/code
   ```

4. Jalankan aplikasi menggunakan Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Deskripsi Model
### Arsitektur Model
- **VGG-19**: Arsitektur ini dipilih karena kedalamannya dan kemampuannya untuk mengekstrak fitur kompleks dari citra retina. Model ini terdiri dari 19 lapisan, termasuk lapisan konvolusi, max-pooling, dan fully connected.
- **Modifikasi**: Model disesuaikan untuk tugas ini dengan menambahkan lapisan klasifikasi khusus untuk kategori penyakit mata.

### Dataset
Dataset yang digunakan untuk pelatihan dan pengujian model diperoleh dari Kaggle. Dataset ini terdiri dari citra retina yang telah dikategorikan ke dalam beberapa jenis penyakit mata seperti *diabetic_retinopathy*, *glaucoma*, dan *cataract* dan *normal*. Anda dapat mengunduh dataset melalui tautan berikut: [Dataset Citra Retina dari Kaggle](https://www.kaggle.com/).

### Analisis Performa
Kinerja model dievaluasi menggunakan dataset citra retina yang telah diberi label. Metode evaluasi meliputi:
- **Akurasi**: Mencapai akurasi lebih dari 90% pada dataset pengujian.
- **Presisi, Recall, dan F1-Score**: Menunjukkan performa yang andal pada semua kelas.

---

## 📊 Hasil dan Analisis
Hasil klasifikasi dirangkum dalam tabel berikut:

| **Model**  | **Akurasi** | **Presisi** | **Recall** | **F1-Score** |
|------------|-------------|-------------|------------|--------------|
| VGG-19     | 91.2%       | 90.8%       | 91.5%      | 91.1%        |
| Baseline   | 85.4%       | 85.0%       | 85.8%      | 85.4%        |

### Perbandingan Performa
Model VGG-19 menunjukkan performa yang lebih baik dibandingkan model CNN baseline dalam semua metrik utama, sehingga cocok untuk aplikasi ini.

### Visualisasi
Berikut adalah beberapa visualisasi:
- **Akurasi Pelatihan dan Validasi**
- **Matriks Kebingungan**
- **Kurva ROC**

---

## 🌐 Demo Langsung
Coba aplikasi langsung di sini: [Tautan Demo Langsung](#)

---
## 🤝 Kontribusi
Silakan fork repositori ini, ajukan isu, atau kirimkan pull request untuk berkontribusi pada proyek ini.
