# Implementasi Algoritma Finite Difference (Selisih Hingga) 📐

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Tugas Mata Kuliah Metode Numerik** > Penerapan Turunan Numerik untuk Estimasi Kecepatan dan Percepatan Objek dari Data Posisi Diskrit.

---

## 👨‍💻 Identitas Penulis

| Nama | [cite_start]Muhammad Farhan Efendi [cite: 8] |
| :--- | :--- |
| **NIM** | [cite_start]21120123140181 [cite: 8] |
| **Departemen** | [cite_start]Teknik Komputer [cite: 9] |
| **Fakultas** | [cite_start]Fakultas Teknik [cite: 10] |
| **Universitas** | [cite_start]Universitas Diponegoro [cite: 11] |

---

## 📝 Deskripsi Proyek

[cite_start]Proyek ini bertujuan untuk menyelesaikan permasalahan dalam sistem pemantauan (seperti kendaraan otonom atau robotika) di mana sensor sering kali hanya memberikan **data posisi ($x$)** terhadap waktu ($t$) secara diskrit[cite: 16].

Karena fungsi analitik posisi tidak diketahui, turunan (kecepatan dan percepatan) tidak dapat dihitung secara langsung menggunakan kalkulus analitik. [cite_start]Oleh karena itu, digunakan **Metode Numerik Selisih Hingga (*Finite Difference*)** untuk mengestimasi nilai kecepatan ($v$) dan percepatan ($a$)[cite: 18, 20].

[cite_start]Tujuan akhir dari proyek ini adalah membandingkan hasil komputasi numerik dengan solusi eksak (teoritis) untuk memvalidasi akurasi algoritma[cite: 21].

---

## ⚙️ Metode yang Digunakan

[cite_start]Studi kasus ini menerapkan tiga skema pendekatan Turunan Numerik[cite: 24]:

1.  **Selisih Maju (*Forward Difference*)**
    * Digunakan pada **Batas Awal** data ($i=0$).
    * [cite_start]Rumus: $f'(x_i) \approx \frac{f(x_{i+1}) - f(x_i)}{h}$[cite: 27].
    * [cite_start]Error: $O(h)$[cite: 28].

2.  **Selisih Mundur (*Backward Difference*)**
    * Digunakan pada **Batas Akhir** data ($i=n$).
    * [cite_start]Rumus: $f'(x_i) \approx \frac{f(x_{i}) - f(x_{i-1})}{h}$[cite: 30].
    * [cite_start]Error: $O(h)$[cite: 31].

3.  **Selisih Pusat (*Central Difference*)**
    * Digunakan pada seluruh **Titik Interior** (tengah).
    * [cite_start]Metode ini dipilih sebagai prioritas karena memiliki akurasi lebih tinggi ($O(h^2)$) dibandingkan dua metode di atas[cite: 35].
    * [cite_start]Rumus: $f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2h}$[cite: 34].

---

## 🚀 Implementasi Kode

[cite_start]Program ditulis menggunakan **Python** dengan memanfaatkan teknik **Vectorization** (Slicing Array) dari pustaka NumPy untuk efisiensi komputasi, menghindari penggunaan *looping* konvensional untuk perhitungan data interior[cite: 116].

### Prasyarat
Install pustaka yang dibutuhkan:
```bash
pip install numpy matplotlib
