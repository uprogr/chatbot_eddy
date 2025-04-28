from flask import render_template
from flask_socketio import emit

class ChatbotController:
    """Handles WebSocket and HTTP requests, connects Model and View."""
    
    def __init__(self, model):
        self.model = model

    def handle_websocket_message(self, data):
        """Handle WebSocket message and emit response."""
        message = data.get('message', '')
        response = self.model.process_message(message)
        if response:
            emit('response', {'message': response})

def register_routes(app, controller):
    """Register HTTP routes."""
    @app.route("/")
    def serve_home():
        """Serve the HTML frontend (View)."""
        return render_template("index.html")
