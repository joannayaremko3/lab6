import requests
import pandas as pd

# Функція для отримання списку доступних продуктів
def get_available_products():
    url = 'https://api.pro.coinbase.com/products'
    response = requests.get(url)
    if response.status_code == 200:
        products_data = response.json()
        return products_data
    else:
        print("Failed to retrieve products. Status code:", response.status_code)
        return None

# Отримання списку доступних продуктів
products_data = get_available_products()

# Перевірка результату
if products_data:
    # Створення DataFrame з отриманих даних
    products_df = pd.DataFrame(products_data)
    print("Список доступних продуктів:")
    print(products_df[['id', 'display_name']])
else:
    print("Не вдалося отримати список продуктів.")