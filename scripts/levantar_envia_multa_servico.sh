echo "Levantando veiculo-api venv"
cd ../envia-multa-servico

# Criando topico e filas
docker start goaws
source .venv2/bin/activate
aws --endpoint-url http://localhost:4100 sns create-topic --name multa__criada
aws --endpoint-url http://localhost:4100 sqs create-queue --queue-name envia_multa_servico__multa__criada
aws --endpoint-url http://localhost:4100 sns subscribe \
--topic-arn arn:aws:sns:us-east-1:000000000000:multa__criada \
--protocol sqs --notification-endpoint http://us-east-1.goaws.com:4100/100010001000/envia_multa_servico__multa__criada

# Iniciando o serviço
source .venv/bin/activate
python -m envia_multa_servico
