Kondansatör (Sığaç) Hesaplayıcı
Bu proje, seri ve paralel bağlı kondansatörlerin (sığaçların) eşdeğer sığasını hesaplamak ve belirli bir eşdeğer değeri elde etmek için gereken kondansatör değerlerini bulmak amacıyla geliştirilmiş bir Python aracıdır.

Shutterstock

Özellikler
Bu script aşağıdaki temel fonksiyonları sunar:

Paralel Bağlantı Hesaplaması: Verilen kondansatör listesinin eşdeğer sığasını hesaplar.

Seri Bağlantı Hesaplaması: Verilen kondansatör listesinin eşdeğer sığasını hesaplar.

Tersine Hesaplama (Tasarım Modu): İstenilen bir eşdeğer sığa değeri ve elinizdeki adet sayısı girildiğinde, seri veya paralel bağlantı için birim kondansatör değerinin ne olması gerektiğini hesaplar.

Güvenli Giriş: Negatif veya sıfır (seri bağlantıda) değerlere karşı hata kontrolleri içerir.

Teorik Arkaplan

Shutterstock

Paralel Bağlantı

Paralel bağlı kondansatörlerde toplam sığa, bireysel sığaların toplamına eşittir. Gerilim her kolda aynıdır.

C 
eq
​	
 =C 
1
​	
 +C 
2
​	
 +⋯+C 
n
​	
 
Seri Bağlantı

Seri bağlı kondansatörlerde eşdeğer sığanın tersi, bireysel sığaların terslerinin toplamına eşittir.

C 
eq
​	
 
1
​	
 = 
C 
1
​	
 
1
​	
 + 
C 
2
​	
 
1
​	
 +⋯+ 
C 
n
​	
 
1
​	
 
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

Plaintext
Select option (1/2/q): 1
Series or Parallel? (s/p): p
Enter capacitor values (comma or space separated): 10 20 5.5
Equivalent capacitance in parallel: 35.5
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