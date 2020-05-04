import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .config import settings


def envia_multa_handler(multa_mensagem, metadata):
    print("Uma multa chegou no serviço")

    sendgrid_api_key = settings.SENDGRID_API_KEY

    if not sendgrid_api_key:
        print("Para mandar email configure a api key do sendgrid!")
        return

    response = requests.get(
        f"{settings.VEICULO_API_URL}/v1/carros/{multa_mensagem['placa']}"
    )

    veiculo = response.json()

    conteudo = f"""
    <h2>{veiculo['proprietario']['nome']} Você foi Multado!</h2>
    <hr>
    <h4>Veiculo: {veiculo['modelo']} </3>
    <h4>Placa:{veiculo['placa']} </3>
    <h4>Multa: {multa_mensagem['tipo']['descricao']}</h3>
    <h4>Valor: {multa_mensagem["tipo"]['valor']} </3>
    """

    mensagem_email = Mail(
        from_email='contato@multa.com',
        to_emails=veiculo["proprietario"]["email"],
        subject="Você foi multado",
        html_content=conteudo
    )
    sendgrid = SendGridAPIClient(settings.SENDGRID_API_KEY)
    sendgrid.send(mensagem_email)

    print("Email enviado!")

    return True
