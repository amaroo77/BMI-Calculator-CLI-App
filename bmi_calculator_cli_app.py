# Project Name: BMI Calculator CLI App

# dapatkan input untuk tinggi dan berat
tinggi = float(input('Masukkan ketinggian anda dalam unit cm: ')) # setkan ke mod float untuk nombor perpuluhan
berat = float(input('Masukkan berat anda dalam unit kg: ')) # setkan ke mod float untuk nombor perpuluhan

# tukar unit tinggi dari cm ke meter (m)
tinggi = tinggi / 100

# Buat function BMI menggunakan formula BMI [berat (kg) / [Height (m)]^2]
def BMI(tinggi, berat):
    bmi = (berat / (tinggi**2))
    bmi = round(bmi, 1) # Tukar kepada 1 titik perpuluhan
    if (bmi < 18.5):
        return 'kurang berat badan.' , bmi
        
    elif (bmi >= 18.5 and bmi < 24.9):
        return 'mempunyai berat badan yang normal.' , bmi
        
    elif (bmi >= 25 and bmi < 29.9):
        return 'mempunyai berat badan berlebihan.' , bmi
        
    elif (bmi >= 30):
        return 'obesiti.' , bmi
    
quote, bmi = BMI(tinggi, berat) #quote berfungsi sebagai penyusun data yang akan dipanggil menggunakan {} mengikut urutan
print('\nBMI anda adalah: {}\nAnda {}'.format(bmi, quote))
