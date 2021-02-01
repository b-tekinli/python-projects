import random
import math
from termcolorer import Color, cprint

# 1- Türk Silahlı Kuvvetleri
# 2- NATO Birliğine ait Silahlı Birim
# 3- Silahsız Araç
# 4- Tehdit Unsurları
# 5- Füze ve benzeri Silah unsurları

sampleArac = [1,2,3,4,5]
# A = Kara Aracı
# B = Deniz Aracı
# C = Hava Aracı

sampleTur = ["Kara","Deniz","Hava"]
def haversine(lon1, lat1, lon2, lat2):
    # Decimal değerleri radyan cinsine çeviriyor
    lon1, lat1, merkezlon, merkezlat = map(math.radians, [lon1, lat1, lon2, lat2])
    # Haversine Formülü
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 +math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = 6371* c        # Dünyanın yarıçapı = 6371
    return km

def tehditOLC():
    arac = random.sample(sampleArac,1)
    tur = random.sample(sampleTur,1)
    if arac[0] == 1 or arac[0] == 2 or arac[0] == 3:
        tehditMi = False
    else:
        tehditMi = True
    lon1 = random.uniform(25.0,45.0)
    lat1 = random.uniform(25.0,45.0)

    if haversine(lon1, lat1, merkezLon, merkezLat) > 6500 or tehditMi == False:
        if arac[0] == 1:
            cprint(f"Bu birim Türk Silahlı kuvvetlerine ait {str(tur[0])} aracıdır. TEHDİT DEĞİLDİR.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'green')
        if arac[0] == 2:
            cprint(f"Bu birim NATO Birliğine ait {str(tur[0])} aracıdır. TEHDİT DEĞİLDİR.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'green')
        if arac[0] == 3:
            cprint(f"Bu birim Silahsız {str(tur[0])} aracıdır. TEHDİT DEĞİLDİR.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'green')
        if arac[0] == 4:
            cprint(f"Bu cismin uzaklığı tehdit oluşturmayacak düzeydedir.", 'green')
            cprint(f"Bu birim tanımlanamamıştır, {str(tur[0])} aracıdır. TEHDİT OLABİLİR.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'red')
        if arac[0] == 5:
            cprint(f"Bu birim bir silahtır.{str(tur[0])} dan/den gelmektedir. ACİL DURUM.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'red')
    else:
        if arac[0] == 4:
            cprint(f"Bu birim tanımlanamamıştır, {str(tur[0])} aracıdır. TEHDİT OLABİLİR.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'red')
            return 1
        if arac[0] == 5:
            cprint(f"Bu birim bir silahtır. {str(tur[0])} dan/den gelmektedir. ACİL DURUM.\nTespit edilen cismin kordinatları {lon1}, {lat1}\nAramızdaki uzaklık: {haversine(lon1,lat1,merkezLon,merkezLat))}", 'red')
            return 1



acilDurum = 0
merkezLon = 39.9333635
merkezLat = 32.8597419

for i in range(0,15,1):
    cprint(f"Durum {i+1}", 'blue')
    cprint("\n------------------------------------------------------------------------\n",'blue')
    if tehditOLC() == 1:
        acilDurum = acilDurum +1
    cprint("\n------------------------------------------------------------------------\n",'blue')
print(f"{15000} cisimden tehdit olabilecek {acilDurum} cisim tespit edilmiştir.")