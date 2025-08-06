# /opt/hokage-bot/config.py (Versi Baru)

import os
import logging

# Fungsi untuk membaca environment variable dan mengubahnya menjadi set of integers
def get_admin_ids():
    admin_ids_str = os.getenv("ADMIN_IDS", "")
    if not admin_ids_str:
        logging.warning("ADMIN_IDS tidak diatur di environment. Tidak akan ada user admin.")
        return set()
    
    try:
        # Mengubah string "123,456" menjadi {123, 456}
        return {int(admin_id.strip()) for admin_id in admin_ids_str.split(',')}
    except ValueError:
        logging.error("Format ADMIN_IDS salah. Harap gunakan angka yang dipisah koma. Cth: 12345,67890")
        return set()

# Membaca variabel dari file .env yang dimuat oleh systemd
BOT_TOKEN = os.getenv("BOT_TOKEN")
KMSP_API_KEY = os.getenv("KMSP_API_KEY")
ADMIN_IDS = get_admin_ids()

# Lakukan pengecekan saat startup
if not BOT_TOKEN:
    logging.critical("FATAL ERROR: BOT_TOKEN tidak ditemukan di environment.")
    # Anda bisa menambahkan sys.exit(1) di sini jika ingin bot berhenti total
    
if not ADMIN_IDS:
    logging.warning("PERINGATAN: Tidak ada ADMIN_IDS yang dikonfigurasi.")
