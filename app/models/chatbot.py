import re

class ChatbotModel:
    """Handles chatbot logic and data processing."""
    
    def __init__(self):
        # Predefined response patterns with conversational Mongolian style
        self.patterns = [
            {
                "regex": re.compile(r"(?i)сайн байна уу|сайн уу|сәлем"),
                "reply": "Сайн байна уу! Яг юуг ярилчихъя? 😎"
            },
            {
                "regex": re.compile(r"(?i)байна уу|байнуу"),
                "reply": "Байна шүү, байна! 😄 Чи яг юуг хэлчихъя гээд байна вэ?"
            },
            {
                "regex": re.compile(r"(?i)нэр чинь хэн бэ|чи хэн вэ"),
                "reply": "Би энгийн чатбот, гэхдээ гоё туслагч шүү! 😊 Чиний нэр хэн бэ?"
            },
            {
                "regex": re.compile(r"(?i)баярлалаа|баярлаа"),
                "reply": "За за, таатай байна! Дахин юуг хөөрөлдчихъя?"
            },
            {
                "regex": re.compile(r"(?i)цаг хэд вэ|одоо хэд вэ"),
                "reply": "Цаг бол миний хувьд таныг инээлгэх цаг л байна шүү! 😜 Юуг ярьъя?"
            },
            {
                "regex": re.compile(r"(?i)юу байна вэ|юу болж байна вэ"),
                "reply": "Юу ч болоогүй, гэхдээ чи надад мессеж биччихлээ! 😄 Яг юуг ярилъя?"
            },
        ]

    def process_message(self, message):
        """Process incoming message and return response."""
        if not message or not message.strip():
            return None
        
        input_text = message.lower()
        response_msg = "Уучлаарай, би тэр юуг хэлчихснийг сайн ойлгосонгүй. Дахин хэлчих! 😊"
        
        for pattern in self.patterns:
            if pattern["regex"].search(input_text):
                response_msg = pattern["reply"]
                break
        
        return response_msg
