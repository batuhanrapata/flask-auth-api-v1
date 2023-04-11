from flask import Flask
from resources.routes import initialize_routes
from flask_restful import Api
from utils.exceptions import errors
from dotenv import load_dotenv


load_dotenv()


app=Flask(__name__)
api=Api(app, errors=errors)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
