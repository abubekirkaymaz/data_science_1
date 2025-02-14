from calculate import calculate_kdv
from validate import rate_validatiton, amount_validation

if __name__ == "__main__":
  while True:
    try:
      amount = float(input("Ürün fiyatını giriniz: "))
      rate = float(input("KDV oranını giriniz (% cinsinden): "))

      if not amount_validation(amount):
        print("Hata: Geçersiz fiyat girdiniz!")
      elif not rate_validatiton(rate):
        print("Hata: Geçersiz KDV oranı girdiniz!")
      else:
        gross_amount, vat_amount = calculate_kdv(amount, rate)
        print(f"KDV Dahil Fiyat: {gross_amount}")
        print(f"KDV Tutarı: {vat_amount}")
        break  # Doğru giriş yapıldığında döngüden çık
    except ValueError:
      print("Lütfen geçerli bir sayı giriniz!")

  #doğru girilen bilgiyi tekrardan istemesin