import os
import requests

def download_file(url, save_path):
    response = requests.get(url)
    response.raise_for_status()  # Перевірка на успішність запиту
    with open(save_path, 'wb') as file:
        file.write(response.content)

# Створіть директорії для CSS, JS та зображення файлів
os.makedirs('static/intl-tel-input/css', exist_ok=True)
os.makedirs('static/intl-tel-input/js', exist_ok=True)
os.makedirs('static/intl-tel-input/img', exist_ok=True)

# URL-адреси файлів
css_url = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/css/intlTelInput.css'
js_url = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/js/intlTelInput.min.js'
utils_url = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/js/utils.js'
flags_url = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/img/flags@2x.png'

# Шляхи для збереження файлів
css_save_path = 'static/intl-tel-input/css/intlTelInput.css'
js_save_path = 'static/intl-tel-input/js/intlTelInput.min.js'
utils_save_path = 'static/intl-tel-input/js/utils.js'
flags_save_path = 'static/intl-tel-input/img/flags@2x.png'

# Завантаження файлів
download_file(css_url, css_save_path)
download_file(js_url, js_save_path)
download_file(utils_url, utils_save_path)
download_file(flags_url, flags_save_path)

print("Завантаження завершено.")
