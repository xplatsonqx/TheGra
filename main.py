import random
import time
from psycopg2 import connect

figury = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
kolory = ['czerwo', 'wino', 'dzwonek', 'trefl']
punktacja = {
    'kolor': len(kolory) * 10, 'figura': len(figury) * 10
}

def send_query(sql: str):
    username = "postgres"
    passwd = "kolor1234"
    hostname = "127.0.0.1"
    db_name = "Gra_DB"
    cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
        cnx.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def losowanie_kart() -> list:
    wybrana_karta = [figury[random.randint(0, len(figury) - 1)],
                     kolory[random.randint(0, len(kolory) - 1)]]
    return wybrana_karta


koniec = ''

nicki=['Gabrysia', 'Oliver', 'Mateusz']

nick_choice = input("\n1.Gabrysia\n2.Oliver\n3.Mateusz\nPodaj swoj nick: ")

nick=nicki[int(nick_choice)-1]

while not koniec == 'T':

    punktacja_total = 0
    wybrany_kolor = 'none'
    wybrana_figura = 'none'
    while not wybrana_figura in figury:
        wybrana_figura = input("\nPodaj figure [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']: ")
    while not wybrany_kolor in kolory:
        wybrany_kolor = input("\nPodaj kolor ['czerwo', 'wino', 'dzwonek', 'trefl']: ")

    print(f"Twoja wybrana karta to: <<<< {wybrana_figura} {wybrany_kolor} >>>>")
    print(f"TRWA LOSOWANIE")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)

    wylosowany_kolor = losowanie_kart()[1]
    wylosowana_figura = losowanie_kart()[0]

    print(f"Twoja wylosowana karta to: <<<< {wylosowana_figura} {wylosowany_kolor} >>>>")

    time.sleep(1)

    if wybrany_kolor == wylosowany_kolor:
        print(f"\n\n\n\n\nSUKCES Twoj kolor jest taki sam jak wylosowany. Otrzymujesz {punktacja['kolor']} pkt.")
        punktacja_total += punktacja['kolor']
    else:
        print(
            f"\nna kolory SKUCHA. Otrzumujesz 0 pkt.")

    if wybrana_figura == wylosowana_figura:
        print(f"\n\n\n\n\nSUKCES Twoja figura jest taka sama jak wylosowana. Otrzymujesz {punktacja['figura']} pkt.")
        punktacja_total += punktacja['figura']
    else:
        print(
            f"\nna figury SKUCHA. Otrzumujesz 0 pkt.")

    sql = f'''
        INSERT INTO public."Score_table" (date, nick, score) 
        VALUES (CURRENT_DATE, '{nick}', {punktacja_total});
    '''
    send_query(sql)

    koniec = input(f"\n{nick}!!!! \nTwoje zdobyte punkty w tej sesji {punktacja_total}\n Chcesz skonczyc?['T','N']: ")
