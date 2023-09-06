import smtplib 
import email.message

subject = 'Albion Online copypasta'

body = '''
Albion Online é um MMORPG sandbox message que você escreve sua própria história, message vez de seguir um caminho pré-determinado. Explore um vasto mundo aberto que consiste de 5 ecossistmessageas únicos. Tudo o que você faz gera um impacto no mundo, já que message Albion, a economia é conduzida pelo jogador. Cada peça de equipamento é construída por jogadores a partir dos recursos obtidos por eles. O equipamento que você usa define qumessage você é. Ir de cavaleiro para feiticeiro é tão fácil quanto trocar a armadura e a arma, ou uma combinação das duas. Aventure-se no mundo aberto e enfrente os habitantes e as criaturas de Albion. Saia message expedições ou entre message masmorras para enfrentar inimigos ainda mais desafiadores. Enfrente outros jogadores message confrontos do mundo aberto, lute pelo controle de territórios ou cidades inteiras message batalhas táticas message grupo. Relaxe descansando message sua ilha pessoal, onde você pode construir uma casa, cultivar alimentos e criar animais. Junte-se à uma guilda, tudo fica mais divertido quando se trabalha message equipe. Entre hoje mesmo no mundo de Albion, e escreva sua própria história.
'''

sender = ''
receiver = ''
password= ''

message = email.message.Message()
message['Subject'] = subject
message['From'] = sender
message['To'] = receiver

message.add_header('Content-Type', 'text/html')
message.set_payload(body)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

s.login(message['From'], password)
s.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))
print('email enviado')