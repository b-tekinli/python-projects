print("\nDÖVİZ UYGULAMASI\n")

def TLyeCevir(tutar, dovizinCinsi):
    if dovizinCinsi == 'Dolar':
        print( tutar * 7.8)
    elif dovizinCinsi == 'Euro':
        print( tutar * 9.5)
    elif dovizinCinsi == 'Sterlin' or dovizinCinsi == 'Pound':
        print( tutar * 10.5)
    else:
        print('Bilinmiyor...')
TLyeCevir( 100, 'Dolar')