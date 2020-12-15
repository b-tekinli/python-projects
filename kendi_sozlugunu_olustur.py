#encoding:utf-8

import shelve

tr_dict = "tr_dict.txt"
eng_dict = "eng_dict.txt"

tr = shelve.open(tr_dict)
eng = shelve.open(eng_dict)

print("Welcome to Your Dictionary :D")

while True:
    lang = input("1. Turkish - English\n2. English -Turkish\n-Write 1 or 2-\nSelect dictionary language: ").lower()
    if lang == "1":
        word = input("Enter the Turkish word you want to translate into English: ").lower()
        if word in tr:
            print(f"{word}, meaning of word: ,",tr[word])
        else:
            addition = input("This word is not defined in the dictionary. Type 'add' to define: ").lower()
            if addition == "add":
                additive = input("Enter the English meaning of the word: ")
                tr[word] = additive
                print(f"{word}, meaning of word: '{additive}' defined as.")
    if lang == "2":
        word = input("Enter the English word you want to translate into Turkish: ").lower()
        if word in eng:
            print(f"{word}, meaning of word: ,",eng[word])
        else:
            addition = input("This word is not defined in the dictionary. Type 'add' to define: ").lower()
            if addition == "add":
                additive = input("Enter the Turkish meaning of the word: ")
                tr[word] = additive
                print(f"{word}, meaning of word: , {additive} defined as.")

tr.close()
eng.close()