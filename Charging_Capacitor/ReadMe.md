RC Zaman Sabiti ve Kondansatör Şarjı
Bu proje, bir RC (Direnç-Kapasitör) devresinin zaman sabiti (τ), şarj/deşarj karakteristikleri, kesim frekansı ve yükselme süresi hesaplamaları hakkında temel bilgiler ve formüller içerir.

Shutterstock
Keşfet

RC Zaman Sabiti Nedir?
RC zaman sabiti (küçük τ harfi ile gösterilir), bir direnç-kapasitör devresinin (RC devresi) karakteristik tepki süresini belirler. Devre direnci ile devre kapasitansının çarpımına eşittir:

τ=R⋅C
Uluslararası Birim Sistemi (SI) kullanıldığında:

R: Ohm (Ω)

C: Farad (F)

τ: Saniye (s) cinsindendir.

Fiziksel Anlamı

Zaman sabiti (τ), şunları ifade eder:

Şarj: Kondansatörün uygulanan DC voltajın yaklaşık %63.2'sine kadar şarj olması için gereken süre.

Deşarj: Kondansatörün başlangıç voltajının yaklaşık %36.8'ine kadar deşarj olması için gereken süre.

Bu değerler, matematiksel sabit e'den (Euler sayısı) türetilmiştir:

1−e 
−1
 ≈0.632 (%63.2)

e 
−1
 ≈0.368 (%36.8)

Şarj ve Deşarj Denklemleri

Shutterstock
Keşfet

1. Kondansatörün Deşarjı

V 
0
​	
  başlangıç gerilimine sahip bir kondansatörün, seri bir direnç üzerinden sıfır volta deşarj olması durumunda voltajın zamana göre değişimi şu şekildedir:

V 
C
​	
 (t)=V 
0
​	
 ⋅(e 
−t/τ
 )
2. Kondansatörün Şarjı

Boş bir kondansatörün, seri bir direnç üzerinden sabit bir V 
0
​	
  giriş gerilimine şarj edilmesi durumunda voltaj değişimi şu şekildedir:

V 
C
​	
 (t)=V 
0
​	
 ⋅(1−e 
−t/τ
 )
Not: Bu eğri, deşarj eğrisinin dikey olarak yansıtılmış halidir.

Kesim Frekansı (Cutoff Frequency)
Zaman sabiti τ, RC devresinin kesim frekansı (f 
c
​	
 ) ile doğrudan ilişkilidir.

τ=RC= 
2πf 
c
​	
 
1
​	
 ≈ 
f 
c
​	
 
0.159
​	
 
Veya frekans cinsinden ifade edilirse:

f 
c
​	
 = 
2πRC
1
​	
 = 
2πτ
1
​	
 ≈ 
τ
0.159
​	
 
Açısal Frekans (ω 
c
​	
 ): Kesim frekansı açısal frekans olarak ifade edildiğinde (ω 
c
​	
 =2πf 
c
​	
 ), zaman sabitinin tersine eşittir.

Birden fazla direnç ve/veya kondansatör içeren karmaşık devrelerde, kesim frekansını tahmin etmek için açık devre zaman sabiti yöntemi (open-circuit time constant method) kullanılabilir.

Yükselme Süresi (Rise Time)
Bir RC devresine bağlı yükselme süresi, zaman sabiti ile orantılıdır:

Aralık	Formül (τ)	Formül (f 
c
​	
 )
%20'den %80'e	t 
r
​	
 ≈1.4τ	t 
r
​	
 ≈ 
f 
c
​	
 
0.22
​	
 
%10'dan %90'a	t 
r
​	
 ≈2.2τ	t 
r
​	
 ≈ 
f 
c
​	
 
0.35
​	
 
Örnek Hesaplama
Aşağıdaki değerlere sahip bir devre düşünelim:

Direnç (R): 1 MΩ (1.000.000Ω)

Kapasitans (C): 1μF (0.000001F)

Başlangıç Voltajı (V 
0
​	
 ): 1 V

Hesaplamalar:

Zaman Sabiti (τ):

τ=1.000.000Ω×0.000001F=1 Saniye
Kesim Frekansı: Bu τ değeri, yaklaşık 159 mHz (milihertz) veya 1 rad/s kesim frekansına karşılık gelir.

Deşarj Durumu: 1 saniye (1τ) sonra kondansatörün voltajı:

V 
C
​	
 (1)≈0.368×1V=368 mV
Geometrik Yorum: V(t) voltaj eğrisinin herhangi bir andaki teğeti, zaman eksenini (sıfır eksenini) t+τ anında keser.