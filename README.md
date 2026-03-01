# Meme-interactive-cam
MediaPipe ve OpenCV kullanarak el hareketleri ve yüz ifadeleriyle tetiklenen interaktif bir meme uygulaması. (Python 3.11 + Ubuntu 24.04 uyumlu)
Ubuntu/Linux kullanıcıları MediaPipe'ın yerelleştirme hatasını almamak için programı LC_ALL=C python maymun_test.py komutuyla çalıştırmalıdır.

Bu proje, MediaPipe ve OpenCV kullanarak el hareketlerinizi ve yüz ifadelerinizi algılayan, bu hareketlere göre ekranın sağ üst köşesinde farklı "Meme" görselleri çıkaran interaktif bir Python uygulamasıdır.

Gereksinimler ve Sürüm Bilgisi
Bu projenin hatasız çalışması için aşağıdaki sürümlerin kullanılması kritiktir:

    Python Sürümü: 3.11.x (MediaPipe, Python 3.12 ve üzeri sürümlerde stabilite sorunları yaşatabilmektedir).

    İşletim Sistemi: Linux (Ubuntu 24.04 test edildi), Windows veya macOS.

    Öncelikle gerekli kütüphaneleri yükleyin
    pip install mediapipe opencv-python

    Kodun çalışması için aşağıdaki isimlerde görsellerin proje klasöründe bulunması gerekir:

    maymun.png (İşaret parmağı havada)

    maymun2.png (Düşünen maymun / Parmak ağızda)

    maymun3.png (Dil çıkaran / Ağız açık)

    nah.png (N*h hareketi)

    Kontroller ve Hareketler:

    Ağız Açık: Dil çıkaran maymun belirir (Ultra hassas algılama).

    İşaret Parmağı Ağızda: Düşünen maymun belirir.

    Sadece İşaret Parmağı Havada: Yukarı bakan maymun belirir.

    Yumruk + Baş Parmak Dışarıda: Nah çeken maymun belirir.

    Kapatmak İçin: Klavye üzerinden q veya Q tuşuna basın.

