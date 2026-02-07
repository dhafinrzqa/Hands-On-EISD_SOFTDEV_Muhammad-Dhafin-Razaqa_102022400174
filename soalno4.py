def validasi_data(nama, email, divisi_study_group, jumlah_terdaftar):
    if nama.strip() == "":
       return "Data tidak valid"
    
    if email.strip() == "" or "@" not in email:
        return "Data tidak valid"
    
    if divisi_study_group.strip() == "":
        return "Data tidak valid"
    
    if not isinstance(jumlah_terdaftar, int) or jumlah_terdaftar < 1:
        return "Data tidak valid"
    
    return "Data valid"


# input data dari user
nama = input("Nama: ")
email = input("Email: ")
divisi_study_group = input("Divisi Study Group: ")

try:
    jumlah_terdaftar = int(input("Masukkan jumlah peserta terdaftar: "))
except ValueError:
    jumlah_terdaftar = 0

hasil = validasi_data(nama, email, divisi_study_group, jumlah_terdaftar)
print(hasil)
