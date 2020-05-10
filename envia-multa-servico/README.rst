===================
envia-multa-servico
===================

Serviço que faz envio de multas que foram criadas em multa-api para o email dos proprietarios dos veiculos multados.

Para realização do envio de multas por emails estamos usando o servico de envio de emails do `Sendgrid`_.
Portanto você precisará setar a api key na envvar SENDGRID_API_KEY no arquivo .env.

Para obter a api key você deverá criar uma conta no sendgrid.
Você não terá custos para ter uma conta no sendgrid .

.. _Sendgrid: https://sendgrid.com/
