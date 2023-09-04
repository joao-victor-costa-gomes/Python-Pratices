import os 
import ssl 
import smtplib 
from email.message import EmailMessage

autor = ""
destinatário = ""
senha= ""

título = "Testando enviar um email com Python"

corpo = '''
Albion Online é um MMORPG sandbox em que você escreve sua própria história, em vez de seguir um caminho pré-determinado. Explore um vasto mundo aberto que consiste de 5 ecossistemas únicos. Tudo o que você faz gera um impacto no mundo, já que em Albion, a economia é conduzida pelo jogador. Cada peça de equipamento é construída por jogadores a partir dos recursos obtidos por eles. O equipamento que você usa define quem você é. Ir de cavaleiro para feiticeiro é tão fácil quanto trocar a armadura e a arma, ou uma combinação das duas. Aventure-se no mundo aberto e enfrente os habitantes e as criaturas de Albion. Saia em expedições ou entre em masmorras para enfrentar inimigos ainda mais desafiadores. Enfrente outros jogadores em confrontos do mundo aberto, lute pelo controle de territórios ou cidades inteiras em batalhas táticas em grupo. Relaxe descansando em sua ilha pessoal, onde você pode construir uma casa, cultivar alimentos e criar animais. Junte-se à uma guilda, tudo fica mais divertido quando se trabalha em equipe. Entre hoje mesmo no mundo de Albion, e escreva sua própria história.
'''
em = EmailMessage()
em["From"] = autor 
em["To"] = destinatário
em["Subject"] = título
em.set_content(corpo) 

conteúdo = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=conteúdo) as smtp : 
    smtp.login(autor, senha)
    smtp.sendmail(autor, destinatário, em.as_string())
