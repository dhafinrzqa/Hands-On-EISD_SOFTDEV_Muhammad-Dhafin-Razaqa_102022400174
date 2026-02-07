def cek_study_group(data):
    tersedia = []
    penuh = []

    for group in data:
        nama = group["nama"]
        kuota = group["kuota"]
        terdaftar = group["terdaftar"]

        if terdaftar < kuota:
            tersedia.append(nama)
        else:
            penuh.append(nama)

    return tersedia, penuh

# Data Pendaftar Study Group 
study_group = [
    {"nama": "Software Development", "kuota": 20, "terdaftar": 18},
    {"nama": "UI/UX Design", "kuota": 15, "terdaftar": 15},
    {"nama": "Technopreneur", "kuota": 25, "terdaftar": 10},
    {"nama": "Intelligence System", "kuota": 10, "terdaftar": 10}
]

# call function
tersedia, penuh = cek_study_group(study_group)

print("Study Group yang masih tersedia:")
for sg in tersedia:
    print("-", sg)

print("\nStudy Group yang sudah penuh:")
for sg in penuh:
    print("-", sg)