

from gigachat import GigaChat
import ssl

# Создаем кастомный SSL контекст без проверки сертификатов
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE



giga = GigaChat(
    credentials='MWIwYjY4ZjctYmQ1Ny00MDcyLWEzNWMtYzYwNWY4NTNjNjg5OmI4OTM4MGMxLWJkODktNGE2My05YWZlLTE5ZWQzZGMzY2JjZA==',
    verify_ssl_certs=False,  # Отключаем проверку SSL
    ssl_context=ssl_context  # Передаем кастомный SSL контекст
)


response = giga.get_models()
print(response)

a = 4
b = 5


# Используем f-string для вставки значений переменных
response = giga.chat(f"коротко скажи сколько будет {a} + {b}")
print(response.choices[0].message.content)

result = giga.tokens_count(input_=["12345"], model="GigaChat-Pro")
print(result)

