import tkinter as tk
from pandastable import Table
import pandas as pd



df1 = pd.read_csv("")
df2 = pd.read_csv("")
df3 = pd.read_csv("")
df = pd.concat([df1, df2, df3])
root = tk.Tk()
root.title('Novo excel')

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

pt = Table(frame, dataframe=df)
pt.show()


root.mainloop()
