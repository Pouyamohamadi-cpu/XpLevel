from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ایجاد نمونه‌ای از چت‌بات
chatbot = ChatBot('SimpleBot')

# تنظیم مربی برای چت‌بات
trainer = ChatterBotCorpusTrainer(chatbot)

# آموزش چت‌بات با استفاده از داده‌های پیش‌فرض
trainer.train('chatterbot.corpus.english')

# حلقه چت
print("Hello! I'm a chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)