import tkinter as tk

def get_response(user_input):
    user_input = user_input.lower()
    if user_input in ['hi', 'hello', 'hey']:
        return "Hello! How can I help you today?"
    elif 'your name' in user_input:
        return "My name is ChatBot."
    elif 'how are you' in user_input:
        return "I'm just a program, but I'm doing well!"
    elif 'help' in user_input:
        return "Sure, I can help. Please tell me your question."
    elif user_input == 'bye':
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."

def send_message(event=None):
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_log.insert(tk.END, "ChatBot: " + response + "\n")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    if user_input.lower() == 'bye':
        root.after(1000, root.destroy)

root = tk.Tk()
root.title("ChatBot")

chat_log = tk.Text(root, state=tk.DISABLED, width=60, height=20, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "ChatBot: Hello! I'm ChatBot. Type 'bye' to exit.\n")
chat_log.config(state=tk.DISABLED)

entry.focus()
root.mainloop()
