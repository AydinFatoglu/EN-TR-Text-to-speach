# Multilingual Clipboard Text-to-Speech

Multilingual Clipboard Text-to-Speech, panoya kopyaladığınız metni otomatik olarak okuyan, hafif ve çevrimdışı çalışan bir Python programıdır. Hızlı ve internet gerektirmeyen ses üretimi için yerel Windows Konuşma API'sini (SAPI) kullanır ve `tkinter` ile oluşturulmuş modern bir grafik arayüzüne (GUI) sahiptir.

## Özellikler

*   **Pano İzleme (Otomatik Okuma):** Panoya kopyalanan yeni metni otomatik olarak algılar ve yapıştırmaya gerek kalmadan anında yüksek sesle okur.
*   **Tek Tıkla Dil Değiştirme:** Arayüzdeki interaktif bayrak simgesine tıklayarak Türkçe (Microsoft Tolga) ve İngilizce (Microsoft David) sesleri arasında sorunsuz bir şekilde geçiş yapın.
*   **Ayarlanabilir Okuma Hızı:** Gerçek zamanlı bir kaydırıcı kullanarak konuşma hızını %50'den %200'e kadar özelleştirin.
*   **%100 Çevrimdışı Çalışma:** Yerel Windows SAPI'yi (`win32com.client`) kullanarak, uygulama internet bağlantısı veya harici API limitleri gerektirmez.
*   **Asenkron Oynatma ve Durdurma:** Ses arka planda işlenir, uygulamayı duyarlı tutar ve "Durdur" düğmesiyle oynatmayı anında durdurmanıza olanak tanır.
*   **Her Zaman Üstte:** Uygulama penceresi, çalışırken veya gezinirken kolay erişim için diğer pencerelerin üzerinde kalır.

## Gereksinimler

*   **İşletim Sistemi:** Windows (Windows SAPI için gereklidir).
*   **Python 3.x:** Sisteminizde Python 3.x'in yüklü olduğundan emin olun.
*   **Gerekli Kütüphaneler:** Gerekli paketleri pip üzerinden yükleyin:
    ```bash
    pip install pyperclip pywin32
    ```

## Kullanım

1.  Depoyu klonlayın veya kaynak kodu yerel makinenize indirin.
2.  Yukarıda belirtilen komutu kullanarak gerekli bağımlılıkları yükleyin.
3.  *(İsteğe bağlı)* US ve TR bayrakları için özel Base64 PNG kodlarınızı kodun içindeki belirlenmiş alanlara ekleyin.
4.  Programı çalıştırın:
    ```bash
    python text_to_speech.py
    ```
5.  **Metni Okumak İçin:** Bilgisayarınızın herhangi bir yerinden herhangi bir metni kopyalayın (`Ctrl+C`). "Panoyu otomatik oku" onay kutusu işaretliyse, otomatik olarak okumaya başlayacaktır. Alternatif olarak, **"▶ OKU" (PLAY)** düğmesine tıklayın.
6.  **Dili Değiştirmek İçin:** İngilizce ve Türkçe arasında geçiş yapmak için pencerenin ortasındaki Bayrak Simgesine tıklayın.
7.  **Hızı Ayarlamak İçin:** Tercih ettiğiniz okuma hızını ayarlamak için kaydırıcıyı sürükleyin.
8.  **Durdurmak İçin:** Mevcut ses çalmayı hemen durdurmak için **"■ DURDUR" (STOP)** düğmesine tıklayın.

## Sınırlamalar

*   **Yalnızca Windows:** Bu uygulama, `win32com.client` ve yerel Windows SAPI'ye olan bağımlılığı nedeniyle Windows ortamları için özel olarak tasarlanmıştır.
*   **Sistem Sesleri:** Kullanılabilir sesler, Windows işletim sisteminizde yüklü olan TTS dil paketlerine bağlıdır (özellikle bu konfigürasyonda İngilizce için *Microsoft David* ve Türkçe için *Microsoft Tolga* beklenmektedir).

## Katkıda Bulunma

Multilingual Clipboard Text-to-Speech programına katkılarınız kabul edilir! Herhangi bir sorun bulursanız, çapraz platform desteği eklemek isterseniz veya iyileştirme önerileriniz varsa, lütfen bir sorun (issue) açın veya bir çekme isteği (pull request) gönderin.
