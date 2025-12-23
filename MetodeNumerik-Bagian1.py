import numpy as np
import matplotlib.pyplot as plt
import time

def check_diag(A):
    """Cek syarat Dominan Diagonal Mutlak"""
    diag = np.abs(np.diag(A))
    off = np.sum(np.abs(A), axis=1) - diag
    if np.all(diag > off):
        print("[INFO] Matriks Dominan Diagonal (Konvergensi Dijamin).")
        return True
    print("[WARN] Matriks TIDAK Dominan Diagonal.")
    return False

def gauss_seidel(A, b, tol=1e-7, max_iter=50):
    n = len(b)
    x = np.zeros(n)
    history = []
    
    print(f"{'Iter':<6} {'I1':<10} {'I2':<10} {'I3':<10} {'Error':<10}")
    print("-" * 50)

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            # Sigma: jumlah a_ij * x_j selain diagonal
            sigma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - sigma) / A[i][i]
        
        err = np.linalg.norm(x - x_old, ord=np.inf)
        history.append(err)
        print(f"{k+1:<6} {x[0]:.6f}   {x[1]:.6f}   {x[2]:.6f}   {err:.2e}")
        
        if err < tol:
            return x, k+1, history
            
    return x, max_iter, history

# --- EKSEKUSI UTAMA ---
if __name__ == "__main__":
    # 1. Definisi Masalah (Rangkaian 3 Loop)
    A = np.array([[20.0, -5.0, 0.0], [-5.0, 15.0, -5.0], [0.0, -5.0, 20.0]])
    b = np.array([100.0, 0.0, 10.0])

    print("=== METODE GAUSS-SEIDEL: ANALISIS RANGKAIAN ===")
    check_diag(A)

    # 2. Proses Numerik
    start = time.time()
    solusi, iterasi, hist = gauss_seidel(A, b)
    durasi = time.time() - start

    # 3. Hasil & Validasi
    print(f"\n[HASIL] Waktu: {durasi:.5f} detik | Iterasi: {iterasi}")
    print(f"Arus I1: {solusi[0]:.8f} A")
    print(f"Arus I2: {solusi[1]:.8f} A")
    print(f"Arus I3: {solusi[2]:.8f} A")

    # Validasi dengan NumPy (Solusi Eksak)
    solusi_asli = np.linalg.solve(A, b)
    diff = np.abs(solusi - solusi_asli)
    print(f"[VALIDASI] Selisih vs NumPy: {np.max(diff):.2e}")

    # 4. Plot Grafik
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, len(hist)+1), hist, 'b-o', markersize=5)
    plt.yscale('log')
    plt.title('Konvergensi Gauss-Seidel (Skala Log)')
    plt.xlabel('Iterasi'); plt.ylabel('Error Relatif')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.show()