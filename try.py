




nick = "Kurczaczek"
punktacja_total = 12000
sql = f'''
    INSERT INTO public."Score_table" (date, nick, score) 
    VALUES (CURRENT_DATE, '{nick}', {punktacja_total});
'''

send_query(sql)
