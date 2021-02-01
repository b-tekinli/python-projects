print("\nMORS ALFABESİ\n")

# A = .-
# B = -...
# C = -.-.
# D = -..
# E = .
# F = ..-.
# G = ..-
# H = ....
# I = ..
# J = .---
# K = -.-
# L = .-..
# M = --
# N = -.
# O = ---
# P = .--.
# Q = --.-
# R = .-.
# S = ...
# T = -
# U = ..-
# V = ...-
# W = .--
# X = -..-
# Y = -.--
# Z = --..
# 0 = -----
# 1 = .----
# 2 = ..---
# 3 = ...--
# 4 = ....-
# 5 = .....
# 6 = -....
# 7 = --...
# 8 = ---..
# 9 = ----.

def MorsAlfabesiDonustur():
    mesaj = input("Mors alfabesi ile yazdırmak istediğiniz mesaj nedir? \n")
    mesaj = mesaj.upper()
    for i in range(len(mesaj)):
        if mesaj[i] == 'A':
            print('.-', end = '')
        elif mesaj[i] == 'B':
            print('-...', end = '')
        elif mesaj[i] == 'C':
            print('-.-.', end = '')
        elif mesaj[i] == 'D':
            print('-..', end = '')
        elif mesaj[i] == 'E':
            print('.', end = '')
        elif mesaj[i] == 'F':
            print('..-.', end = '')
        elif mesaj[i] == 'G':
            print('..-', end = '')
        elif mesaj[i] == 'H':
            print('....', end = '')
        elif mesaj[i] == 'I':
            print('..', end = '')
        elif mesaj[i] == 'J':
            print('.---', end = '')
        elif mesaj[i] == 'K':
            print('-.-', end = '')
        elif mesaj[i] == 'L':
            print('.-..', end = '')
        elif mesaj[i] == 'M':
            print('--', end = '')
        elif mesaj[i] == 'N':
            print('-.', end = '')
        elif mesaj[i] == 'O':
            print('---', end = '')
        elif mesaj[i] == 'P':
            print('.--.', end = '')
        elif mesaj[i] == 'Q':
            print('--.-', end = '')
        elif mesaj[i] == 'R':
            print('-.-.', end = '')
        elif mesaj[i] == 'S':
            print('...', end = '')
        elif mesaj[i] == 'T':
            print('-', end = '')
        elif mesaj[i] == 'U':
            print('..-', end = '')
        elif mesaj[i] == 'V':
            print('...-', end = '')
        elif mesaj[i] == 'W':
            print('.--', end = '')
        elif mesaj[i] == 'X':
            print('-..-', end = '')
        elif mesaj[i] == 'Y':
            print('-.--', end = '')
        elif mesaj[i] == 'Z':
            print('--..', end = '')
        elif mesaj[i] == '0':
            print('-----', end = '')
        elif mesaj[i] == '1':
            print('.----', end = '')
        elif mesaj[i] == '2':
            print('..---', end = '')
        elif mesaj[i] == '3':
            print('...--', end = '')
        elif mesaj[i] == '4':
            print('....-', end = '')
        elif mesaj[i] == '5':
            print('.....', end = '')
        elif mesaj[i] == '6':
            print('-....', end = '')
        elif mesaj[i] == '7':
            print('--...', end = '')
        elif mesaj[i] == '8':
            print('---..', end = '')
        elif mesaj[i] == '9':
            print('----.', end = '')
        else:
            print('',end = '')
        print(' ',end = '')
    print("")

    secim = input("Yeniden denemek ister misiniz(Evet = e , Hayır = h):").upper()
    if secim == "E":
        MorsAlfabesiDonustur()
    elif secim == "H":
        print("Bizi tercih ettiğiniz için teşekkürler :) ")

MorsAlfabesiDonustur()