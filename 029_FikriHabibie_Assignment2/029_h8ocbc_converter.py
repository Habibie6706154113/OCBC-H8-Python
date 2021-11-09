def convert_cel_and_kel(val, type):
    '''
    Mengkonversi suhu dari Celsius ke Kelvin atau Kelvin ke Celsius
    :param val: Input angka Suhu | int or float
    :param type: Input Jenis Suhu untuk menentukan konversi suhu dari Celsius atau Kelvin | string 
    
    :return Suhu dalam Celsius atau Kelvin
    '''
    if(type == 'c'):
        res = val + 273.15
    else:
        res = val - 273.15
    return round(res, 3)

def convert_to_fahr(val, type):
    '''
    Mengkonversi suhu dari Celsius ke Fahrenheit atau Kelvin ke Fahrenheit
    :param val: Input angka Suhu | int or float
    :param type: Input Jenis Suhu untuk menentukan konversi suhu dari Celsius atau Kelvin | string 
    
    :return Suhu dalam Fahrenheit
    '''
    if(type == 'c'):
        cel = val * 9 / 5 + 32
        res = '\nCelsius: {} to Fahrenheit: {}'.format(val, round(cel, 3))
    else:
        kel = (convert_cel_and_kel(val, type) * 9 / 5) + 32
        res = '\nKelvin: {} to Fahrenheit: {}'.format(val, round(kel, 3))
    return res

def convert_from_fahr(val):
    '''
    Mengkonversi suhu dari Fahrenheit ke Celsius dan Kelvin sekaligus
    :param val: Input angka Suhu | int or float
    
    :return Suhu dalam Celsius dan Kelvin sekaligus
    '''
    cel = (val - 32) * 5 / 9
    kel = cel + 273.15
    return "Fahrenheit: {} to Celsius: {} & Fahrenheit: {} to Kelvin: {}".format(val, round(cel, 3), val, round(kel, 3))

while(True):
    try:
        print("\n== Konversi Suhu ==\n")
        print("Pilihan: ")
        print("1. Celsius ke Kelvin / Kelvin ke Celsius")
        print("2. Celsius ke Fahrenheit / Kelvin ke Fahrenheit")
        print("3. Fahrenheit ke (Celsius & Kelvin)")
        print("0. Exit\n")
        pilih = int(input("Masukkan Pilihan: "))

        if(pilih == 1):
            print("\nTolong masukkan angka dan jenis suhu yang akan dikonversi")
            jenis = input("Jenis Suhu (c/k): ").lower()

            if(jenis != 'c' and jenis != 'k'):
                print("\nMasukkan jenis c atau k saja pada pilihan 1")
                continue

            angka = int(input('Masukkan angka: '))

            if(jenis == 'c'):
                print("\nCelsius: {} to Kelvin: {}".format(angka, convert_cel_and_kel(angka, jenis)))
            else:
                print("\nCelsius: {} to Kelvin: {}".format(angka, convert_cel_and_kel(angka, jenis)))
            
        elif(pilih == 2):
            print("\nTolong masukkan angka dan jenis suhu yang akan dikonversi")
            jenis = input("Jenis Suhu (c/k): ").lower()

            if(jenis != 'c' and jenis != 'k'):
                print("\nMasukkan jenis c atau k saja pada pilihan 2")
                continue
        
            angka = int(input('Masukkan angka: '))

            print('\n' + convert_to_fahr(angka, jenis))
    
        elif(pilih == 3):
            print("\nTolong masukkan angka yang akan dikonversi")
            angka = int(input('Masukkan angka: '))

            print("\n" + convert_from_fahr(angka))

        elif(pilih == 0):
            break
    
        else:
            print("\nPilihan yang dimasukkan tidak tersedia, silahkan masukkan pilihan yang tersedia di menu")

    except ValueError:
        print("\nMasukkan pilihan berupa angka")

print('\nTerimakasih telah menjalankan program ini :)')
