Oyun Kontrol ve Arduino Entegrasyonu
Bu Python kodu, bir oyunun ekran görüntüsünü yakalayarak görüntü üzerinde optik karakter tanıma (OCR) kullanır ve ekranda "GAME OVER" metnini tespit ettiğinde bir Arduino cihazına çıkış sinyali gönderir. Ayrıca, belirtilen tuş kombinasyonlarına basarak oyunu başlatır.

Nasıl Kullanılır
Gerekli Kütüphaneler

Kodun düzgün çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

pyautogui
easyocr
screeninfo
serial
keyboard
Bu kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

Copy code
pip install pyautogui easyocr screeninfo pyserial keyboard
Arduino Bağlantısı

Arduino'nuzu bilgisayarınıza bağlayın ve ardından Arduino'nun COM portunu bulmak için cihaz yöneticisini kullanarak bilgi edinin. Daha sonra, bu COM portunu kodunuzun kullanması için girin.

Tuşlar

keys.txt adlı bir metin dosyasında, oyunu başlatmak ve durdurmak için kullanılan tuşları belirtmelisiniz. Dosyanın içeriği şu şekilde olmalıdır:

Copy code
START_KEY
FIRST_PLAYER_KEY
SECOND_PLAYER_KEY
Örneğin:

Copy code
F1
F2
F3
Kodu Çalıştırma

Ana kodu çalıştırmak için main() fonksiyonunu çağırın. Kod, oyunu izlemeye başlayacak ve "GAME OVER" metnini tespit ettiğinde Arduino'ya bir sinyal gönderecektir.

