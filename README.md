# BMI-Calculator-CLI-App
# 📊 Kalkulator Ringkas BMI (CLI)

Sebuah aplikasi mudah jenis Command Line Interface (CLI) untuk mengira Indeks Jisim Badan (BMI) berdasarkan ketinggian dan berat pengguna. Dibina menggunakan Python.

---

## 🎯 Tujuan

- Mengetahui kategori BMI anda berdasarkan input tinggi dan berat
- Projek asas Python untuk latihan fungsi, input/output, dan pengiraan formula

---

## ⚙️ Ciri-ciri

- Input tinggi dalam **cm** dan berat dalam **kg**
- Penukaran unit tinggi kepada meter
- Formula BMI:
  
  \[
  BMI = \frac{berat}{(tinggi / 100)^2}
  \]

- Kategori BMI berdasarkan nilai:
  | BMI       | Kategori                |
  |-----------|-------------------------|
  | < 18.5    | Kurang berat badan      |
  | 18.5–24.9 | Berat badan normal      |
  | 25–29.9   | Berat badan berlebihan  |
  | ≥ 30      | Obesiti                 |

---

## 🚀 Cara Guna

### Keperluan:
- Python 3.x
- Terminal / Command Prompt

### Langkah-langkah:
```bash
# 1. Muat turun fail
git clone https://github.com/nama-pengguna/kalkulator-bmi

# 2. Masuk ke folder
cd kalkulator-bmi

# 3. Jalankan program
python kalkulator_BMI.py
📷 Contoh Output
bash
Copy
Edit
Masukkan ketinggian anda dalam unit cm: 165
Masukkan berat anda dalam unit kg: 60

BMI anda adalah: 22.0
Anda mempunyai berat badan yang normal.
📁 Struktur Projek
bash
Copy
Edit
kalkulator-bmi/
│
├── kalkulator_BMI.py   # Kod utama
└── README.md           # Dokumentasi projek
