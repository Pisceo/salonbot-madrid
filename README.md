# 💇‍♀️ SalonBot Madrid - AI Chatbot for Salon/Barbershop

A complete AI chatbot agent for a Madrid salon/barbershop that can be deployed to WhatsApp, Instagram, and web platforms.

## 🚀 Features

### ✅ Core Capabilities
- **FAQ Responses**: Hours, location, services, prices, payments, booking, cancellations, products, gender services, duration, languages
- **Appointment Booking**: Demo/fake booking system with slot availability
- **Service Details**: Complete service information with durations and prices
- **Working Hours**: Real-time business hours information
- **Location Info**: Madrid address with transport information
- **Contact Methods**: WhatsApp, Instagram DM, web form integration
- **Professional Tone**: Friendly, Instagram-style communication
- **Conversation Starters**: Interactive buttons and quick replies
- **Fallback Responses**: Handles unrecognized messages gracefully

### 🏢 Madrid-Specific Features
- **Location**: Calle Gran Vía 123, 28013 Madrid
- **Contact**: +34 600 123 456 (WhatsApp & Phone)
- **Transport**: Metro and bus information
- **Languages**: Spanish (primary) with English support

### 💅 Service Categories
- **Hair Services**: Corte de cabello (25€, 45min), Coloración (50€, 90min)
- **Nail Services**: Manicura (15€, 45min), Pedicura (20€, 60min)
- **Beauty Services**: Tratamiento facial (35€, 60min), Masaje (40€, 60min)

## 📁 Files Included

```
SalonBotDemo/
├── salon_bot_config.json          # Complete chatbot configuration
├── salon_bot_implementation.py    # Python implementation with demo
├── webhook_handler.py             # Webhook handler for all platforms
├── requirements.txt               # Python dependencies
├── deployment_guide.md            # Detailed deployment instructions
├── templates/
│   └── index.html                 # Web chat interface
├── static/                        # Static files directory
└── README.md                      # This file
```

## 🛠️ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Demo Conversation
```bash
python salon_bot_implementation.py
```

### 3. Start Web Server
```bash
python webhook_handler.py
```
Then open: http://localhost:5000

## 🎯 Demo Conversation Examples

### Service Information
- **User**: "¿Cuáles son sus servicios?"
- **Bot**: Lists all services with prices and durations
- **Quick Replies**: More info by category, booking options

### Booking Process
- **User**: "Quiero reservar una cita"
- **Bot**: Provides contact methods and available slots
- **Quick Replies**: WhatsApp, Instagram, web booking

### Location & Hours
- **User**: "¿Dónde están ubicados?"
- **Bot**: Full address with transport information
- **User**: "¿Cuáles son sus horarios?"
- **Bot**: Complete weekly schedule

## 🌐 Platform Deployment

### WhatsApp Business API
1. Set up WhatsApp Business API account
2. Configure webhook: `https://your-domain.com/webhook/whatsapp`
3. Update verification tokens in environment variables

### Instagram Direct Messages
1. Create Facebook Developer account
2. Set up Instagram Business account
3. Configure webhook: `https://your-domain.com/webhook/instagram`

### Web Chat Widget
1. Deploy webhook handler to your server
2. Access web interface at root URL
3. Customize styling and branding

## ⚙️ Configuration

### Business Information
Edit `salon_bot_config.json`:
```json
"business_info": {
  "name": "Your Salon Name",
  "address": "Your Address",
  "phone": "Your Phone",
  "whatsapp": "Your WhatsApp"
}
```

### Services & Pricing
Modify the services array:
```json
"services": [
  {
    "name": "Service Name",
    "duration": "45 min",
    "price": "25€",
    "description": "Service description"
  }
]
```

### Working Hours
Update business hours:
```json
"working_hours": {
  "monday": "09:00 - 20:00",
  "tuesday": "09:00 - 20:00"
}
```

## 🔧 Customization

### Adding New Intents
1. Add to `intents` section in config
2. Define patterns and response
3. Include quick replies if needed

### Modifying Responses
1. Update response text in config
2. Add emojis and formatting
3. Test with demo script

### Adding New Services
1. Add to `services` array
2. Update service category responses
3. Test booking flow

## 📊 API Endpoints

### Webhook Endpoints
- `POST /webhook/whatsapp` - WhatsApp messages
- `POST /webhook/instagram` - Instagram messages
- `POST /webhook/web` - Web chat messages

### Utility Endpoints
- `GET /health` - Health check
- `GET /config` - Bot configuration
- `POST /booking/demo` - Create demo booking
- `GET /slots/<date>` - Get available slots

## 🧪 Testing

### Manual Testing
```bash
# Run demo conversation
python salon_bot_implementation.py

# Test specific intents
python -c "
from salon_bot_implementation import SalonBot
bot = SalonBot()
response = bot.process_message('¿Cuáles son sus horarios?')
print(response)
"
```

### Web Interface Testing
1. Start server: `python webhook_handler.py`
2. Open: http://localhost:5000
3. Test conversation flows
4. Verify quick replies work

## 🚀 Production Deployment

### Environment Variables
```bash
export WHATSAPP_VERIFY_TOKEN="your_whatsapp_token"
export INSTAGRAM_VERIFY_TOKEN="your_instagram_token"
export PORT=5000
export DEBUG=False
```

### Security Considerations
- Use HTTPS for all webhooks
- Validate incoming requests
- Implement rate limiting
- Store sensitive data securely

### Monitoring
- Log all conversations
- Track intent accuracy
- Monitor response times
- Set up error alerts

## 📱 Platform-Specific Features

### WhatsApp
- Rich message formatting
- Quick reply buttons
- Media message support
- Business profile integration

### Instagram
- Story mention handling
- Direct message threading
- Media sharing support
- Business account features

### Web
- Responsive chat interface
- Real-time messaging
- Custom styling options
- Analytics integration

## 🎨 Customization Options

### Styling
- Modify CSS in `templates/index.html`
- Update color scheme and fonts
- Add salon branding elements
- Customize chat bubble design

### Functionality
- Add new conversation flows
- Implement payment integration
- Connect to real booking system
- Add multilingual support

## 📞 Support & Contact

For questions or customization requests:
- Review the configuration file
- Check the implementation code
- Test with the demo script
- Refer to deployment guide

## 📄 License

This is a demo project for educational purposes. Feel free to modify and use for your salon business.

---

**Ready to deploy your salon chatbot!** 🚀

The bot is fully functional with fake data and can be easily customized for your specific salon needs.
