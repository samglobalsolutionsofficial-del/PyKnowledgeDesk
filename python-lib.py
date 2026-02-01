
# required modules

import tkinter as tk
import json
import pyttsx3



class MyLibrary:
    def __init__(self):

        # load data as variable
        self.data = self.load_data()

        # create window
        self.window = tk.Tk()
        self.window.title("Python Library")
        self.window.geometry("574x550")

        # ICON (PNG)
        icon_path = 'E:\\PyCharm-Pro\\100-Days-Of-Code-Exercises/PythonLibrary/icon/library_ico.png'
        icon = tk.PhotoImage(file=icon_path)
        self.window.iconphoto(True, icon)


        # show welcome message
        welcome_message = "< / >  Welcome to Python Library  < / >"
        self.label = tk.Label(
            self.window,
            text=welcome_message,
            font=("Helvetica", 20, 'bold'),
            wraplength=650,
            fg='white',
            relief='ridge',
            bg='#0000FF',
            activebackground='#F0F0F0',
            activeforeground='#222222',
            bd=1.5,
            highlightbackground='#222222',
            highlightthickness=3,
            width=33,
            height=3,
        )
        self.label.grid(row=0, column=0, columnspan=3)

        # topic label
        self.topic_label = tk.Label(
            self.window,
            text="Enter the topic name:",
            font=("Helvetica", 15, 'bold'),
            fg='#2c3e50'
        )
        self.topic_label.grid(row=1, column=0, padx=10, pady=10)

        # entry box
        self.entry = tk.Entry(
            self.window,
            width=29,
            font=("Arial", 14),
            bd=1.5,
            relief='solid',
            highlightbackground='#222222',
            bg='#FFFFFF',
            highlightthickness=1,
            fg='#222222',
            insertbackground='#222222',
            selectbackground='#222222',
            selectforeground='#FFFFFF'
        )
        self.entry.grid(row=1, column=1, pady=30)

        # button frame
        button_frame = tk.Frame(self.window)
        button_frame.grid(row=2, column=1)

        # button to search topic
        self.search_button = tk.Button(
            button_frame,
            text="Search",
            font=("Arial", 12, 'bold'),
            width=12,
            height=1,
            bd=2,
            relief='raised',
            bg='#0000FF',
            fg='white',
            activebackground='#F0F0F0',
            activeforeground='#222222',
            command=self.search_topic
        )
        self.search_button.pack(side=tk.LEFT, padx=10, pady=10)

        # button to audio
        self.audio_button = tk.Button(
            button_frame,
            text="🔊 Play Audio",
            font=("Arial", 12, 'bold'),
            width=12,
            height=1,
            bd=2,
            relief='raised',
            bg='#0000FF',
            fg='white',
            activebackground='#F0F0F0',
            activeforeground='#222222',
            command=self.play_audio
        )
        self.audio_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # output text box
        self.output_result = tk.Text(
            self.window,
            relief='solid',
            height=12,
            width=45,
            font=('Arial', 14),
            bd=1,
            highlightbackground='#222222',
            bg='#FFFFFF',
            highlightthickness=0.5,
            fg='#222222',
            insertbackground='#222222',
            selectbackground='#222222',
            selectforeground='#FFFFFF'
        )
        self.output_result.grid(row=5, column=0, columnspan=3, pady=10)
        self.output_result.bind('<Key>', self.ignore_input)
        self.output_result.config(state='disabled')

    # load data
    def load_data(self):
        try:
            with open('data/data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    # search topic
    def search_topic(self):
        key = self.entry.get().lower().strip()
        self.output_result.config(state='normal')
        self.output_result.delete('1.0', tk.END)

        if key in self.data:
            self.output_result.insert(tk.END, self.data[key])
        else:
            self.output_result.insert(tk.END, f'Key "{key}" not found.')

        self.output_result.config(state='disabled')

    # play audio
    def play_audio(self):
        text = self.output_result.get('1.0', tk.END).strip()
        if text:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 170)
            engine.say(text)
            engine.runAndWait()
            engine.stop()

    # disable typing in text box
    def ignore_input(self, event):
        return 'break'

    # run app
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    library = MyLibrary()
    library.run()