#Program menghitung nilai rata-rata dari nilai yang diinput

total = 0
cacah = 0
data = int(input("Masukkan nilai (0 = selesai): "))

while data != 0:
    total += data
    cacah +=1
    data = int(input("Masukkan nilai (0 = selesai): "))

rerata = total/cacah

print("Nilai rata-rata: ", rerata)