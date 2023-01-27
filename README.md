

Importar a biblioteca smtplib: Essa biblioteca fornece as funções necessárias para enviar e-mails através de um servidor SMTP.

Configurar o servidor e as credenciais: Usando a função SMTP(), especificamos o endereço do servidor SMTP do Gmail (smtp.gmail.com) e a porta (587) que será usada para conectar. Em seguida, usamos a função starttls() para iniciar uma conexão segura com o servidor e a função login() para fazer login com as credenciais do nosso e-mail e senha.

Criar a mensagem: Nessa etapa, definimos as informações básicas da mensagem, como o remetente, os destinatários, assunto e corpo do e-mail. O corpo do e-mail está em formato HTML, mas pode ser mudado para texto puro.

Enviar a mensagem: Usamos a função sendmail() fornecida pela biblioteca smtplib para enviar a mensagem. Essa função requer três argumentos: o remetente, os destinatários e a mensagem propriamente dita.

Encerrar a conexão: Finalmente, usamos a função quit() para encerrar a conexão com o servidor de e-mail.

É importante lembrar que para usar o serviço de email do Gmail, é necessário permitir aplicativos menos seguros no seu email do google.
Caso tenha alguma dúvida, por favor, pergunte.
