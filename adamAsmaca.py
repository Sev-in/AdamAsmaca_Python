# Problem Seti 2, adamAsmaca.py
# İsim: Şevin Sönmez
# Ortak çalışanlar: Ahmet Kaya ve Şevin Sönmez
# Harcanan zaman: 7 saat

# Adam Asmaca Oyunu
#------------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# ama fonksiyonları nasıl kullanacağını bilmeniz gerekecek
# (dökümanları okuduğunuzdan emin olun!)
from ntpath import join
import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    
     Kelime listesinin boyutuna bağlı olarak,
     bu fonksiyonun tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    return random.choice(wordlist)

# yardımcı kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden erişilebilmesi için
# kelime listesini değişken kelime listesine yükleyin
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    olcme_Degeri= True
    for i in letters_guessed:
       sonuc = i in secret_word and olcme_Degeri 
    return sonuc

        
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime;
    tüm harflerin küçük olduğunu varsayar
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi);
     tüm harflerin küçük olduğunu varsayar
     returns: boolean, secret_word'ün tüm harfleri letter_guessed içindeyse True;
     Aksi takdirde yanlış
    '''



def get_guessed_word(secret_word, letters_guessed):
    sozcuk =[]
    for i in range(len(secret_word)):
        sozcuk.append("_")
    for i in secret_word:
         if " " in secret_word:
            sozcuk.insert(secret_word.index(i)," ")

    for i in letters_guessed:
       sonuc = i in secret_word 
       if sonuc==True:
           for j in secret_word:
               if j==i:
                    sozcuk.pop(secret_word.index(j))
                    sozcuk.insert(secret_word.index(j),i)
    sonuc=""
    for i in sozcuk:
        sonuc += i
    return sonuc
                
    ["_"]     
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: harflerden, alt çizgilerden (_) ve şu ana kadar secret_word
     içindeki hangi harflerin tahmin edildiğini gösteren boşluklardan oluşan dize.
    '''



def get_available_letters(letters_guessed):

    tum_harfler= list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in tum_harfler:
            tum_harfler.remove(i)
    sonuc =""
    for i in tum_harfler:
        sonuc += i
    return sonuc
    '''
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: dize (harfler), hangi harflerin henüz tahmin edilmediğini temsil eden harflerden oluşur.
    '''
    
    
secret_word = choose_word(wordlist)

def adamAsmaca(secret_word):
    
    letters_guessed = []
    uyari_hakki = 3
    tahmin_hakki=6
    print("Adam asmaca oyununa hoş geldiniz!")
    print(f"{len(secret_word)} harf uzunluğunda bir kelime düşünüyorum.")
    print("-"*10)
    print(f"{tahmin_hakki} tahmin hakkınız kaldı!")
    print("Kullanılabilir harfler: ", get_available_letters(letters_guessed))

    while tahmin_hakki>=-1:
        harf_tahmini = input("Lütfen bir harf tahmin ediniz: ")
        dogru_cevap_sayisi=0
        
        if not(str.isalpha(harf_tahmini)):
            print("Yalnızca alfabe giriniz!")
            uyari_hakki-=1
            if uyari_hakki>=0:
                print("Kalan uyarı hakkınız: ",uyari_hakki)
            else:
                if uyari_hakki<0:
                    tahmin_hakki-=1
                print("Kalan tahmin hakkınız: ",tahmin_hakki)
            print("Son durum:",get_guessed_word(secret_word,letters_guessed))



        elif harf_tahmini in letters_guessed:
            print("Bu harfi daha önce tahmin etmiştiniz!")
            uyari_hakki-=1
            if uyari_hakki>=0:
                print("Kalan uyarı hakkınız: ",uyari_hakki)
            else:
                if uyari_hakki<0:
                    tahmin_hakki-=1
                print("Kalan tahmin hakkınız: ",tahmin_hakki)
            print("Son durum:",get_guessed_word(secret_word,letters_guessed))


        else:
            str.islower(harf_tahmini)
            letters_guessed.append(harf_tahmini)
            sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
            


            print(f"{tahmin_hakki} tahmin hakkınız kaldı!")
            print("Kullanılabilir harfler: ", get_available_letters(letters_guessed))

            if harf_tahmini in secret_word:
                print("Doğru cevap!!!",get_guessed_word(secret_word,letters_guessed))
                dogru_cevap_sayisi+=1
            else:
                if harf_tahmini in sesli_harfler:
                    tahmin_hakki-=2
                else: 
                    tahmin_hakki-=1
                print("Yanlış cevap!!!",get_guessed_word(secret_word,letters_guessed))
               

        print("-"*10)
        
        if tahmin_hakki ==0:
            print("Üzgünüm, tahmin hakkınız bitti!")
            print("Gizli kelime: ",secret_word)
            break
        if "_" not in get_guessed_word(secret_word, letters_guessed):
            print("Tebrikler kelimeyi tamamladınız!!!")

            benzersiz_harfler = []
            for i in secret_word:
                if i.isalpha():
                    benzersiz_harfler.append(i)

                    benzersiz_harf_sayisi = len(benzersiz_harfler)

            toplam_puan = tahmin_hakki * benzersiz_harf_sayisi
            print(f"Toplam puanınız: {toplam_puan}")
            break


    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyununu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini
        ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve
        kullanıcının henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir mektup yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''




