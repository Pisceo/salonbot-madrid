# SalonBot Madrid - Deployment Guide

## Overview
This is a complete AI chatbot for a Madrid salon/barbershop that can be deployed to WhatsApp, Instagram, and web platforms.

## Files Included
- `salon_bot_config.json` - Complete chatbot configuration
- `salon_bot_implementation.py` - Python implementation with demo
- `webhook_handler.py` - Webhook handler for different platforms
- `requirements.txt` - Python dependencies

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Demo
```bash
python salon_bot_implementation.py
```

### 3. Test Configuration
```bash
python -c "from salon_bot_implementation import SalonBot; bot = SalonBot(); print('✅ Configuration loaded successfully')"
```

## Platform Deployment

### WhatsApp Business API
1. Set up WhatsApp Business API account
2. Configure webhook URL: `https://your-domain.com/webhook/whatsapp`
3. Use the provided webhook handler
4. Update `deployment_config.webhook_url` in config

### Instagram Direct Messages
1. Set up Facebook Developer account
2. Create Instagram Business account
3. Configure webhook for Instagram messaging
4. Use webhook URL: `https://your-domain.com/webhook/instagram`

### Web Chat Widget
1. Deploy webhook handler to your server
2. Create web chat interface
3. Connect to webhook endpoint
4. Customize UI with salon branding

## Configuration Customization

### Business Information
Update in `salon_bot_config.json`:
```json
"business_info": {
  "name": "Your Salon Name",
  "address": "Your Address",
  "phone": "Your Phone",
  "whatsapp": "Your WhatsApp",
  "instagram": "@your_instagram"
}
```

### Services and Prices
Modify the `services` array:
```json
"services": [
  {
    "name": "Service Name",
    "duration": "45 min",
    "price": "25€",
    "description": "Service description",
    "category": "category"
  }
]
```

### Working Hours
Update `working_hours`:
```json
"working_hours": {
  "monday": "09:00 - 20:00",
  "tuesday": "09:00 - 20:00",
  // ... etc
}
```

## Features Included

### ✅ Core Features
- [x] FAQ responses (hours, location, services, prices, payments, booking, cancellations, products, gender services, duration, languages)
- [x] Appointment booking system (demo/fake)
- [x] Service details with durations and prices
- [x] Working hours information
- [x] Location info with fake Madrid address
- [x] Contact methods (WhatsApp, Instagram DM, web form)
- [x] Friendly, professional tone
- [x] Conversation starters/buttons
- [x] Fallback responses for unrecognized messages

### ✅ Madrid-Specific Features
- [x] Madrid location (Calle Gran Vía 123, 28013 Madrid)
- [x] Spanish phone number (+34 600 123 456)
- [x] Metro and bus information
- [x] Spanish language support with English fallback

### ✅ Service Categories
- [x] Hair services (Corte, Coloración)
- [x] Nail services (Manicura, Pedicura)
- [x] Beauty services (Facial, Masaje)
- [x] Realistic pricing in euros
- [x] Accurate duration estimates

### ✅ Conversation Flows
- [x] Greeting and welcome
- [x] Service information
- [x] Booking process
- [x] Contact information
- [x] FAQ responses
- [x] Promotions and special offers
- [x] Fallback handling

## Testing

### Manual Testing
Run the demo conversation:
```bash
python salon_bot_implementation.py
```

### API Testing
Test individual intents:
```python
from salon_bot_implementation import SalonBot
bot = SalonBot()
response = bot.process_message("¿Cuáles son sus horarios?")
print(response)
```

## Customization Options

### Adding New Intents
1. Add new intent to `intents` section in config
2. Define patterns and response
3. Add quick replies if needed

### Modifying Responses
1. Update response text in config
2. Add emojis and formatting
3. Test with demo script

### Adding New Services
1. Add to `services` array
2. Update service category responses
3. Test booking flow

## Production Deployment

### Security
- Use HTTPS for webhooks
- Validate incoming requests
- Implement rate limiting
- Store sensitive data securely

### Monitoring
- Log all conversations
- Track intent accuracy
- Monitor response times
- Set up alerts for errors

### Scaling
- Use Redis for session storage
- Implement load balancing
- Cache frequent responses
- Optimize database queries

## Support
For questions or customization requests, refer to the configuration file and implementation code.
