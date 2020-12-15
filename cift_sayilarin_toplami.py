counter = 0                                                         # counter değişkenini 0'a eşitledik.
number = 20                                                         # number değişkenini 20'ye eşitledik.
add = 0                                                             # add değişkenini 0'a eşitledik.

while counter < number:                                             # counter'ı number'dan küçük tuttuk.
    add += counter                                                  # add'i counter ile toplayıp add'e atadık.
    counter += 2                                                    # counter'ı 2 ile toplayıp counter'a atadık.
print(f"0'dan 20'ye kadar olan çift sayıların toplamı: {add}")      # ekrana toplamı yazdırdık.
