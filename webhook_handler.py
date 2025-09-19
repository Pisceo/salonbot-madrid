#!/usr/bin/env python3
"""
Webhook Handler for SalonBot Madrid
Handles incoming messages from WhatsApp, Instagram, and web platforms
"""

from flask import Flask, request, jsonify
import json
import logging
from salon_bot_implementation import SalonBot
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
bot = SalonBot()

# Platform-specific handlers
class PlatformHandler:
    @staticmethod
    def whatsapp_handler(data):
        """Handle WhatsApp webhook data"""
        try:
            # Extract message from WhatsApp webhook format
            entry = data.get('entry', [{}])[0]
            changes = entry.get('changes', [{}])[0]
            value = changes.get('value', {})
            messages = value.get('messages', [])
            
            if not messages:
                return None
            
            message = messages[0]
            user_id = message.get('from')
            message_text = message.get('text', {}).get('body', '')
            
            return {
                'user_id': user_id,
                'message': message_text,
                'platform': 'whatsapp'
            }
        except Exception as e:
            logger.error(f"WhatsApp handler error: {e}")
            return None
    
    @staticmethod
    def instagram_handler(data):
        """Handle Instagram webhook data"""
        try:
            # Extract message from Instagram webhook format
            entry = data.get('entry', [{}])[0]
            messaging = entry.get('messaging', [{}])[0]
            
            user_id = messaging.get('sender', {}).get('id')
            message_text = messaging.get('message', {}).get('text', '')
            
            return {
                'user_id': user_id,
                'message': message_text,
                'platform': 'instagram'
            }
        except Exception as e:
            logger.error(f"Instagram handler error: {e}")
            return None
    
    @staticmethod
    def web_handler(data):
        """Handle web chat data"""
        try:
            user_id = data.get('user_id', 'web_user')
            message_text = data.get('message', '')
            
            return {
                'user_id': user_id,
                'message': message_text,
                'platform': 'web'
            }
        except Exception as e:
            logger.error(f"Web handler error: {e}")
            return None

def format_response_for_platform(response, platform):
    """Format bot response for specific platform"""
    if platform == 'whatsapp':
        return {
            'messaging_product': 'whatsapp',
            'to': response.get('user_id'),
            'type': 'text',
            'text': {'body': response['message']}
        }
    elif platform == 'instagram':
        return {
            'recipient': {'id': response.get('user_id')},
            'message': {'text': response['message']}
        }
    else:  # web
        return {
            'message': response['message'],
            'quick_replies': response.get('quick_replies', [])
        }

@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """WhatsApp webhook endpoint"""
    try:
        data = request.get_json()
        logger.info(f"WhatsApp webhook received: {data}")
        
        # Handle verification
        if request.args.get('hub.verify_token') == os.getenv('WHATSAPP_VERIFY_TOKEN'):
            return request.args.get('hub.challenge')
        
        # Process message
        message_data = PlatformHandler.whatsapp_handler(data)
        if message_data:
            response = bot.process_message(
                message_data['message'], 
                message_data['user_id']
            )
            response['user_id'] = message_data['user_id']
            
            formatted_response = format_response_for_platform(response, 'whatsapp')
            return jsonify(formatted_response)
        
        return jsonify({'status': 'ok'})
    
    except Exception as e:
        logger.error(f"WhatsApp webhook error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/webhook/instagram', methods=['POST'])
def instagram_webhook():
    """Instagram webhook endpoint"""
    try:
        data = request.get_json()
        logger.info(f"Instagram webhook received: {data}")
        
        # Handle verification
        if request.args.get('hub.verify_token') == os.getenv('INSTAGRAM_VERIFY_TOKEN'):
            return request.args.get('hub.challenge')
        
        # Process message
        message_data = PlatformHandler.instagram_handler(data)
        if message_data:
            response = bot.process_message(
                message_data['message'], 
                message_data['user_id']
            )
            response['user_id'] = message_data['user_id']
            
            formatted_response = format_response_for_platform(response, 'instagram')
            return jsonify(formatted_response)
        
        return jsonify({'status': 'ok'})
    
    except Exception as e:
        logger.error(f"Instagram webhook error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/webhook/web', methods=['POST'])
def web_webhook():
    """Web chat webhook endpoint"""
    try:
        data = request.get_json()
        logger.info(f"Web webhook received: {data}")
        
        message_data = PlatformHandler.web_handler(data)
        if message_data:
            response = bot.process_message(
                message_data['message'], 
                message_data['user_id']
            )
            
            return jsonify(response)
        
        return jsonify({'error': 'Invalid data'}), 400
    
    except Exception as e:
        logger.error(f"Web webhook error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'bot_name': bot.config['bot_name']
    })

@app.route('/config', methods=['GET'])
def get_config():
    """Get bot configuration"""
    return jsonify({
        'bot_name': bot.config['bot_name'],
        'business_info': bot.business_info,
        'services': bot.services,
        'working_hours': bot.working_hours
    })

@app.route('/booking/demo', methods=['POST'])
def create_demo_booking():
    """Create a demo booking"""
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'demo_user')
        service = data.get('service', 'Corte de cabello')
        date = data.get('date', datetime.now().strftime('%Y-%m-%d'))
        time = data.get('time', '10:00')
        
        booking = bot.create_demo_booking(user_id, service, date, time)
        
        return jsonify({
            'success': True,
            'booking': booking,
            'message': f'Reserva {booking["booking_id"]} creada exitosamente'
        })
    
    except Exception as e:
        logger.error(f"Booking error: {e}")
        return jsonify({'error': 'Booking failed'}), 500

@app.route('/slots/<date>', methods=['GET'])
def get_available_slots(date):
    """Get available slots for a date"""
    try:
        slots = bot.get_available_slots(date)
        return jsonify({
            'date': date,
            'available_slots': slots,
            'is_open': bot.is_open_now()
        })
    
    except Exception as e:
        logger.error(f"Slots error: {e}")
        return jsonify({'error': 'Failed to get slots'}), 500

@app.route('/', methods=['GET'])
def index():
    """Serve the web chat interface"""
    from flask import render_template
    return render_template('index.html')

if __name__ == '__main__':
    # Set environment variables for production
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
