from datetime import datetime

print("\nSAAT KAÇ?\n")

def saat():
     print(datetime.now().hour, ':', datetime.now().minute, sep='')

saat()