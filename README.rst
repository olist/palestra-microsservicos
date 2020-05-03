===========================================================================
Palestra Desvendando uma arquitetura de microsserviços baseada em eventos
===========================================================================

O projeto exemplifica uma simples plataforma de um Departamento de Trânsito, onde
multas são cadastradas e as mesmas são enviadas para os emails dos Proprietários.

Para a construção dessa plataforma de microsserviços, foi utilizada as seguintes tecnologias:

- `Boto3`_: É o SDK da AWS para Python, que permite desenvolvedores Python utilizarem serviços como o Amazon SNS e SQS em suas aplicações;
- `Django`_: É um framework Web open source que lhe permitirá escrever aplicações web sem precisar reinventar a roda;
- `Django Rest Framework`_: É um kit de ferramentas que auxilia na criação de APIs REST em cima do framework Django;
- `Loafer`_: É um biblioteca que auxilia na contrução de aplicações assíncronas que consumem mensagens enviadas para filas SQS;
- `SQS`_: É um serviço da AWS de filas de mensagens que permite o desacoplamento e a escalabilidade de microsserviços. Nosso microsserviço obterá as mensagens por meio de um fila SQS.
- `SNS`_: É um serviço da AWS de publicação de mensagens em tópicos que permite o desacoplamento de microsserviços. Nossa API irá publicar mensagens em um determinado tópico que possui uma fila SQS inscrita.

.. _Boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
.. _Django: https://www.djangoproject.com/
.. _Django Rest Framework: https://www.django-rest-framework.org/
.. _Loafer: https://loafer.readthedocs.io/en/latest/
.. _SQS: https://aws.amazon.com/pt/sqs/
.. _SNS: https://aws.amazon.com/pt/sns/


Diagrama de Fluxo de Funcionamento da plataforma
-------------------------------------------------

.. image:: imagens/fluxo-multa.png


Configurando o Projeto
-----------------------

1. Antes de tudo faça o clone do projeto executando o comando abaixo.

.. code-block:: console

   $ git clone git@github.com:olist/palestra-microservicos.git
   $ cd palestra-microservicos

2. Para instalar as dependências das aplicações você deve ter o `pipenv`_ instalado. Para isso execute a lia abaixo no terminal.

.. code-block:: console

   ~/palestra-microservicos $ pip install pipenv

3. Após ter instalado o pipenv, devemos instalar as dependências das 3 aplicações: multa-api, veiculo-api, envia-multa-servico, executando o comando abaixo.

.. code-block:: console

   ~/palestra-microservicos $ make instalar_dependencias

4. Após ter instalado as dependências devemos rodar as migrações das apis.

.. code-block:: console

   ~/palestra-microservicos $ make migrar_bancos


.. _pipenv: https://pipenv.pypa.io/en/latest/
