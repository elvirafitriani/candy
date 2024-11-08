import requests

# Baca file email.txt dan pisahkan email dan password
with open('email.txt', 'r') as file:
    for line in file:
        email, password = line.strip().split(';')

        # URL API dan payload
        url = "https://api.candy-land.club/api/user/register?lang=id"
        payload = {
            "email": email,
            "kata sandi masuk": password,
            "kata sandi keamanan": password,  # Sandi keamanan sama dengan sandi masuk
            "referral_code": "849205"  # Kode referal 
        }
        headers = {
            "Content-Type": "application/json"  # Pastikan tipe konten sudah benar
        }

        # Kirim POST request
        response = requests.post(url, json=payload, headers=headers)

        # Cek status kode untuk konfirmasi registrasi
        if response.status_code == 200:
            print(f"Registrasi berhasil untuk {email}")
        else:
            print(f"Registrasi gagal untuk {email} dengan status code: {response.status_code}")
            print(f"Response: {response.text}")  # Tampilkan response error untuk debugging
