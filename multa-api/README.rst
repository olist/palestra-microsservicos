=========
multa-api
=========

API de multas que armazena informações sobre multas.

.. image:: ../imagens/multa-api.png


Endpoints
---------

Listagem de Multas
^^^^^^^^^^^^^^^^^^

Requisição
##########

**GET** http://localhost:8001/v1/multas/

Resposta
########

HTTP status code 200 OK

.. code-block:: json

    [
        {"id":1,"placa":"kkk-1111","tipo":1},
        {"id":2,"placa":"kkk-2222","tipo":1},
        {"id":3,"placa":"kkk-3333","tipo":2},
        {"id":4,"placa":"kkk-4444","tipo":2}
    ]


Criação de Multas
^^^^^^^^^^^^^^^^^

Tipos de multas:
    - 1  ( Sinal Vermelho )
    - 2  ( Trafegando em contra mão )
    - 3  ( Estacionado em local proibido )

Requisição
##########

**POST** http://localhost:8001/v1/multas/


**Payload**

.. code-block:: json

    {
        "tipo": 1,
        "placa": "kkk-1111"
    }

Resposta
########

HTTP status code 201 Created

.. code-block:: json

    {
        "id": 1,
        "tipo": 1,
        "placa": "kkk-1111"
    }

Requisição
##########

**POST** http://localhost:8001/v1/multas/


**Payload**

.. code-block:: json

    {}

Resposta
########

HTTP status code 400 Bad Request

.. code-block:: json

    {
        "placa": ["This field is required."],
        "tipo": ["This field is required."]
    }

Busca de uma multa
^^^^^^^^^^^^^^^^^^

Requisição
##########

**GET** http://localhost:8001/v1/multas/66/

Resposta
########

HTTP status code 200 OK

.. code-block:: json

    {
        "id": 66,
        "tipo": 1,
        "placa": "kkk-1111"
    }

Requisição
##########

**GET** http://localhost:8001/v1/multas/id-multa-inexistente/

Resposta
########

HTTP status code 404 Not Found

.. code-block:: json

    {
        "detail": "Not found."
    }