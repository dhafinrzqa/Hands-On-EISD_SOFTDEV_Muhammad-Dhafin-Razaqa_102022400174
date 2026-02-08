# ata pendaftar
pendaftar = [
    {"nama": "Alya", "status": "active", "nilai": 85 },
    {"nama": "Bima", "status": "inactive", "nilai": 90 },
    {"nama": "Citra", "status": "active", "nilai": 70 },
    {"nama": "Doni", "status": "active", "nilai": 95 },
    {"nama": "Eka", "status": "inactive", "nilai": 60 }
]

hasil = []

for p in pendaftar:
    if p["status"] == "active" and p["nilai"] >= 80:
        data_baru = {
            "nama": p["nama"],
            "nilai": p["nilai"]
        }
        hasil.append(data_baru)


print(hasil)

