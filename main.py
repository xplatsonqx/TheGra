import random
import time
from psycopg2 import connect

figury = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
kolory = ['czerwo', 'wino', 'dzwonek', 'trefl']
punktacja = {'kolor': len(kolory) * 10, 'figura': len(figury) * 10}


class Card:
    def __init__(self, figura, kolor):
        self.kolor = kolor
        self.figura = figura


def send_query(sql):
    with connect(user="postgres", password="kolor1234", host="127.0.0.1", database="Gra_DB") as cnx:
        with cnx.cursor() as cursor:
            try:
                cursor.execute(sql)
                cnx.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
                cnx.rollback()


def losowanie_kart():
    return [random.choice(figury), random.choice(kolory)]


nicki = ['Gabrysia', 'Oliver', 'Mateusz']
nick = nicki[int(input("\n1.Gabrysia\n2.Oliver\n3.Mateusz\nPodaj swoj nick: ")) - 1]

while input(f"\n{nick}!!!! \nTwoje zdobyte punkty w tej sesji {punktacja_total}\n Chcesz skonczyc?['T','N']: ") != 'T':
    punktacja_total = 0
    wybrana_figura = ''
    wybrany_kolor = ''
    while wybrana_figura not in figury:
        wybrana_figura = input("\nPodaj figure [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']: ")
    while wybrany_kolor not in kolory:
        wybrany_kolor = input("\nPodaj kolor ['czerwo', 'wino', 'dzwonek', 'trefl']: ")

    print(f"Twoja wybrana karta to: <<<< {wybrana_figura} {wybrany_kolor} >>>>")
    print("TRWA LOSOWANIE")
    for i in [3, 2, 1]:
        print(i)
        time.sleep(1)

    wylosowana_figura, wylosowany_kolor = losowanie_kart()

    print(f"Twoja wylosowana karta to: <<<< {wylosowana_figura} {wylosowany_kolor} >>>>")

    if wybrany_kolor == wylosowany_kolor:
        print(f"SUKCES Twoj kolor jest taki sam jak wylosowany. Otrzymujesz {punktacja['kolor']} pkt.")
        punktacja_total += punktacja['kolor']
    else:
        print("na kolory SKUCHA. Otrzumujesz 0 pkt.")

    if wybrana_figura == wylosowana_figura:
        print(f"SUKCES Twoja figura jest taka sama jak wylosowana. Otrzymujesz {punktacja['figura']} pkt.")
        punktacja_total += punktacja['figura']
    else:
        print("na figury SKUCHA. Otrzumujesz 0 pkt.")

    sql = f'''
        INSERT INTO public."Score_table" (date, nick, score) 
        VALUES (CURRENT_DATE, '{nick}', {punktacja_total});
    '''
    send_query(sql)
