import tkinter as tk
import requests
import json
def get_repository_info():
    repo_name = repo_name_entry.get()
    url = f'https://api.github.com/repos/{repo_name}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        info = {
            'company': data.get('owner', {}).get('company'),
            'created_at': data.get('created_at'),
            'email': data.get('owner', {}).get('email'),
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('owner', {}).get('url')
        }
        with open('repository_info.json', 'w') as file:
            json.dump(info, file, indent=4)
        result_label.config(text="Информация успешно сохранена.", fg="black")
    elif response.status_code == 404:
        result_label.config(text="Репозиторий не найден.", fg="red")
    else:
        result_label.config(text="Произошла ошибка при получении информации.", fg="red")


window = tk.Tk()
window.title("GitHub Repository Info")

repo_name_label = tk.Label(window, text="Имя репозитория (например, 'kubernetes/kubernetes'): ")
repo_name_label.pack()

repo_name_entry = tk.Entry(window)
repo_name_entry.pack()

get_info_button = tk.Button(window, text="Получить информацию", command=get_repository_info)
get_info_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
