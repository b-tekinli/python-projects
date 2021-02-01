#2 nokta arasındaki uzaklığı hesaplama

import random
import math

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # Haversine Formülü
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    km = 6371 * c      # Dünyanın yarıçapı = 6371
    return km

lon1 = random.uniform(0, 180.0)
lat1 = random.uniform(0, 180.0)
lon2 = random.uniform(0, 180.0)
lat2 = random.uniform(0, 180.0)

print(lon1, lat1, lon2, lat2)
print(haversine(lon1, lat1, lon2, lat2))