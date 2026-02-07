def status_pendaftaran(kuota, terdaftar):
    if terdaftar < kuota - 3:
        return "Pendaftaran diterima"
    elif terdaftar < kuota:
        return "Hampir penuh"
    elif terdaftar == kuota:
        return "Pendaftaran ditutup"
    else:
        return "Pendafraran ditolak"
    

# input dari user
kuota = int(input("Masukkan kuota maksimal: "))
terdaftar = int(input("Masukkan jumlah peserta terdaftar: "))

# menampilkan hasil
status = status_pendaftaran(kuota, terdaftar)
print("Status pendafraran:", status)


