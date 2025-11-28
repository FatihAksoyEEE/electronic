def calculate_voltage(): # Gerilim hesaplama fonksiyonu
    try:
        current = float(input("Akım (I) değerini girin (Amper): "))
        resistance = float(input("Direnç (R) değerini girin (Ohm): "))
        voltage = current * resistance
        print(f"Gerilim (V) = {voltage:.2f} Volt")
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal değerler girin.")
 
def calculate_current(): # Akım hesaplama fonksiyonu
    try:
        voltage = float(input("Gerilim (V) değerini girin (Volt): "))
        resistance = float(input("Direnç (R) değerini girin (Ohm): "))
        if resistance == 0:
            print("Direnç sıfır olamaz. Akım tanımsızdır.")
        else:
            current = voltage / resistance
            print(f"Akım (I) = {current:.2f} Amper")
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal değerler girin.")
 
def calculate_resistance(): # Direnç hesaplama fonksiyonu
    try:
        voltage = float(input("Gerilim (V) değerini girin (Volt): "))
        current = float(input("Akım (I) değerini girin (Amper): "))
        if current == 0:
            print("Akım sıfır olamaz. Direnç tanımsızdır.")
        else:
            resistance = voltage / current
            print(f"Direnç (R) = {resistance:.2f} Ohm")
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal değerler girin.")
 
def calculate_power(): # Güç hesaplama fonksiyonu
    try:
        print("Güç (P) hesaplamak için hangi değerleri kullanmak istersiniz?")
        print("1. Gerilim (V) ve Akım (I)")
        print("2. Akım (I) ve Direnç (R)")
        print("3. Gerilim (V) ve Direnç (R)")
        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == '1':
            voltage = float(input("Gerilim (V) değerini girin (Volt): "))
            current = float(input("Akım (I) değerini girin (Amper): "))
            power = voltage * current
            print(f"Güç (P) = {power:.2f} Watt")
        elif choice == '2':
            current = float(input("Akım (I) değerini girin (Amper): "))
            resistance = float(input("Direnç (R) değerini girin (Ohm): "))
            power = current**2 * resistance
            print(f"Güç (P) = {power:.2f} Watt")
        elif choice == '3':
            voltage = float(input("Gerilim (V) değerini girin (Volt): "))
            resistance = float(input("Direnç (R) değerini girin (Ohm): "))
            if resistance == 0:
                print("Direnç sıfır olamaz. Güç tanımsızdır.")
            else:
                power = voltage**2 / resistance
                print(f"Güç (P) = {power:.2f} Watt")
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal değerler girin.")

def main():
    while True:
        print("\n--- Ohm Kanunu ve Güç Hesaplayıcı ---")
        print("1. Gerilim (V) Hesapla")
        print("2. Akım (I) Hesapla")
        print("3. Direnç (R) Hesapla")
        print("4. Güç (P) Hesapla")
        print("5. Çıkış")

        choice = input("Yapmak istediğiniz işlemi seçin (1-5): ")

        if choice == '1':
            calculate_voltage()
        elif choice == '2':
            calculate_current()
        elif choice == '3':
            calculate_resistance()
        elif choice == '4':
            calculate_power()
        elif choice == '5':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir sayı girin.")

if __name__ == "__main__":
    main()
