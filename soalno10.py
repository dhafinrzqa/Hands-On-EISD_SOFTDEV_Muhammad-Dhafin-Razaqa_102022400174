# Daftar peminjam
antrian_peminjam = [
    "Alya",
    "Bima",
    "Citra",
    "Doni",
    "Eka",
    "Farah"
]


stok_buku = 4

print("=== Simulasi Peminjaman Buku ===")


for nama in antrian_peminjam:
    if stok_buku > 0:
        print(f"{nama} berhasil meminjam buku.")
        stok_buku -= 1
    else:
        print(f"{nama} gagal meminjam buku (stok habis).")
        print("Simulasi dihentikan.")
        break


print("Sisa buku:", stok_buku)