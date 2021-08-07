import tkinter as tk
import random


class Application(tk.Frame):
    def __init__(self, master=None):
      super().__init__(master)
      self.words = []
      self.hanger = ['''
                _____
                |   |
                    |
                    |
                    |
                   _|_''', '''
                _____
                |   |
                O   |
                    |
                    |
                   _|_''', '''
                _____
                |   |
                O   |
                |   |
                |   |
                   _|_''', '''
                _____
                |   |
                O   |
               /|   |
                |   |
                   _|_''', '''
                _____
                |   |
                O   |
               /|\  |
                |   |
                   _|_''', ''' 
                _____
                |   |
                O   |
               /|\  |
                |   |
               /   _|_''', '''
                _____
                |   |
                O   |
               /|\  |
                |   |
               / \ _|_''', '''
     ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
     ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

               \O/      
      WINNER    |    WINNER        
                |    
               / \ 

     ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
     ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
      self.master = master
      self.pack()
      self.create_widgets()
      self.load_words()
      self.play()

    def load_words(self):
       with open('words.txt', 'r') as f:
          for line in f:
              self.words.append(line)

    def create_widgets(self):
      self.entry = tk.Entry(root)
      self.entry.pack()

      self.display = tk.Text(root, height=15, width=50)
      self.display.pack(side="right")

      self.display_2 = tk.Text(root, height=15, width=34)
      self.display_2.pack(side="left")

      self.submit = tk.Button(self, text="Submit", fg="red")
      self.submit["command"] = self.check
      self.submit.pack(side="left")

      self.new = tk.Button(self, text="New", fg="green")
      self.new["command"] = self.play
      self.new.pack(side="left")
      
    def play(self):
      self.found = False
      self.verify = []
      self.used = set()
      self.mistakes = 0
      self.word = (self.words[random.randint(0, len(self.words) - 1)]).strip()
      self.letters = [letter for letter in self.word]
      
      for i in range(len(self.letters)):
        self.verify.append(" _ ")
        self.lines = "".join(self.verify)

      self.update_display()
      self.update_display_images()

    def check(self):
      if self.entry.get() and len(self.entry.get()) == 1:
          self.input = self.entry.get()
          if self.input in self.word:
              for i in range(len(self.letters)):
                if self.letters[i] == self.input:
                    self.verify[i] = self.input
              self.update_display("\n\nYou found a letter!")
          elif self.input not in self.letters:
              if self.input not in self.used:
                self.mistakes += 1
                self.update_display("\n\nYou made a mistake!")

          if self.input in self.used:
              self.update_display("\n\nYou already entered this letter!")
          
          self.used.add(self.input)
          self.update_display_images(self.mistakes)

      if self.letters == self.verify:
        self.update_display("\n\nYou guessed the word! You win! ")
        self.update_display_images(7)

      if self.mistakes == 6:
          self.end_game()

      elif len(self.entry.get()) != 1 :
        self.update_display("\n\nPlease enter only a letter!")

    def update_display(self, message=""):
      self.display.config(state=tk.NORMAL)
      self.display.delete('1.0', tk.END)
      self.display.insert(tk.END, " ".join(self.verify))
      self.display.insert(tk.END, message + f" \n\nMistakes: {self.mistakes} (Max 6)")
      self.display.config(state=tk.DISABLED)
        
    def update_display_images(self, number=0):
      self.display_2.config(state=tk.NORMAL)
      self.display_2.delete('1.0', tk.END)
      self.display_2.insert(tk.END, "".join(self.hanger[number]))
      self.display_2.config(state=tk.DISABLED)

    def end_game(self):
      self.submit["state"] = tk.DISABLED
      self.update_display(f"\n\nGame Over! You lose! The word was '{self.word}'!")
    
root = tk.Tk()
root.title('Hangman by Calvin Liew')
app = Application(master=root)
app.mainloop()