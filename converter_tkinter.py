from tkinter import *
from le_converter import *

root = Tk()

root.geometry("500x600")
root.title("yare yare")

root.minsize(500,600)
root.maxsize(500,600)

root.config(bg="#b2ebf2")

def process():
    global result, text_from
    
    result = ""
    text_from = input_text.get("1.0", "end-1c")
    
    if clicked_get == "STRING" and clicked_set == "BINARY":
        result = str_to_bin(text_from)
    elif clicked_get == "STRING" and clicked_set == "HEXADECIMAL":
        result = str_to_hex(text_from)

    if clicked_get == "BINARY" and clicked_set == "STRING":
        result = bin_to_str(text_from)
    elif clicked_get == "BINARY" and clicked_set == "HEXADECIMAL":
        result =  bin_to_hex(text_from)
   
    if clicked_get == "HEXADECIMAL" and clicked_set == "STRING":
        result = hex_to_str(text_from)
    elif clicked_get == "HEXADECIMAL" and clicked_set == "BINARY":
        result = hex_to_bin(text_from)

    if clicked_get==clicked_set: result = text_from

    return result

def show():
    output_text.delete("1.0", "end-1c")
    
    global clicked_get,clicked_set
    clicked_get,clicked_set = clicked_from.get(), clicked_to.get()
    
    process()
    output_text.insert(END, result)

def swap():
    item1 = output_text.get("1.0","end-1c") 
    item2 = input_text.get("1.0","end-1c")
    clicked_get,clicked_set = clicked_from.get(), clicked_to.get()

    clear()
    
    clicked_from.set(clicked_set)
    clicked_to.set(clicked_get)
    input_text.insert(END, item1)
    output_text.insert(END, item2)
    
def clear():
    input_text.delete("1.0", "end-1c")
    output_text.delete("1.0", "end-1c")

options = ["STRING", "BINARY", "HEXADECIMAL"]

clicked_from = StringVar()
clicked_from.set(options[0])

clicked_to = StringVar()
clicked_to.set(options[0])

string_in = StringVar()

## LAYOUT

##  LABEL & DROPBOX    ##########################################################################

label_from = Label(root, text = "FROM: ", bg = "#b2ebf2", font=("", 12)).place(x=10,y=15)

drop = OptionMenu(root, clicked_from, *options)
drop.place(x=75,y=15, width = 120, height = 30)

label_to = Label(root, text = "TO: ", bg = "#b2ebf2", font=("", 12)).place(x=200,y=15)

drop2 = OptionMenu(root, clicked_to, *options)
drop2.place(x=240, y=15, width = 120, height = 30)

##  BUTTONS    ##########################################################################

btn_convert = Button(root,text="CONVERT",bg = "#9ccc65", activebackground = "#4caf50", command = show)
btn_convert.place(x=380,y=15, width = 100, height = 40)

btn_clear = Button(root, text="CLEAR",bg="red", activebackground = "#ff4500", command = clear)
btn_clear.place(x=380, y=60, width = 100, height = 40)

btn_swap = Button(root, text="SWAP", bg="#ffa000", activebackground = "#ff6f00", command=swap)
btn_swap.place(x=380,y=105, width =100, height = 40)

##  TEXTBOX    ##########################################################################

label_input = Label(root, text="INPUT TEXT: ", bg="#b2ebf2")
label_input.place(x=12, y=150)

input_text = Text(root, width = 52, height = 10, bg = "light yellow", font=("",12))
input_text.place(x=14, y=180)

label_output = Label(root, text="OUTPUT: ", bg="#b2ebf2")
label_output.place(x=12, y=380)

output_text = Text(root, width = 52, height = 10, bg = "#85c1e9", font=("",12))
output_text.place(x=14,y=400)

##  MAINLOOP    ##########################################################################

root.mainloop()
