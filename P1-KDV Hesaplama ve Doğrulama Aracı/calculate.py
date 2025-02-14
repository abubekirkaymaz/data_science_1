#kdv hesapalama  fonksiyonu. 

def calculate_kdv (net_amount, vat_rate):
  vat_amount = net_amount * (vat_rate / 100)
  gross_amount = net_amount + vat_amount
  
  return gross_amount, vat_amount #kdv dahil tutar


