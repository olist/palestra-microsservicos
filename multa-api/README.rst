===========
multa-api
===========

API de multas que armazena informações sobre multas

.. image:: ../imagens/multa-api.png


Endpoints
---------

Listagem de Multas
^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Método", "URI"
   :widths: 10, 30

   "GET", "/v1/multas/"


Respostas esperadas
####################

1 - HTTP status code 200 OK

.. code-block:: json

    [
        {"id":1,"placa":"kkk-1111","tipo":1},
        {"id":2,"placa":"kkk-2222","tipo":1},
        {"id":3,"placa":"kkk-3333","tipo":2},
        {"id":4,"placa":"kkk-4444","tipo":2}
    ]


Criação de Multas
^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Método", "URI"
   :widths: 10, 30

   "POST", "/v1/multas/"

Estrutura do payload a ser enviado
##################################

.. code-block:: json

    {
        "tipo": 1,
        "placa": "kkk-1111"
    }

Tipos de multas:
    - 1  ( Sinal Vermelho )
    - 2  ( Trafegando em contra mão )
    - 3  ( Estacionado em local proibido )

Campos obrigatórios:
    - tipo
    - placa

Respostas esperadas
###################

1 - HTTP status code 201 Created

.. code-block:: json

    {
        "id": 1,
        "tipo": 1,
        "placa": "kkk-1111"
    }

2 - HTTP status code 400 Bad Request

.. code-block:: json

    {
        "placa": ["This field is required."],
        "tipo": ["This field is required."]
    }

Busca de uma multa
^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Método", "URI"
   :widths: 10, 30

   "GET", "/v1/multas/<id-multa>/"

Respostas esperadas
###################

1 - HTTP status code 200 OK

.. code-block:: json

    {
        "id": 1,
        "tipo": 1,
        "placa": "kkk-1111"
    }

2 - HTTP status code 404 Not Found

.. code-block:: json

    {
        "detail": "Not found."
    }


