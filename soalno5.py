# Data jumlah peserta study group
study_groups = {
    ("Software Development", 20),
    ("UI/UX", 15),
    ("Technopreneur", 10),
    ("Intelligence System", 15)
}

# variabel acculumator
total_peserta = 0
jumlah_group = 0


# looping untuk menghitung total peserta
for group, peserta in study_groups:
    total_peserta += peserta
    jumlah_group += 1

rata_rata = total_peserta / jumlah_group

print("=== DATA PESERTA STUDY GROUP ===")
for group, peserta in study_groups:
    print(f"{group}: {peserta} peserta")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Total seluruh peserta        : {total_peserta} peserta")
print(f"Rata-rata peserta per group  : {rata_rata:.2f} peserta")