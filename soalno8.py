# data peserta
peserta = [
    {"nama": "Alya", "status": "active", "kategori": "Web", "nilai": 85},
    {"nama": "Bima", "status": "active", "kategori": "Data", "nilai": 75},
    {"nama": "Citra", "status": "inactive", "kategori": "Web", "nilai": 90},
    {"nama": "Doni", "status": "active", "kategori": "Web", "nilai": 95},
    {"nama": "Eka", "status": "active", "kategori": "Data", "nilai": 80}
]

peserta_lolos = []


for p in peserta:
    if p["status"] == "active" and p["kategori"] == "Web" and p["nilai"] >= 80:
        peserta_lolos.append(p)


print("Peserta yang lolos penyaringan:")
for p in peserta_lolos:
    print(f"- {p['nama']} (Nilai: {p['nilai']})")