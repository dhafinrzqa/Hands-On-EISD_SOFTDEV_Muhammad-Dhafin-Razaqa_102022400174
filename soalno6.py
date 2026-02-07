# Data email peserta
email = [
    "Andi@gmail.com",
    "Budi@gmail.com",
    "Sari@gmail.com",
    "Andi@gmail.com",
    "Rina@gmail.com",
    "Budi@gmail.com"
]

email_count = {}

for email in email:
    email_count[email] = email_count.get(email, 0) + 1


print("Daftar email duplikat:")
for email, count in email_count.items():
    if count > 1:
        print(f"- {email} (muncul {count} kali)")
