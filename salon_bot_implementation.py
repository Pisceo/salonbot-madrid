#!/usr/bin/env python3
"""
SalonBot Madrid - Working Implementation
"""

import json
import random
from datetime import datetime

class SalonBot:
    def __init__(self, config_file: str = "salon_bot_config.json"):
        with open(config_file, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        self.business_info = self.config['business_info']
        self.services = self.config['services']
        self.working_hours = self.config['working_hours']
        self.intents = self.config['intents']
        self.fallback_responses = self.config['fallback_responses']
        
    def get_greeting(self):
        return {
            "message": self.config['greeting']['message'],
            "quick_replies": self.config['greeting']['quick_replies']
        }
    
    def process_message(self, user_message: str, user_id: str = "default"):
        message_lower = user_message.lower()
        
        # Simple keyword matching
        if any(word in message_lower for word in ["hola", "buenos", "buenas", "hey", "hi"]):
            return self.intents['greeting']
        elif any(word in message_lower for word in ["servicios", "precios", "cuánto", "corte", "manicura"]):
            return self.intents['services_prices']
        elif any(word in message_lower for word in ["horarios", "horario", "abren", "cierran"]):
            return self.intents['working_hours']
        elif any(word in message_lower for word in ["ubicación", "dirección", "dónde", "gran vía"]):
            return self.intents['location']
        elif any(word in message_lower for word in ["reservar", "cita", "booking", "agendar"]):
            return self.intents['booking']
        elif any(word in message_lower for word in ["contacto", "teléfono", "whatsapp", "instagram"]):
            return self.intents['contact']
        elif any(word in message_lower for word in ["preguntas", "faq", "dudas", "ayuda"]):
            return self.intents['faq']
        elif any(word in message_lower for word in ["promociones", "ofertas", "descuentos"]):
            return self.intents['promotions']
        elif any(word in message_lower for word in ["pago", "tarjeta", "efectivo", "bizum"]):
            return self.intents['payment']
        elif any(word in message_lower for word in ["cancelar", "cancelación", "anular"]):
            return self.intents['cancellation']
        elif any(word in message_lower for word in ["productos", "venden", "comprar"]):
            return self.intents['products']
        elif any(word in message_lower for word in ["hombres", "mujeres", "unisex"]):
            return self.intents['gender_services']
        elif any(word in message_lower for word in ["duración", "tiempo", "minutos", "horas"]):
            return self.intents['duration']
        elif any(word in message_lower for word in ["idiomas", "inglés", "español", "hablan"]):
            return self.intents['languages']
        else:
            return {
                "response": random.choice(self.fallback_responses),
                "quick_replies": self.config['quick_reply_templates']['main_menu']
            }
    
    def get_available_slots(self, date=None):
        demo_slots = ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00"]
        return demo_slots[:random.randint(3, 7)]
    
    def create_demo_booking(self, user_id, service, date, time):
        booking_id = f"BK{random.randint(1000, 9999)}"
        return {
            "booking_id": booking_id,
            "user_id": user_id,
            "service": service,
            "date": date,
            "time": time,
            "status": "confirmed",
            "created_at": datetime.now().isoformat()
        }

def demo_conversation():
    bot = SalonBot()
    
    print("=" * 50)
    print("SALONBOT MADRID - DEMO CONVERSATION")
    print("=" * 50)
    
    greeting = bot.get_greeting()
    print(f"🤖 Bot: {greeting['message']}")
    print(f"📱 Quick Replies: {', '.join(greeting['quick_replies'])}")
    print()
    
    demo_messages = [
        "Hola, buenos días",
        "¿Cuáles son sus servicios?",
        "¿Cuánto cuesta un corte de cabello?",
        "¿Cuáles son sus horarios?",
        "¿Dónde están ubicados?",
        "Quiero reservar una cita",
        "¿Aceptan tarjetas?",
        "¿Tienen promociones?",
        "¿Hablan inglés?",
        "algo que no entiendo"
    ]
    
    for i, message in enumerate(demo_messages, 1):
        print(f"👤 Usuario {i}: {message}")
        response = bot.process_message(message, f"user_{i}")
        print(f"🤖 Bot: {response['response']}")
        if response.get('quick_replies'):
            print(f"📱 Quick Replies: {', '.join(response['quick_replies'])}")
        print("-" * 30)
    
    print("📅 DEMO BOOKING:")
    available_slots = bot.get_available_slots()
    print(f"Slots disponibles: {', '.join(available_slots)}")
    
    booking = bot.create_demo_booking("user_1", "Corte de cabello", "2024-01-15", "10:00")
    print(f"Reserva creada: {booking}")

if __name__ == "__main__":
    demo_conversation()
