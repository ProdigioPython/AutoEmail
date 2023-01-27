import smtplib

# Configuração do servidor e credenciais
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("seu_email@gmail.com", "sua_senha")

# Criação da mensagem
from_email = "seu_email@gmail.com"
to_email = ["destinatario1@example.com", "destinatario2@example.com"]
subject = "Assunto do email"
body = "<p>Corpo do email em HTML</p>"

message = f"Subject: {subject}\n\n{body}"

# Enviando o email
server.sendmail(from_email, to_email, message)

# Encerrando a conexão
server.quit()
