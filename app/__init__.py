from flask import Flask
from flask_socketio import SocketIO
from app.controllers.chatbot import ChatbotController
from app.models.chatbot import ChatbotModel

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key

    # Initialize SocketIO
    socketio.init_app(app)

    # Initialize Model and Controller
    model = ChatbotModel()
    controller = ChatbotController(model)

    # Register routes
    from app.controllers.chatbot import register_routes
    register_routes(app, controller)

    # Register WebSocket handlers
    @socketio.on('message')
    def handle_message(data):
        controller.handle_websocket_message(data)

    return app
