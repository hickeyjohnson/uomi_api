"""Main file to run server"""

import connexion
import logging
from uomi_server import encoder

def main():
    """
    main function
    """
    logging.basicConfig(level=logging.INFO)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'UOMI API'})
    app.run()


if __name__ == '__main__':
    main()
