from flask import Flask, jsonify
from flask_restful import Api, Resource
from fetching_data import Fetching as fs
from clean_train_test_data import Clean_spliting_data as csd
from prediction_method import Prediction as pr
from pyngrok import ngrok
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app and Api
app = Flask(__name__)
api = Api(app)

# Define the Resource
class CompanyData(Resource):
    def get(self):
        data = pr.final_pred
        companies = []
        j = 0
        for i in data.keys():
            companies.append({
                "company_name": i,
                "symbol": fs.symbols[j],
                "open_price": csd.final_data[i]['open'].iloc[-1],
                "close_price": csd.final_data[i]['close'].iloc[-1],
                "actual_timeframe": list(csd.final_data[i]['close'][-7:].values),
                "prediction": list(data[i][0])
            })
            j += 1
        return jsonify(companies)

# Add the resource to the API
api.add_resource(CompanyData, '/api/data')

# Set up ngrok and start the Flask a
NGROK_AUTH = os.getenv("NGROK_AUTH")

    # Check if ngrok auth token is loaded correctly
if NGROK_AUTH is None:
    print("Error: ngrok authentication token is not set. Please check your .env file.")
    exit(1)

    # Authenticate ngrok
ngrok.set_auth_token(NGROK_AUTH)

# Open a tunnel on port 5000
tunnel = ngrok.connect(5000,domain = 'gorilla-sacred-bison.ngrok-free.app')
print(f"Public URL: {tunnel.public_url}")

# Run the Flask app
app.run(host='0.0.0.0', port=5000)
