krediler = ["Hızlı Krediler","Maaşını Halk Bank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]

for kredi in krediler: #kredi=alias(takma ad)
  print("<option>"+kredi+"<option>") 

for i in range(10): #10 kere tekrarlanacak bir döngüyü ifade eder.
  print(i)

for i in range(len(krediler)): #krediler listesinin uzunluğunu alır.
  print(krediler[i])

for i in range(3,10) #3 dahil 10 dahil değil.
  print(i)

for i in range(0,10,2): #0'dan 10'a kadar 2'şer gider.
  print(i)