# Adam asmaca işlevinizi tamamladığınızda, dosyanın
#en altına gidin ve test edilecek ilk iki satırın yorumunu kaldırın
# (ipucu: kendi testinizi yaparken kendi secret_word'ünüzü
# seçmek isteyebilirsiniz)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    gercek_sonuc = True  # varsayılan olarak True olarak başlatın

    for i in range(len(other_word)):
        if other_word[i] == my_word[i] or my_word[i] == '_':
            continue  # Eğer karakterler eşleşiyorsa veya my_word'deki karakter "_" ise bir sonraki adıma geçsin.
        else:
            gercek_sonuc = False  # Eğer karakterler eşleşmiyorsa ve my_word'deki karakter "_" değilse, eşleşme yoktur.
            break  # Döngüyü sonlandırın, çünkü eşleşme bulunamadı.

    return gercek_sonuc

    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    other_word: string, normal İngilizce kelime
    returns: boolean, True, eğer my_word'ün tüm gerçek harfleri other_word'ün karşılık gelen harfleriyle eşleşiyorsa veya harf özel sembol _ ise ve my_word ile other_word aynı uzunluktaysa; Aksi takdirde False:
    '''



def show_possible_matches(my_word):
    with open(WORDLIST_FILENAME, "r") as dosya:
        metin = dosya.read()

    kelimeler = metin.split()

    uygun_kelimeler = []
    for kelime in kelimeler:
        if len(kelime) == len(my_word):
            eşleşme_var = True
            for i in range(len(my_word)):
                if my_word[i] != '_' and my_word[i] != kelime[i]:
                    eşleşme_var = False
                    break
            if eşleşme_var:
                uygun_kelimeler.append(kelime)

    if uygun_kelimeler:
        print(uygun_kelimeler)
    else:
        print("Eşleşme bulunamadı")


    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    returns: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen
        her kelimeyi yazdırmalıdır.
    adamAsmaca ile bir harf tahmin edildiğinde, o harfin gizli kelimede
        geçtiği tüm pozisyonların ortaya çıktığını unutmayın.
    Bu nedenle, gizli harf(_ ) zaten ortaya çıkmış olan kelimedeki
     harflerden biri olamaz.
    '''



