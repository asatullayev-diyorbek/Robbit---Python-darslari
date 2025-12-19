import pyzipper
import itertools

def crack_zip_numeric(zip_path, min_len=4, max_len=7):
    with pyzipper.AESZipFile(zip_path) as zf:
        for length in range(min_len, max_len + 1):
            for pw_tuple in itertools.product("0123456789", repeat=length):
                password = ''.join(pw_tuple)
                print(f"Urinilmoqda: {password}")
                try:
                    zf.pwd = password.encode('utf-8')
                    zf.extractall()  # Parol to'g'ri bo'lsa, xatolik bo'lmaydi
                    print(f"\n[✅] Parol topildi: {password}")
                    return password
                except:
                    continue
        print("\n❌ Parol topilmadi.")
        return None

zip_file_path = "yakshanba fn2.zip"

crack_zip_numeric(zip_file_path)
