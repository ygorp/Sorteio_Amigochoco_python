from random import randint
import smtplib
from email.mime.text import MIMEText

class Amigo:
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        

class AmigoChoco:
    
    def __init__(self, quantidade_amigos):
        self.quantidade_amigos = quantidade_amigos
        self.amigos = []
        self.amigos_aux = []
        
    def obter_pessoas(self):
        
        for i in range(self.quantidade_amigos):
            print(f'---- AMIGO {i+1} ----')
            nome = input('Nome: ')
            email = input('E-mail: ')
            
            try:
                self.amigos.append(Amigo(nome, email))
                self.amigos_aux.append(Amigo(nome, email))
                print('Amigo criado com sucesso!')
            except:
                print('Erro ao criar amigo.')
    
    def sortear(self):
        self.sorteio = {}
        
        for amigo in self.amigos:
            index = randint(0, len(self.amigos_aux)-1)
            
            while amigo.nome == self.amigos_aux[index].nome:
                index = randint(0, len(self.amigos_aux)-1)
            
            self.sorteio[amigo] = self.amigos_aux[index]
            print(f'{amigo.nome} sorteou {self.amigos_aux[index].nome}')
            
            # Envie o e-mail para o amigo sorteado
            self.enviar_email(amigo.email, self.amigos_aux[index].nome)
            
            del self.amigos_aux[index]
    
    def enviar_email(self, destinatario, nome_sorteado):
        remetente = 'ygorpacheco92@gmail.com'
        senha = 'analaura7292'
        
        assunto = 'Resultado do Amigo Secreto'
        mensagem = f'Olá!\n\nVocê tirou: {nome_sorteado}\n\nFeliz Natal!'
        
        # Configuração do servidor SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        
        # Criação da mensagem MIME
        msg = MIMEText(mensagem)
        msg['Subject'] = assunto
        msg['From'] = remetente
        msg['To'] = destinatario
        
        # Envio do e-mail
        server.sendmail(remetente, destinatario, msg.as_string())
        
        # Fechamento da conexão
        server.quit()
        

# Exemplo de uso
amigo_choco = AmigoChoco(3)
amigo_choco.obter_pessoas()
amigo_choco.sortear()
