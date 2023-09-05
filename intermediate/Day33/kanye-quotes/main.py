from tkinter import *
import requests
import json

URl = 'https://api.kanye.rest/'
proxy = {
    'http' : 'http://192.168.98.126:8080',
    'https' : 'http://192.168.98.126:8080'
}

def get_quote():
    print('connecting ...')
    response = requests.get(
        url=URl,
        proxies=proxy
    )
    print('Im back')
    data = response.text
    try:
        data_json = json.loads(data)
        print(data_json)
        canvas.itemconfigure(quote_text, text=data_json['quote'])
    except json.JSONDecodeError:
        print("Empty response")
    print('checked out')


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()