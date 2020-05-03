from loafer.managers import LoaferManager

from .routes import routes

print('Serviço Rodando... Aperte Crtl + C para pausar o serviço')

manager = LoaferManager(routes=routes)
manager.run()
