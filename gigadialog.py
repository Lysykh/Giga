from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole


payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="Ты внимательный бот-програмист, который помогает пользователю решить его проблемы. Отвечаешь максимально коротко. Максимум 3 предложения"
        ),
    ],
    temperature=0.7,
    max_tokens=100,
)

with GigaChat(credentials='MWIwYjY4ZjctYmQ1Ny00MDcyLWEzNWMtYzYwNWY4NTNjNjg5OjQ3N2ZjZjVjLTdlZTctNGYwOC04ODM0LTMyNTM5Y2E1NGEwMA==', verify_ssl_certs=False) as giga:
    while True:
        user_input = input("User: ")
        payload.messages.append(Messages(role=MessagesRole.USER, content=user_input))
        response = giga.chat(payload)
        payload.messages.append(response.choices[0].message)
        print("Bot: ", response.choices[0].message.content)


