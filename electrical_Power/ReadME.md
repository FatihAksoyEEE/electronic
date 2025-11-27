<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elektronik Güç Hesaplayıcı</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    
    <style>
        :root {
            --primary-color: #0056b3;
            --bg-color: #f8f9fa;
            --text-color: #333;
            --code-bg: #2d2d2d;
            --code-text: #f8f8f2;
            --accent: #e7f1ff;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.05);
            min-height: 100vh;
        }

        header {
            border-bottom: 2px solid var(--accent);
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }

        h1 { color: var(--primary-color); font-size: 2.2rem; margin-bottom: 0.5rem; }
        h2 { color: #2c3e50; border-left: 5px solid var(--primary-color); padding-left: 10px; margin-top: 2rem; }
        h3 { color: #444; margin-top: 1.5rem; }
        p { margin-bottom: 1rem; }

        /* Kod Blokları */
        pre {
            background-color: var(--code-bg);
            color: var(--code-text);
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        }

        /* Tablo Stilleri */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            font-size: 0.95rem;
        }
        
        table th, table td {
            padding: 12px 15px;
            border: 1px solid #ddd;
            text-align: left;
        }

        table th {
            background-color: var(--primary-color);
            color: white;
        }

        table tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        /* Güç Üçgeni Görselleştirmesi (CSS ile) */
        .triangle-container {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        .triangle-box {
            position: relative;
            width: 200px;
            height: 150px;
            border-bottom: 3px solid #e74c3c; /* P (Aktif) */
            border-right: 3px solid #2ecc71;  /* Q (Reaktif) */
        }
        .triangle-hypotenuse {
            position: absolute;
            width: 250px;
            height: 3px;
            background-color: #3498db; /* S (Görünür) */
            top: 75px;
            left: -25px;
            transform: rotate(-37deg);
        }
        .label { position: absolute; font-weight: bold; font-size: 0.9rem; }
        .label-p { bottom: -25px; left: 40%; color: #e74c3c; }
        .label-q { right: -90px; top: 40%; color: #2ecc71; }
        .label-s { top: 30px; left: 30%; color: #3498db; }

        /* Etiketler */
        .badge {
            display: inline-block;
            padding: 0.25em 0.6em;
            font-size: 75%;
            font-weight: 700;
            line-height: 1;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: 0.25rem;
            color: #fff;
            background-color: #6c757d;
        }
        .badge-dc { background-color: #17a2b8; }
        .badge-ac { background-color: #fd7e14; }

    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Elektronik Güç Hesaplayıcı</h1>
        <p>Bu proje, elektrik ve elektronik devrelerinde kullanılan temel güç hesaplamalarını (DC ve AC) gerçekleştiren bir araçtır.</p>
    </header>

    <div class="triangle-container">
        <div class="triangle-box">
            <div class="triangle-hypotenuse"></div>
            <span class="label label-p">P (Aktif Güç)</span>
            <span class="label label-q">Q (Reaktif Güç)</span>
            <span class="label label-s">S (Görünür Güç)</span>
        </div>
    </div>
    <p style="text-align: center; font-size: 0.8rem; color: #666;">*Temsili Güç Üçgeni (Power Triangle)</p>

    <section>
        <h2>Özellikler</h2>
        <p>Program, aşağıdaki senaryolarda hesaplama yapabilir:</p>

        <h3>1. DC Güç Hesaplamaları <span class="badge badge-dc">DC</span></h3>
        <ul>
            <li><strong>Voltaj ve Akım ile:</strong> $$P = V \cdot I$$</li>
            <li><strong>Akım ve Direnç ile:</strong> $$P = I^2 \cdot R$$</li>
            <li><strong>Voltaj ve Direnç ile:</strong> $$P = \frac{V^2}{R}$$</li>
        </ul>

        <h3>2. AC Güç Hesaplamaları <span class="badge badge-ac">AC</span></h3>
        <p>Tek fazlı AC devrelerde <strong>güç faktörü</strong> ($$\cos\phi$$) kullanılarak:</p>
        <ul>
            <li><strong>Aktif Güç (P):</strong> $$P = V_{rms} \cdot I_{rms} \cdot \cos\phi$$ <br> <small>Birim: Watt (W)</small></li>
            <li><strong>Reaktif Güç (Q):</strong> $$Q = V_{rms} \cdot I_{rms} \cdot \sin\phi$$ <br> <small>Birim: VAr</small></li>
            <li><strong>Görünür Güç (S):</strong> $$S = \sqrt{P^2 + Q^2}$$ <br> <small>Birim: VA</small></li>
        </ul>
    </section>

    <section>
        <h2>Kurulum</h2>
        <p>Bu proje Python ile yazılmıştır ve harici kütüphane gerektirmez.</p>
        <pre><code># Dosyayı çalıştırın
python power_calc.py</code></pre>
    </section>

    <section>
        <h2>Kullanım Senaryosu</h2>
        <p>Örnek bir AC Motor güç hesabı çıktısı:</p>
        <pre><code>--- Güç Hesaplayıcı ---
1. DC Güç Hesapla
2. AC Güç Hesapla
Seçiminiz: 2

Voltaj (Vrms): 220
Akım (Irms): 5
Güç Faktörü (cos phi): 0.8

Sonuçlar:
- Görünür Güç (S): 1100.0 VA
- Aktif Güç (P): 880.0 W
- Reaktif Güç (Q): 660.0 VAR</code></pre>
    </section>

    <section>
        <h2>Formül Referansı</h2>
        <table>
            <thead>
                <tr>
                    <th>Hesaplama Türü</th>
                    <th>Formül</th>
                    <th>Açıklama</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>DC Temel</strong></td>
                    <td>$$P = V \cdot I$$</td>
                    <td>V ve I biliniyorsa</td>
                </tr>
                <tr>
                    <td><strong>DC (Dirençli)</strong></td>
                    <td>$$P = I^2 \cdot R$$</td>
                    <td>I ve R biliniyorsa</td>
                </tr>
                <tr>
                    <td><strong>AC Aktif</strong></td>
                    <td>$$P = S \cdot \cos\phi$$</td>
                    <td>İş yapan gerçek güç</td>
                </tr>
                <tr>
                    <td><strong>AC Reaktif</strong></td>
                    <td>$$Q = S \cdot \sin\phi$$</td>
                    <td>Bobin/Kondansatör gücü</td>
                </tr>
            </tbody>
        </table>
    </section>

    <footer style="margin-top: 3rem; border-top: 1px solid #eee; padding-top: 1rem; text-align: center; color: #888;">
        <p>Açık Kaynak Kodlu Eğitim Projesi</p>
    </footer>
</div>

</body>
</html>