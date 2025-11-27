Kondansatör (Sığaç) Hesaplayıcı
Bu proje, seri ve paralel bağlı kondansatörlerin (sığaçların) eşdeğer sığasını hesaplamak ve belirli bir eşdeğer değeri elde etmek için gereken kondansatör değerlerini bulmak amacıyla geliştirilmiş bir Python aracıdır.

[Shutterstock](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcS8zjRFV53BaJbbXSL3i1c8c3PqGWIbj5__blm_jlIijBrAgR-ba9cNwXRQ-S8UaM9QlucfvUicI9LnQp7OYEh1BnAzoDnasqdnbaYGrAPbof54MlQ)<img width="3999" height="3999" alt="image" src="https://github.com/user-attachments/assets/872dab39-f60c-45dc-be88-d2c11ceabfb3" />


Özellikler
Bu script aşağıdaki temel fonksiyonları sunar:

Paralel Bağlantı Hesaplaması: Verilen kondansatör listesinin eşdeğer sığasını hesaplar.

Seri Bağlantı Hesaplaması: Verilen kondansatör listesinin eşdeğer sığasını hesaplar.

Tersine Hesaplama (Tasarım Modu): İstenilen bir eşdeğer sığa değeri ve elinizdeki adet sayısı girildiğinde, seri veya paralel bağlantı için birim kondansatör değerinin ne olması gerektiğini hesaplar.

Güvenli Giriş: Negatif veya sıfır (seri bağlantıda) değerlere karşı hata kontrolleri içerir.

Teorik Arkaplan

[Shutterstock](https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQy9xbjQHDAPk0xtppGCdjza2kkdeyeHHYDB57AS8wHioXmYktvSHY5NVbz2Ah64-YNaUNNJ8LWj6NMDjg5SyEWWWHj7moyhspaYIns-Rag9OtxrVY)<img width="3999" height="2689" alt="image" src="https://github.com/user-attachments/assets/726d1778-9408-4aae-9015-270dc921a412" />


Paralel Bağlantı

Paralel bağlı kondansatörlerde toplam sığa, bireysel sığaların toplamına eşittir. Gerilim her kolda aynıdır.
<img width="269" height="57" alt="image" src="https://github.com/user-attachments/assets/b6192fad-a7a8-4224-8615-03f2d448c7d0" />

Seri Bağlantı

Seri bağlı kondansatörlerde eşdeğer sığanın tersi, bireysel sığaların terslerinin toplamına eşittir.

<img width="269" height="57" alt="image" src="https://github.com/user-attachments/assets/3e492ac9-cf8f-45e8-abd9-acdcff28f869" />

 
Kurulum ve Çalıştırma
Bu proje herhangi bir harici kütüphane (pip install gerektirmez) kullanmaz. Standart Python 3 kurulumu yeterlidir.

Dosyayı indirin (örneğin main.py olarak kaydedin).

Terminal veya komut satırını açın.

Aşağıdaki komutla çalıştırın:

Bash
python main.py

Kullanım Örnekleri
Program çalıştırıldığında interaktif bir menü sunar:

1. Eşdeğer Sığa Hesaplama

Birden fazla kondansatörünüz var ve toplam sığayı merak ediyorsunuz:

<img width="732" height="226" alt="image" src="https://github.com/user-attachments/assets/84efe671-6c68-47a3-a6c7-643aae5c8a96" />

2. Bileşen Değeri Belirleme

Bir devre tasarlıyorsunuz, 10μF elde etmeniz gerek ama elinizde sadece birbirinin aynısı 4 adet kondansatör kullanabileceğiniz bir yerleşim (footprint) var:

Plaintext
Select option (1/2/q): 2
Enter required equivalent capacitance: 10
Enter number of identical capacitors: 4
To get 10.0 (with 4 identical capacitors):
 - per capacitor (parallel): 2.5
 - per capacitor (series): 40.0
Yorum: 4 adet 2.5 birimlik kondansatörü paralel bağlarsanız veya 4 adet 40 birimlik kondansatörü seri bağlarsanız 10 birim elde edersiniz.

Geliştirici Notları
Kod içerisinde doctest modülü bulunmaktadır. Testleri çalıştırmak için dosyayı çalıştırırken -v parametresini ekleyebilirsiniz (Python modül çalışma mantığına göre düzenleme gerekebilir).

Tip ipuçları (Type Hints) from __future__ import annotations kullanılarak modern Python standartlarına uygun yazılmıştır.
