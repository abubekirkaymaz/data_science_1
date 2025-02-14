def amount_validation (amount):
  return amount > 0 # Fiyat negatif veya sıfır olmamalı
  
def rate_validatiton (rate):
  rate_list = [1, 8, 20] # Türkiye’de yaygın kullanılan KDV oranları
  return rate in rate_list


