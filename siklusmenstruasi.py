from datetime import datetime, timedelta

def hitung_siklus_menstruasi_berikutnya(tanggal_awal_str, panjang_siklus):
    try:
        tanggal_awal = datetime.strptime(tanggal_awal_str, '%Y-%m-%d')
        tanggal_siklus_berikutnya = tanggal_awal + timedelta(days=panjang_siklus)
        return tanggal_siklus_berikutnya.strftime('%Y-%m-%d')
    except ValueError:
        return "Format tanggal tidak valid. Harap gunakan format 'YYYY-MM-DD'."
      
print("Pengecek Siklus Menstruasi")
tanggal_awal = input("Masukkan tanggal awal menstruasi terakhir Anda (YYYY-MM-DD): ")
panjang_siklus = int(input("Masukkan panjang rata-rata siklus dalam hari: "))
siklus_berikutnya = hitung_siklus_menstruasi_berikutnya(tanggal_awal, panjang_siklus)
print(f"Siklus menstruasi berikutnya diperkirakan mulai pada: {siklus_berikutnya}")