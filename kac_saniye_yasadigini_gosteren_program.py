# import datetime

# print("\nDOĞUM GÜNÜ UYGULAMASI\n")

# def birthday_info():
#     print("Doğum bilgilerinizi giriniz..")
#     d = int(input("Gün: "))
#     m = int(input("Ay: "))
#     y = int(input("Yıl: "))

#     birth_day = datetime.date(d, m, y)
#     return birth_day

# def date_calculate(origin_date, target_date):
#     this_year = datetime.date(target_date.year, origin_date.month, origin_date.day)

#     day_difference = this_year - target_date
#     return day_difference.days

# def birthday(days):
#     if days < 0:
#         print("Bu yıl doğum günün {days} gün önceydi.")
#     elif days > 0:
#         print("Doğum günün {days} gün sonra.")
#     else:
#         print("Doğum günün kutlu olsun...")

# def main():
#     b_day = birthday_info()
#     today = datetime.date.today()
#     number_of_days = date_calculate(b_day, today)
#     birthday(number_of_days)


# main()