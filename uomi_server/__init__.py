# from uomi_server.__main__ import main

import connexion
import logging
from uomi_server import encoder

# main()
logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'UOMI API'})
app.run()
