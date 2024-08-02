import random
Kelime_listesi = ["kalem","araba","diyaliz","mide","kalınbağırsak","sevgi","süleyman","fatma","reşide","mahmut",
                  "çaybardağı","çaydanlık","oruç","ramazan","iftar","baklava","etliekmek","kaymak","künefe",
                  "kumpir","karnıyarık","kahve","yastık","yorgan","yatak","koltuk","sandalye","sürahi","kağıt",
                  "dergi","mum","radyoaktif","nükleer","kuyruk","kurbağa","kedi","köpek","zürafa","fare","fil",
                  "zebra","devekuşu","kaplan","aslan","yılan","timsah","çiçek","saksı","ağaç","papatya","manolya",
                  "lale","gül","deve","masalambası","ruj","maskara","hoparlör","sürme","güneşkremi","bilgisayar",
                  "mühendis","mimar","şoför","esnaf","yönetici","mercedes","perde","konya","kolonya","erzurum",
                  "ağrı","van","izmir","istanbul","ankara","sivas","çanakkale","bursa","bolu","trabzon","zonguldak",
                  "ordu","asker","polis","öğretmen","inşaat","muğla","karnabahar","ilkbahar","sonbahar","kış","deniza"
                                                                                                              "a"]
while True:
    rkelime = random.choice(Kelime_listesi)
    #print(rkelime)
    uzunluk = len(rkelime)
    print("Kelimenin uzunlugu: '", end='')              #Harf sayısı kadar '_' yazdırılacaktır
    for i in range(uzunluk):
        print("_ ", end='')
    print("'",end='')
    print("{} harfli".format(uzunluk))

    #if uzunluk % 2 == 0:                                #Tahmin hakkını hesapladım
     #   tahmin_hak = uzunluk // 2
    #else:
     #   tahmin_hak = (uzunluk + 1) // 2
    tahmin_hak = 5
    print("Tahmin hakkı:", tahmin_hak)
    #tr_karakterler = "çğöşüı"
    puan = 0
    sesli_harfler = "aeiıöüou"
    sessiz_harfler = "bcçdfgğhjklmnprsştvyzqwx"
    bilinen = []                                    #dogru tahmin edilen harfleri tutacak bir liste olusturdum
    girilenler=[]                                   #girilen harf tekrarını kontrol etmek için girilenleri listeye kaydettim
    for i in range(uzunluk):
        bilinen += '_'                              #bilinen harfleri kaydetmek için listenin şablonunu oluşturdum
    kont=0                                          #girilen harf tekrarını kontrol eden degişken
    c=0                                             #girilen harf tekrarını kontrol için degisken
    while tahmin_hak >= 0:
        sayac = 0                                   #puan hesabı yaparken bilinen harf sayısını saymak için
        harf = input("\nHarf giriniz:").lower()
        kont+=1
        if kont!=1:
            for i in girilenler:                           #girilen harf tekrarını kontrol ediyor
                if harf==i:
                    print("Girdiginiz harfi tekrar girmeyiniz.")
                    c=1
                else:
                    c=0
        if c==1:
            continue
        for i in range(1):
            girilenler+=harf                        #girilen harfleri girilenler listesine kaydettim
        #if harf in tr_karakterler:                  #tr karakter girilirse uyarı verdirdim
            #print("Türkçe karakter giremezsiniz!")
            #continue
        if len(harf) != 1:                          #birden fazla harf girilirse uyarı verdirdim
            print("Birden fazla harf girmeyiniz.")
            continue
        for i in range(uzunluk):
            if harf != rkelime[i]:                  #girilen harf kelimede bulunuyor mu kontrolu yaptım
                continue
            else:
                bilinen[i] = harf                 #bulunuyorsa bilinen listesinin o indisine yerleştirdim
                sayac += 1                          #kelimede o harften kaç tane oldugunu saydım
        if harf in sesli_harfler:
            puan += sayac * 3                       #kelimede bulunan harf sesli harfse ve bir veya birden fazla varsa harf sayısı kadar 3 puan kazanır
        if harf in sessiz_harfler:
            puan += sayac * 3                       #kelimede bulunan harf sessiz harfse ve bir veya birden fazla varsa harf sayısı kadar 2 puan kazanır
        if sayac == 0:
            tahmin_hak = tahmin_hak - 1             #harfin kelimede olmaması durumunda 1 tahmin hakkını kaybeder
            puan -= 4                               #bilinemeyen her harf için 4 puan kaybeder

        if tahmin_hak==5:
            print("                                   ____")
            print("                                  |    |")
            print("                                       |")
            print("                                       | ")
            print("                                       | ")
        if tahmin_hak==4:
            print("                                   ____")
            print("                                  |    |")
            print("                                  O    |")
            print("                                       | ")
            print("                                       | ")
        if tahmin_hak==3:
            print("                                   ____")
            print("                                  |    |")
            print("                                  O    |")
            print("                                 /     |")
            print("                                       | ")
        if tahmin_hak==2:
            print("                                   ____")
            print("                                  |    |")
            print("                                  O    |")
            print("                                 /|    |")
            print("                                       | ")
        if tahmin_hak==1:
            print("                                   ____")
            print("                                  |    |")
            print("                                  O    |")
            print("                                 /|\   | ")
            print("                                       | ")
        if tahmin_hak==0:
            print("                                   ____")
            print("                                  |    |")
            print("                                  O    |")
            print("                                 /|\   | ")
            print("                                 /     | ")
        if tahmin_hak==-1:
            print("                                   ____")
            print("                                  |    |")
            print("                                  O    |")
            print("                                 /|\   | ")
            print(" ADAM ÖLDÜ AFERİN!!              / \   |")
        print("Kelimenin durumu:",end='')           #her hamlede kelimenin son hali yazdırılmalıdır
        for i in bilinen:
            print(i,end='')
        print(" ")
        if tahmin_hak != -1:
            print("Kalan yanılma hakki:", tahmin_hak) #her hamlede kalan yanılma hakkı yazdırılmalıdır
        print("puan:", puan)                          #her hamle sonunda puan yazılmalıdır
        print("Girilen harfler:",girilenler)
        if tahmin_hak == -1:                                            #hak kalmadıgı durumunda proje sonlanır
            #print("Adam öldü aferin ><")
            print("Kelime '{}' idi".format(rkelime))
            break
        if bilinen == list(rkelime):                  #kelime bulunduysa menüye yönlendirilir- kıyas icin kelimeyi listeye cevirdim
            print("Tebrikler...Kelimeyi buldunuz!!!")
            break
    print("---------------MENÜ---------------")
    print("1-Çıkış\t\t2-Yeni Kelime Tahmini")                           #menü
    secim = int(input("Lütfen yapmak istediğiniz islemi seciniz:"))
    while secim!=1 and secim!=2:                         #1 ve 2den başka tuşlama yapıldıgı durumda tekrar secim alınır
        secim=int(input("Gecerli tuslama yapiniz:"))
        if secim==2 or secim==1:
            break
    if secim==1:
        break
    else:
        print("KELİME TAHMİNİ OYUNUNA YENİDEN HOŞGELDİNİZ!")
