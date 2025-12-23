import numpy as np
import matplotlib.pyplot as plt

def get_analytical(t):
    """Mengembalikan nilai eksak posisi, kecepatan, dan percepatan."""
    x = 2*t**3 - 5*t**2 + 3*t       # Posisi
    v = 6*t**2 - 10*t + 3           # Kecepatan
    a = 12*t - 10                   # Percepatan
    return x, v, a

def numerical_diff(t, x):
    """Menghitung turunan numerik menggunakan Finite Difference."""
    h = t[1] - t[0]
    v = np.zeros_like(x)
    a = np.zeros_like(x)

    # --- 1. Kecepatan (v) ---
    # Interior: Selisih Pusat (Central)
    v[1:-1] = (x[2:] - x[:-2]) / (2*h)
    # Batas: Selisih Maju & Mundur
    v[0]  = (x[1] - x[0]) / h
    v[-1] = (x[-1] - x[-2]) / h

    # --- 2. Percepatan (a) ---
    # Interior: Selisih Pusat Orde 2
    a[1:-1] = (x[2:] - 2*x[1:-1] + x[:-2]) / h**2
    # Batas: Turunan dari v (Selisih Maju & Mundur)
    a[0]  = (v[1] - v[0]) / h
    a[-1] = (v[-1] - v[-2]) / h

    return v, a

# --- MAIN PROGRAM ---
# Setup Data
t = np.linspace(0, 4, 21)
x_exact, v_exact, a_exact = get_analytical(t)

# Proses Numerik
v_num, a_num = numerical_diff(t, x_exact)

# Hitung Error (MAE)
mae_v = np.mean(np.abs(v_exact - v_num))
mae_a = np.mean(np.abs(a_exact - a_num))

print(f"Step size (h): {t[1]-t[0]:.2f}")
print(f"MAE Kecepatan: {mae_v:.6f} | MAE Percepatan: {mae_a:.6f}")

# Visualisasi Compact
fig, ax = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Plot Posisi
ax[0].plot(t, x_exact, 'o-', label='Posisi (Input)')
ax[0].set_ylabel('Posisi (m)'); ax[0].grid(True); ax[0].legend()
ax[0].set_title('Analisis Kinematika Numerik')

# Plot Kecepatan
ax[1].plot(t, v_exact, 'g-', label='Eksak')
ax[1].plot(t, v_num, 'rx--', label='Numerik')
ax[1].set_ylabel('Kecepatan (m/s)'); ax[1].grid(True); ax[1].legend()

# Plot Percepatan
ax[2].plot(t, a_exact, 'purple', label='Eksak')
ax[2].plot(t, a_num, 'orange', ls='--', marker='x', label='Numerik')
ax[2].set_ylabel('Percepatan (m/s²)'); ax[2].grid(True); ax[2].legend()
ax[2].set_xlabel('Waktu (s)')

plt.tight_layout()
plt.show()