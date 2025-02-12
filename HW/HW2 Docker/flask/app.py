import os
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response(
        {
            'response': 'Hello, World!',
            'status': 200
        }
    )
    return response

@app.route('/repeat', methods=['GET'])
def repeat():
    user_input = request.args.get('input', 'No input provided')  # Get 'input' param
    response = make_response(
        {
            "body": user_input,
            "status": 200
        }
    )
    return response

@app.route('/health')
@app.route('/healthcheck')
def health():
    response = make_response(
        {
            'body': 'OK',
            'status': 200
        }
    )
    return response



if __name__ == '__main__':
    # Get the port from the environment variable, defaulting to 5000 if not set
    port = int(os.getenv('PORT', 5000))
    
    # Run the app on host '0.0.0.0' to make it accessible on any IP address and use the port from the environment
    app.run(host='0.0.0.0', port=port, debug=True)
