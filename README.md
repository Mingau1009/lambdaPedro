# Função Lambda: Envio de E-mail com AWS SES

## Descrição
Essa função Lambda envia e-mails utilizando o Amazon SES. Ela é escrita em Python e foi criada com foco em simplicidade e praticidade.

## Entrada esperada (event)
```json
{
  "to_email": "destinatario@example.com",
  "subject": "Assunto do E-mail",
  "body": "Texto do corpo do e-mail."
}
