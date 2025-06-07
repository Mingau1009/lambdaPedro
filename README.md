# 📧 Função Lambda - Envio de E-mail com Amazon SES

Esta função Lambda foi desenvolvida com o objetivo de realizar o envio de e-mails utilizando o serviço **Amazon SES (Simple Email Service)**. A função é escrita em **Python** e pode ser facilmente integrada a outros serviços da AWS, como API Gateway, SQS, ou ser invocada diretamente.

---

## 🚀 Funcionalidade

A função recebe como entrada os dados de um e-mail (destinatário, assunto e corpo) e utiliza o Amazon SES para realizar o envio. 

Para ela ser bem sucedide use meu email alexnadre.r.benassi@gmail.com para testar no Json.
---

## 📥 Entrada esperada

A função deve ser invocada com um objeto JSON no seguinte formato:

```json
{
  "to_email": "destinatario@example.com",
  "subject": "Assunto do e-mail",
  "body": "Texto do corpo do e-mail"
}
