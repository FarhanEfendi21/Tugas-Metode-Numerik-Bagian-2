# Implementasi Algoritma Finite Difference (Selisih Hingga) 📐

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Tugas Mata Kuliah Metode Numerik** > Penerapan Turunan Numerik untuk Estimasi Kecepatan dan Percepatan Objek dari Data Posisi Diskrit.

---

## 👨‍💻 Identitas Penulis

| Nama | Muhammad Farhan Efendi |
| :--- | :--- |
| **NIM** | 21120123140181 |
| **Departemen** | Teknik Komputer |
| **Fakultas** | Fakultas Teknik |
| **Universitas** | Universitas Diponegoro |

---

## 📝 Deskripsi Proyek

Proyek ini bertujuan untuk menyelesaikan permasalahan dalam sistem pemantauan (seperti kendaraan otonom atau robotika) di mana sensor sering kali hanya memberikan **data posisi (x)** terhadap waktu (t) secara diskrit.

Karena fungsi analitik posisi tidak diketahui, turunan (kecepatan dan percepatan) tidak dapat dihitung secara langsung menggunakan kalkulus analitik. [cite_start]Oleh karena itu, digunakan **Metode Numerik Selisih Hingga (*Finite Difference*)** untuk mengestimasi nilai kecepatan (v) dan percepatan (a).

Tujuan akhir dari proyek ini adalah membandingkan hasil komputasi numerik dengan solusi eksak (teoritis) untuk memvalidasi akurasi algoritma.

---

## ⚙️ Metode yang Digunakan

Studi kasus ini menerapkan tiga skema pendekatan Turunan Numerik:

1.  **Selisih Maju (*Forward Difference*)**
    * Digunakan pada **Batas Awal** data ($i=0$).
    * Rumus: $f'(x_i) \approx \frac{f(x_{i+1}) - f(x_i)}{h}$.
    * Error: $O(h)$.

2.  **Selisih Mundur (*Backward Difference*)**
    * Digunakan pada **Batas Akhir** data ($i=n$).
    * Rumus: $f'(x_i) \approx \frac{f(x_{i}) - f(x_{i-1})}{h}$.
    * Error: $O(h)$[cite: 31].

3.  **Selisih Pusat (*Central Difference*)**
    * Digunakan pada seluruh **Titik Interior** (tengah).
    * Metode ini dipilih sebagai prioritas karena memiliki akurasi lebih tinggi (O(h^2)) dibandingkan dua metode di atas.
    * Rumus: $f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2h}$.

---

## 🚀 Implementasi Kode

Program ditulis menggunakan **Python** dengan memanfaatkan teknik **Vectorization** (Slicing Array) dari pustaka NumPy untuk efisiensi komputasi, menghindari penggunaan *looping* konvensional untuk perhitungan data interior.

### Prasyarat
Install pustaka yang dibutuhkan:
```bash
pip install numpy matplotlib
