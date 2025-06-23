from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os
from datetime import datetime

app = Flask(__name__)

# ===== Load Dataset dan Model =====
DATA_PATH = 'penyakit_umum_diperluas_final.xlsx'
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset tidak ditemukan: {DATA_PATH}")

df = pd.read_excel(DATA_PATH)
df["all_symptoms"] = df[["Gejala 1", "Gejala 2", "Gejala 3", "Gejala 4", "Gejala 5"]].values.tolist()

mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df["all_symptoms"])

le = LabelEncoder()
y = le.fit_transform(df["Penyakit"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ===== Route Halaman Utama =====
@app.route('/')
def index():
    symptoms = list(mlb.classes_)
    return render_template('index.html', symptoms=symptoms)

# ===== Route Diagnosa dan Hasil =====
@app.route('/diagnose', methods=['POST'])
def diagnose():
    # Ambil gejala yang dipilih
    selected_symptoms = request.form.getlist('symptoms')
    if not selected_symptoms:
        return render_template('result.html', error="❌ Harap pilih setidaknya satu gejala.", result=None)

    # Ambil data pasien
    nama = request.form.get('nama')
    lahir = request.form.get('lahir')
    alamat = request.form.get('alamat')
    telepon = request.form.get('telepon')

    # Prediksi penyakit
    X_input = mlb.transform([selected_symptoms])
    predicted = model.predict(X_input)
    predicted_label = le.inverse_transform(predicted)[0]
    info = df[df["Penyakit"] == predicted_label].iloc[0]

    # Data hasil
    result = {
        'penyakit': predicted_label,
        'deskripsi': info['Deskripsi'],
        'keparahan': info['Tingkat Keparahan'],
        'pengobatan': info['Pengobatan Awal'],
        'obat': info['Obat yang Disarankan'],
        'gejala': selected_symptoms,
        'nama': nama,
        'lahir': lahir,
        'alamat': alamat,
        'telepon': telepon,
        'tanggal': datetime.now().strftime('%d-%m-%Y'),
        'waktu': datetime.now().strftime('%H:%M')
    }

    return render_template('result.html', result=result, error=None)

if __name__ == '__main__':
    app.run(debug=True)
