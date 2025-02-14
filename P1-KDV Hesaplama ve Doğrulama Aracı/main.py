from calculate import calculate_kdv
from validate import rate_validatiton, amount_validation

if __name__ == "__main__":
  while True:
    try:
      while True:  # Amount için döngü
        amount = float(input("Ürün fiyatını giriniz: "))
        if amount_validation(amount):
            break  # Geçerli giriş yapıldığında döngüden çık
        else:
            print("Hata: Geçersiz fiyat girdiniz!")

      while True:  # Rate için döngü
        rate = float(input("KDV oranını giriniz (% cinsinden): "))
        if rate_validatiton(rate):
            break  # Geçerli giriş yapıldığında döngüden çık
        else:
            print("Hata: Geçersiz KDV oranı girdiniz!")

      gross_amount, vat_amount = calculate_kdv(amount, rate)

      print(f"KDV Dahil Fiyat: {gross_amount:.2f}")
      print(f"KDV Tutarı: {vat_amount:.2f}")
      break  # Tüm girişler doğru olduğunda döngüden çık

    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")

  #doğru girilen bilgiyi tekrardan istemesin>> Çözüldü. Her veri giriş işlemini while döngüsü içine aldım.
  #Kullanıcıdan input girişimi yapacağı yoksa excel dosyasımı yükleyeceğini sorsun. Kullanıcının cevabına göre işlemi yapsın.