def adamAsmaca_ipuclu(secret_word):
    
    letters_guessed = []
    uyari_hakki = 3
    tahmin_hakki=6
    print("Adam asmaca oyununa hoş geldiniz!")
    print(f"{len(secret_word)} harf uzunluğunda bir kelime düşünüyorum.")
    print("-"*10)
    print(f"{tahmin_hakki} tahmin hakkınız kaldı!")
    print("Kullanılabilir harfler: ", get_available_letters(letters_guessed))

    while tahmin_hakki>=-1:
        harf_tahmini = input("Lütfen bir harf tahmin ediniz: ")
        print("İpucu almak istiyorsanız '*' tuşlayınız!")
        
        if harf_tahmini=="*":
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))


        elif not(str.isalpha(harf_tahmini)):
            print("Yalnızca alfabe giriniz!")
            uyari_hakki-=1
            if uyari_hakki>=0:
                print("Kalan uyarı hakkınız: ",uyari_hakki)
            else:
                if uyari_hakki<0:
                    tahmin_hakki-=1
                print("Kalan tahmin hakkınız: ",tahmin_hakki)
            print("Son durum:",get_guessed_word(secret_word,letters_guessed))
            


        elif harf_tahmini in letters_guessed:
            print("Bu harfi daha önce tahmin etmiştiniz!")
            uyari_hakki-=1
            if uyari_hakki>=0:
                print("Kalan uyarı hakkınız: ",uyari_hakki)
            else:
                if uyari_hakki<0:
                    tahmin_hakki-=1
                print("Kalan tahmin hakkınız: ",tahmin_hakki)
            print("Son durum:",get_guessed_word(secret_word,letters_guessed))
            

        else:
            str.islower(harf_tahmini)
            letters_guessed.append(harf_tahmini)
            sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
            


            print(f"{tahmin_hakki} tahmin hakkınız kaldı!")
            print("Kullanılabilir harfler: ", get_available_letters(letters_guessed))

            if harf_tahmini in secret_word:
                print("Doğru cevap!!!",get_guessed_word(secret_word,letters_guessed))
            else:
                if harf_tahmini in sesli_harfler:
                    tahmin_hakki-=2
                else: 
                    tahmin_hakki-=1
                print("Yanlış cevap!!!",get_guessed_word(secret_word,letters_guessed))
               

        print("-"*10)
        
        if tahmin_hakki ==0:
            print("Üzgünüm, tahmin hakkınız bitti!")
            print("Gizli kelime: ",secret_word)
            break
        if "_" not in get_guessed_word(secret_word, letters_guessed):
            print("Tebrikler kelimeyi tamamladınız!!!")

            benzersiz_harfler = []
            for i in secret_word:
                if i.isalpha():
                    benzersiz_harfler.append(i)

                    benzersiz_harf_sayisi = len(benzersiz_harfler)

            toplam_puan = tahmin_hakki * benzersiz_harf_sayisi
            print(f"Toplam puanınız: {toplam_puan}")
            break
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyunu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini ve
        kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır
    
     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve kullanıcının
        henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir harf tahmin ettiğini kontrol ettiğinizden emin olun.
      
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
      
     * Tahmin sembolü * ise, kelime listesindeki mevcut tahmin edilen
        kelimeyle eşleşen tüm kelimeleri yazdırın.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''



# adamAsmaca_ipuclu işlevinizi tamamladığınızda, yukarıdaki adam asmaca
# fonksiyonunu çalıştırmak için kullanılan benzer iki satırı yorumlayın ve
# ardından bu iki satırın yorumunu kaldırın ve test etmek için bu dosyayı çalıştırın!
# İpucu: Test ederken kendi secret_word'ünüzü seçmek isteyebilirsiniz.


if __name__ == "__main__":
    # pass

    # 2. bölümü test etmek için yukarıdaki pass satırında # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin
    
    # secret_word = choose_word(wordlist)
    # adamAsmaca(secret_word)
    

###############
    
# 3. bölümü test etmek için yukarıdaki satırlarlarda yeniden # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin

    secret_word = choose_word(wordlist)
    adamAsmaca_ipuclu(secret_word)
