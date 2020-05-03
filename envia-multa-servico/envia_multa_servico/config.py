from decouple import config


class Settings:
    AWS_DEFAULT_REGION = config("AWS_DEFAULT_REGION")
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_ENDPOINT_URL = config("AWS_ENDPOINT_URL", default=None)

    MULTA_CRIADA_FILA = config("MULTA_CRIADA_FILA")

    VEICULO_API_URL = config("VEICULO_API_URL")
    SENDGRID_API_KEY = config("SENDGRID_API_KEY")


settings = Settings()
