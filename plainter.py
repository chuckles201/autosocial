import tkinter as tk

# store variables
func_vars = [None,None,None,None,None,None]
def guiApp():
    # function for when clicked (end and collect info)
    def submitClick():
        # get info,close
        url = input_url.get().strip()
        extra_instruct = extra_instr.get("1.0",tk.END).strip()
        
        x_var = x_response.get()
        hn_var = hn_response.get()
        disc_var = disc_response.get()
        reddit_var = reddit_response.get()
        
        root.destroy()
        
        global func_vars
        func_vars = [url,extra_instruct,x_var,hn_var,disc_var,reddit_var]
        
    
    # main-window
    root = tk.Tk()
    root.title("TestApplicationFun!")
    
    # two columns
    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=3)
    
    # header for application
    header = tk.Frame(root,height=50)
    header.grid(row=0,column=0,sticky='ew',columnspan=2)
    title = tk.Label(header,text="AutoSocial",font=('Jokerman',25))
    title.pack(pady=15)
    
    # setting frames
    left_frame = tk.Frame(root,bg="lightgreen",width=300,height=400)
    right_frame = tk.Frame(root,bg="lightblue",width=300,height=400)
    # fixed frames
    left_frame.grid(row=1,column=0,sticky='nsew')
    right_frame.grid(row=1,column=1,sticky='nsew')
    left_frame.propagate(False)
    right_frame.propagate(False)
    
    # textbox/entry
    input_title = tk.Label(left_frame,text="URL to article",font=('Arial',15),pady=5,bg="lightgreen")
    input_title.pack()
    input_url = tk.Entry(left_frame,font=('Arial',12),bg="white")
    input_url.pack()
    
    # instructions
    instr_title = tk.Label(left_frame,text="Extra Instructions For LLM",font=('Arial',15),pady=5,bg="lightgreen")
    instr_title.pack()
    extra_instr = tk.Text(left_frame,font=('Arial',12),height=7,bg="white")
    extra_instr.pack()
    
    # adding in yes/no
    x_response = tk.BooleanVar()
    hn_response = tk.BooleanVar()
    reddit_response = tk.BooleanVar()
    disc_response = tk.BooleanVar()
    
    checks_title = tk.Label(right_frame,text="Post to:",font=('Arial',15),bg="lightblue",pady=10)
    x_checkbox = tk.Checkbutton(right_frame,text="X?",variable=x_response,bg="lightblue")
    hn_checkbox = tk.Checkbutton(right_frame,text="HackerNews?",variable=hn_response,font=('Arial',12),bg="lightblue")
    reddit_checkbox = tk.Checkbutton(right_frame,text="Reddit?",variable=reddit_response,font=('Arial',12),bg="lightblue")
    disc_checkbox = tk.Checkbutton(right_frame,text="Discord?",variable=disc_response,font=('Arial',12),bg="lightblue")
    
    
    checks_title.pack()
    x_checkbox.pack()
    hn_checkbox.pack()
    reddit_checkbox.pack()
    disc_checkbox.pack()
    
    # button to stop
    submit_button = tk.Button(root,text='Submit',font=('Arial',12),command=submitClick)
    submit_button.grid(row=2,column=0,columnspan=2)
    

    # main window
    root.mainloop()
    
    global func_vars
    
    return func_vars 
    
    
# ORDER: URL,INSTRUCTIONS,X,HN,DISC,REDDIT
# # url,
# print(guiApp())