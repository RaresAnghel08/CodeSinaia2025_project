import tkinter as tk
from probability import get_response
from responses import unknown

def start_main_app():
    root = tk.Tk()
    root.title("Chatbot")
    
    #TODO
    # #upper left image logo
    # root.iconbitmap('logo.ico')  # Ensure you have a logo.ico file in the same directory
    
    window_width = 500
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    splash_x = (screen_width // 2) - (window_width // 2)
    splash_y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{splash_x}+{splash_y}")

    chat_log = tk.Text(root, state=tk.DISABLED, wrap="word")
    chat_log.pack(padx=10, pady=10, expand=True, fill='both')

    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=5)

    entry = tk.Entry(entry_frame, width=50)
    entry.pack(side=tk.LEFT, padx=(0, 10))

    # TODO:fa un buton in figma pt a trimite textul / & sterge chatul la care sa ii pui bacground imaginea si action
    # button_image_input = PhotoImage(file=relative_to_assets("button_input.png"))
    # Button_input = Button(
    #     image=button_image_input,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=select_input_folder,
    #     relief="flat",
    #     activebackground="#D9D9D9",
    #     background="#D9D9D9"
    # )
    send_button = tk.Button(entry_frame, text="Trimite", command=lambda: send_message(entry, chat_log))
    send_button.pack(side=tk.LEFT)
    
    # TODO: optional - sa puna si place la buton
    # Button_input.place(
    #     x=22.0,
    #     y=84.0,
    #     width=755.0,
    #     height=56.0
    # )

    clear_button = tk.Button(entry_frame, text="Clear Chat", command=lambda: clear_chat(chat_log))
    clear_button.pack(side=tk.LEFT, padx=(10, 0))

    root.bind('<Return>', lambda event=None: send_message(entry, chat_log))

    root.mainloop()

def send_message(entry, chat_log):
    
    #TODO: check and alert in a separate windows if empty message
    if not entry.get():
        # de customizat
        '''
        de centrat
        de scos butonul de ok
        de pus un mesaj de genul "Please enter a message."
        ceva cu semnul ala rosu de eroare
        de pus un icon de eroare
        de pus un background la fereastra de alert
        de pus un titlu la fereastra de alert
        '''
        #TODO: de revizuit
        alert = tk.Toplevel()
        alert.title("Alert")
        alert.geometry("300x100")
        alert.configure(bg="#ff0015")
        # alert.iconbitmap('error.ico')  # Ensure you have an error.ico file in the same directory
        alert_label = tk.Label(alert, text="Please enter a message.", bg="#f8d7da", fg="#ff0019", font=("Helvetica", 12))
        alert_label.pack(expand=True)
        ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#ff0019")
        ok_button.pack(pady=10)
        return
    
    user_message = entry.get()
    if user_message.strip() == "":
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_message}\n")

    bot_response = get_response(user_message)
    chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")

    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
def clear_chat(chat_log):
    chat_log.config(state=tk.NORMAL)
    chat_log.delete('1.0', tk.END)
    chat_log.config(state=tk.DISABLED)

def show_splash_then_main():
    splash = tk.Tk()
    splash.overrideredirect(True)
    
    #TODO
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    
    splash_width = 400
    splash_height = 200
    
    #TODO 
    splash_x = (screen_width // 2) - (splash_width // 2)
    splash_y = (screen_height // 2) - (splash_height // 2)
    splash.geometry(f"400x200+{splash_x}+{splash_y}")
    
    splash.configure(bg="#333333")

    label = tk.Label(splash, text="Welcome to Chatbot!", font=("Helvetica", 24), fg="white", bg="#333333")
    label.pack(expand=True)

    def close_splash():
        splash.destroy()
        start_main_app()
        
    splash.after(3000, close_splash)
    splash.mainloop()

if __name__ == "__main__":
    show_splash_then_main()
