import tkinter

window = tkinter.Tk()
window.title('KG to Pound Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

kg_input = tkinter.Entry(width=10)
kg_input.grid(column=1, row=0)

kg_label = tkinter.Label(text="kg")
kg_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equals to")
equal_label.grid(column=0, row=1)

output_label = tkinter.Label()
output_label.grid(column=1, row=1)

lbs_label = tkinter.Label()
lbs_label['text'] = 'lbs'
lbs_label.grid(column=2, row=1)


def button_clicked():
    kgs = float(kg_input.get())
    lbs = kgs * 2.20462
    output_label.config(text=str(lbs))


my_button = tkinter.Button(text='Convert', command=button_clicked)
my_button.grid(column=1, row=2)

window.mainloop()
