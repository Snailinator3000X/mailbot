from mailer import Mailer

mail = Mailer(email='gary.rosien@googlemail.com', password='AWlb87iNYC')

username = 'Anna'
agent = 'Harald'
subj='Wir wollen dich persönlich kennenlernen!'
msg=f'Liebe/r {username},\n\nich hoffe, dir geht es gut und du bist gesund! Ich bin {agent} von Zwopr. Vielleicht wunderst du dich, wieso ich dir schreibe. Ich habe heute die Zwopr App durchstöbert und du bist mir wegen (Kategorie, Kommentar, Helfer einsatz) ins Auge gesprungen. An dieser Stelle schon einmal Danke für deinen Einsatz. :)\n\nIch wollte dich fragen, ob du bereit wärst, mir dein Feedback zu deinen Erfahrungen bei Zwopr zu geben? Deine Meinung ist für uns wichtig.... Falls ja, wann können wir dazu mal telefonieren?\n\nIch würde mich sehr über eine Antwort und über ein Kennenlernen mit dir freuen!\n\nBis dahin wünsche ich dir eine schöne Adventszeit.\n\nDein {agent} '




mail.send(receiver='mifira5093@mmgaklan.com', subject=subj, message= msg)