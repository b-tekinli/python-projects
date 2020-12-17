print("\nSICAKLIK ÇEVİREN PROGRAM\n")

choose = int(input("1.Celsius-Fahrenheit\n2.Fahrenheit-Celsius\nSeçim yapınız-1/2-: "))

if choose == 1:
    celsius = float(input("\nDönüştürülecek derece: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"\n{celsius} santigrat derece, {fahrenheit} fahrenhayt dereceye eşittir.")
elif choose == 2:
    fahrenheit = float(input("\nDönüştürülecek derece: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"\n{fahrenheit} fahrenhayt derece, {celsius} santigrat dereceye eşittir.")
else:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz..")