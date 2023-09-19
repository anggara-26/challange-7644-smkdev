# Mengambil input dari user dan memasukkan ke variabel 'n'
n = int(input("Masukkan series: "))
# Menampung jawaban dalam variabel 'ans'
ans = 0

# Melakukan looping sebanyak n-kali
for i in range(1, n+1):
  # Menambah value dari variabel ans dengan 2 sebanyak 'i' kali misal: 222
  ans += int("2"*i)

print(ans)