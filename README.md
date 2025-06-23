# 🧠 AI Diagnosis Penyakit (Flask + Random Forest)

Proyek ini merupakan **sistem diagnosis penyakit sederhana berbasis web** yang dikembangkan menggunakan Python (Flask) dan algoritma **Random Forest**. Pengguna dapat memilih gejala-gejala yang dialami, lalu sistem akan memprediksi jenis penyakit berdasarkan model klasifikasi yang telah dilatih.

## 📂 Fitur Utama

- Input data pasien (nama, tanggal lahir, alamat, telepon)
- Pemilihan gejala (checkbox)
- Prediksi penyakit berdasarkan Random Forest
- Informasi deskripsi penyakit, tingkat keparahan, pengobatan, dan obat
- Tampilan hasil diagnosis
- Fitur download hasil diagnosis dalam format **PDF dengan kop**
- Desain responsif dan modern

## 📊 Dataset

Dataset yang digunakan dalam proyek ini merupakan kumpulan data yang **dikompilasi secara mandiri dari berbagai sumber** publik dan referensi umum. Harap dicatat bahwa **beberapa informasi mungkin kurang akurat atau belum tervalidasi secara medis**.

Untuk penggunaan nyata atau sistem diagnosis berskala besar, sangat disarankan untuk:

- Menggunakan **dataset yang lebih lengkap dan tervalidasi**
- Melakukan **survei gejala dan penyakit sesuai kebutuhan medis atau klinis**
- Melibatkan tenaga ahli profesional di bidang kesehatan

> ⚠️ Proyek ini dibuat **sebagai contoh pembelajaran (educational purpose)**. Bukan sebagai pengganti diagnosis medis yang sesungguhnya.

## 📦 Teknologi yang Digunakan

- Python 3.x
- Flask
- Pandas
- scikit-learn (RandomForestClassifier)
- HTML + CSS + JS
- jsPDF + html2canvas (untuk download PDF)

## 📁 Struktur Proyek

AI_Diagnosis_Penyakit/
├── app.py
├── penyakit_umum_diperluas_final.xlsx
├── static/
│ ├── css/
│ │ └── style.css
│ ├── img/
│ │ └── kop.png
│ └── js/
│ └── script.js
├── templates/
│ ├── index.html
│ └── result.html
└── README.md

## 🚀 Cara Menjalankan

1. Pastikan Python sudah terinstal.
2. Install dependensi:
   ```bash
   pip install flask pandas scikit-learn openpyxl
    Jalankan aplikasi:
        python app.py
   👨‍💻 Pengembang
   Proyek ini dikembangkan oleh:
   Ahmad Adrian Wibisana
   Mahasiswa Politeknik Negeri Bengkalis
   ```
