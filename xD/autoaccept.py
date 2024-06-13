import pyautogui
import time
import winsound
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk  # Importujemy potrzebne moduły PIL

last_message = ""

def click_accept_button():
    global last_message
    
    while True:
        try:
            accept_button_location = pyautogui.locateOnScreen('accept.png', confidence=0.9)
            if accept_button_location is not None:
                current_message = "Znaleziono Mecz!"
                if current_message != last_message:
                    message_label.config(text=current_message)
                    last_message = current_message
                
                # Sygnał dźwiękowy
                winsound.Beep(440, 75)
                winsound.Beep(700, 100)
                
                accept_button_center = pyautogui.center(accept_button_location)
                pyautogui.click(accept_button_center)

                current_message = "Powodzenia GLHF:) "
                if current_message != last_message:
                    message_label.config(text=current_message)
                    last_message = current_message
                
                time.sleep(5)
                
            else:
                current_message = "Szukanie meczu..."
                if current_message != last_message:
                    message_label.config(text=current_message)
                    last_message = current_message
                
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            current_message = "Szukanie nastepnego meczu"
            if current_message != last_message:
                message_label.config(text=current_message)
                last_message = current_message
            
            time.sleep(1)

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Bot do akceptacji meczu")
root.geometry("508x401")  # Ustawienie rozmiaru okna

# Dodajemy obraz tła
background_image = Image.open("background_image.png")  # Wczytujemy obraz
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Tworzymy etykietę do wyświetlania wiadomości
message_label = tk.Label(root, text="Kliknij 'Start' aby rozpocząć", font=("Arial", 12))
message_label.pack(pady=20)

# Uruchamiamy funkcję w osobnym wątku, aby nie blokować interfejsu
thread = Thread(target=click_accept_button)
thread.start()

# Obsługa zamykania okna
def on_closing():
    root.destroy()
    try:
        thread.join()  # Upewniamy się, że wątek zostanie zamknięty przed zamknięciem aplikacji
    except NameError:
        pass

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
