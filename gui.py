
import tkinter as tk
from turtle import bgcolor, color
from pyparsing import col
import sympy
sympy.init_printing()
from functions import *
from tkinter import NW, SOLID, ttk
from matplotlib import mathtext
from io import BytesIO
from PIL import ImageTk, Image
  
 
LARGEFONT =("Verdana", 35)
class Menubar(ttk.Frame):
    """Builds a menu bar for the top of the main window"""
    def __init__(self, parent, *args, **kwargs):
        ''' Constructor'''
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_menubar()

    def on_exit(self):
        '''Exits program'''
        quit()

    def display_help(self):
        '''Displays help document'''
        pass

    def display_about(self):
        '''Displays info about program'''
        pass

    def init_menubar(self):
        self.menubar = tk.Menu(self.root)
        self.menu_file = tk.Menu(self.menubar) # Creates a "File" menu
        self.menu_file.add_command(label='Exit', command=self.on_exit) # Adds an option to the menu
        self.menubar.add_cascade(menu=self.menu_file, label='File') # Adds File menu to the bar. Can also be used to create submenus.

        self.menu_help = tk.Menu(self.menubar) #Creates a "Help" menu
        self.menu_help.add_command(label='Help', command=self.display_help)
        self.menu_help.add_command(label='About', command=self.display_about)
        self.menubar.add_cascade(menu=self.menu_help, label='Help')

        self.root.config(menu=self.menubar)  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self, width=800, height=600) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, KM, Sardinas, HuffmanTree, AdaptiveHuffman,Golomb,  Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text ="Compression", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        # label.grid(row = 0, column = 1, padx = 10, pady = 10,columnspan=5)
  
        button1 = ttk.Button(self, text ="Kraft-McMillan Inequality",
        command = lambda : controller.show_frame(KM))
     
        # putting the button in its place by
        # using grid
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10,columnspan=5)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Sardinas",
        command = lambda : controller.show_frame(Sardinas))
     
        # putting the button in its place by
        # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10,columnspan=5)

         ## button to show frame 2 with text layout2
        button3 = ttk.Button(self, text ="Huffman Tree",
        command = lambda : controller.show_frame(HuffmanTree))
      ## button to show frame 2 with text layout2
        button4 = ttk.Button(self, text ="Adaptive Huffman Tree",
        command = lambda : controller.show_frame(AdaptiveHuffman))

        button5 = ttk.Button(self, text ="Golomb Encoding",
        command = lambda : controller.show_frame(Golomb))
     
        # putting the button in its place by
        # using grid
        # button3.grid(row = 3, column = 1, padx = 10, pady = 10,columnspan=5)
        label.pack(padx = 10, pady = 10)
        button1.pack(padx = 10, pady = 10)
        button2.pack(padx = 10,pady = 10)
        button3.pack(padx = 10,pady = 10)
        button4.pack(padx = 10,pady = 10)
        button5.pack(padx = 10,pady = 10)
        
class KM(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Enter space separated codewords: ")
        label.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0,column=3)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Check inequality",
                            command = lambda : self.compute(self.entry.get()))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 0, column = 4, padx = 10, pady = 10)


        clearbutton = ttk.Button(self, text ='Clear', command=self.clear)
        clearbutton.grid(row = 1, column = 4)

        self.label_success = ttk.Label(self, text='')
        self.img_label = ttk.Label(self,image='')

    def compute(self,data):
        if data != '':
            c = data.split()
            sum = km(c)
            buffer = BytesIO()

            #Writing png image with our rendered greek alpha to buffer
            mathtext.math_to_image('$\sum_{i = 1}^{k} {2^{-L_{i}}} = ' + str(sum) +'$', buffer, dpi=100, format='png')

            #Remoting bufeer to 0, so that we can read from it
            buffer.seek(0)

            # Creating Pillow image object from it
            pimage= Image.open(buffer)

            #Making background transparent
            img = pimage.convert("RGBA")
            datas = img.getdata()

            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)

            img.putdata(newData)
            #Creating PhotoImage object from Pillow image object
            image = ImageTk.PhotoImage(img)

            #Creating label with our image
            # mylabel = tk.Label(self,image=image)
            self.img_label.config(image='')
            self.img_label.grid(row = 1, column =3)


            #Storing reference to our image object so it's not garbage collected,
            # as TkInter doesn't store references by itself
            self.img_label.config(image=image)
            self.img_label.img = image
            self.img_label.grid(row = 1, column =3)


            self.label_success.config( text='')
            self.label_success.grid(row = 2, column =3)

            self.success() if sum <=1 else self.fail()  

    def success(self):
        message = "Inequality holds"
        self.label_success.config( text=message, foreground='green')
        self.label_success.grid(row = 2, column =3)
        
    def fail(self):
        message = "Inequality fails"
        self.label_success = ttk.Label(self, text=message, foreground= 'red')
        self.label_success.grid(row = 2, column =3)
    def clear(self):
        self.entry.delete(0,'end')
        self.label_success.config(text = '')
        self.img_label.config(image='')
        self.img_label.img = ''

# second window frame page1
class Sardinas(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Enter space separated codewords: ")
        label.grid(row = 1, column = 1, padx = 10, pady = 10)

        ttk.Label(self,text='Sardinas-Patterson check for decodeability').grid(row=0, column=2, padx=10)
        self.entry = ttk.Entry(self, width=40)
        self.entry.grid(row=1,column=2)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        button2 = ttk.Button(self, text ="Check decodeability",
                            command = lambda : self.compute(self.entry.get()))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 3, padx = 10, pady = 10)

        button3 = ttk.Button(self,text='Clear', command = self.clear)
        button3.grid(row = 2, column=3)
        self.setVar = tk.StringVar(value ='Prefix/Suffix Sets')
        self.outVar = tk.StringVar(value ='Output')
        self.setLabel = tk.Message(self, textvariable=self.setVar, anchor=NW, fg='grey', width =120, background='white', borderwidth=0.5, relief=SOLID)
        self.setLabel.grid(row=2, column=1,padx=20,pady =10)
        self.outLabel = tk.Message(self, textvariable=self.outVar, anchor=NW, fg='grey', width =200, background='white', borderwidth=0.5, relief=SOLID)
        self.outLabel.grid(row=2, column=2,padx=20,pady =10, sticky="N")
    
    def compute(self,data):
        if data != '':
            c = None

            self.setVar.set('')
            self.outVar.set('')
            c = set(data.split())
            message,sets = sardinas(c)
            self.setVar.set(sets)
            self.outVar.set(message)
    def clear(self):
        self.entry.delete(0,'end')
        self.setVar.set('Prefix/Suffix Sets')
        self.outVar.set('Output')


class HuffmanTree(tk.Frame):
     
    def __init__(self, parent, controller):
        self.count = 3
        tk.Frame.__init__(self, parent)
        
        self.ran = False
        self.controlFrame = tk.Frame(self,parent)
        self.controlFrame.grid(row=0, column=2, padx=10)
        self.choice = tk.IntVar()
        ttk.Label(self.controlFrame,text='Construct Huffman Tree from', font='helvetica 12 bold').grid(row=0, column=0,columnspan=2)

       
        self.symEntries=[]
        self.probEntries=[]

        self.entriesFrame= tk.Frame(self,parent)
        
        self.sequenceFrame = tk.Frame(self,parent)
        
        self.seq = tk.Entry(self.sequenceFrame)
        self.seq.grid(row=2,column=1,padx = 10, pady = 10)
        ttk.Radiobutton(self.controlFrame,text='Sym : Prob pairs', value = 0, variable=self.choice, command= lambda: self.changeFrame(self.choice.get()) ).grid(row=1, column=0)
        ttk.Radiobutton(self.controlFrame,text='Sequence', value = 1, variable=self.choice, command=lambda: self.changeFrame(self.choice.get()) ).grid(row=1, column=1)
        
        label = ttk.Label(self.entriesFrame, text ="Sym : Prob")
        label.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        ttk.Label(self.sequenceFrame, text ='Enter Sequence').grid(row = 1, column = 1, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda: self.home(controller))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 0, column = 1, padx = 10)
  
        button2 = ttk.Button(self.controlFrame, text ="Construct Tree",
                            command = self.compute)

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 0, padx = 10, pady = 10, columnspan=2)
        button3 = ttk.Button(self,text='Clear', command = self.clear)
        button3.grid(row = 0, column=3, padx = 10, pady = 10)
        
        self.newBtn = ttk.Button(self.entriesFrame,text='+', command = self.add, width=5)
        self.newBtn.grid(row=self.count+1, column=2)
        # self.canvas = tk.Canvas(self, 
        # width = self.width, height = self.height,bg="white")
        # self.canvas.grid(row=2,column=2)
        self.add()
        self.frames = {}
        self.frames[0] = self.entriesFrame
        self.frames[1] = self.sequenceFrame
        self.frame = self.frames[self.choice.get()]
        self.outVar = tk.StringVar(value='Output')
        self.changeFrame(self.choice.get())
        
        
    def changeFrame(self, frame_num):
        self.clear()
        new_frame = self.frames[frame_num]
        if self.frame is not None:
            self.frame.grid_forget()
        self.frame = new_frame
        self.frame.grid(row =1, column =1,padx = 10, pady = 10)
        
    
    
    def home(self,controller):
        self.clear()
        controller.show_frame(StartPage)
    def add(self):
        
        self.symEntries.append(tk.Entry(self.entriesFrame, width=5, borderwidth=0.5, relief=SOLID)) # Create and append to list
        self.symEntries[-1].grid(row=self.count,column=1,padx=2, pady=5) # Place the just created widget
        self.probEntries.append(tk.Entry(self.entriesFrame, width=5, borderwidth=0.5, relief=SOLID)) # Create and append to list
        self.probEntries[-1].grid(row=self.count,column=2,padx=2, pady=5) # Place the just created widget
        self.newBtn.grid(row=self.count+1, column=2)
        self.count += 1 # Increase the count by 1
    def symbols_from_sequence(self, sequence):
        syms = dict.fromkeys([char for char in sequence],0)
        for char in sequence:
            syms[char] += round(1/len(sequence),3)
        return [(k,v) for k,v in syms.items()]
        
    def compute(self):
        
        if self.seq.get() != '' or ( self.symEntries[0].get() != '' and self.probEntries[0].get() != ''):
            if self.choice.get() == 0: symbols = [(self.symEntries[i].get(),float(self.probEntries[i].get())) for i in range(len(self.symEntries))]
            else: symbols = self.symbols_from_sequence(self.seq.get())
            
            # symbols = [('a', 0.4), ('b', 0.2), ('c',0.1), ('d', 0.1), ('e', 0.09), ('f',0.09), ('g', 0.01), ('h', 0.01)]
            self.ran = True
            # symbols = [('a', 0.4), ('b', 0.2), ('c',0.1), ('d', 0.1), ('e', 0.09), ('f',0.09), ('g', 0.01), ('h', 0.01)]    
            root = ConstructHuffmanTree(symbols)
            depth = maxDepth(root)
            self.codebook = makeCodes(root)
            self.root = root
            self.width = getMaxWidth(root)*200
            self.height = depth*100
            self.canvas = tk.Canvas(self, 
            width = self.width, height = self.height,bg='#F0f0f0')
            self.canvas.grid(row=1,column=2)
            self.outLabel = tk.Message(self, textvariable=self.outVar, anchor=NW, fg='black', width =self.width,background='white', borderwidth=0.5, relief=SOLID)
            self.outLabel.grid(row=3, column=2,padx=20,pady =10, sticky="N")
            
            display(self,adaptive=False)
            H = round(-sum(symbols[i][1] * math.log(symbols[i][1],2) for i in range(len(symbols))),4)
            Lav = round(sum(symbols[i][1]*len(self.codebook.get(symbols[i][0])) for i in range(len(symbols))),4)
            Var = round(sum(symbols[i][1]* (len(self.codebook.get(symbols[i][0]))-Lav)**2 for i in range(len(symbols))),4)
            R = round(abs(H-Lav),4)

            message = ''
            message += 'Codebook: ' + str(self.codebook) + '\n'
            message += 'Entropy: ' + str(H) + '\n'
            message += 'Average Length ' + str(Lav) + '\n'
            message += 'Variance: ' +str(Var) + '\n'
            message += 'Redundancy: ' +str(R) + '\n'
            self.outVar.set(message)
            


    def clear(self):

        for sym,prob in zip(self.symEntries, self.probEntries):
            sym.grid_forget()
            prob.grid_forget()
        if self.ran:  
            self.canvas.delete('all')
            self.canvas.grid_forget()
            self.outLabel.grid_forget()
        self.outVar.set('Output')
        self.codebook = None
        self.symEntries.clear()
        self.probEntries.clear()
        self.seq.delete(0,'end')
        self.add()


# second window frame page1
class AdaptiveHuffman(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text ="Home",
                            command = lambda: self.home(controller))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 0, column = 0, padx = 10,pady = 10)
        self.ran = False
        self.entryFrame = tk.Frame(self, parent) 
        self.entryTxt = tk.StringVar(self,value ='Enter a Sequence')
        self.entry = tk.Entry(self.entryFrame, textvariable = self.entryTxt, fg = 'grey')
        self.entry.grid(row = 0, column = 0, padx = 10)
        self.entry.bind('<FocusIn>', self.clear_entry )
        self.goBtn = ttk.Button(self.entryFrame, text='Go', command = self.compute)
        self.goBtn.grid(row = 0, column = 1, padx = 10)
        self.entryFrame.grid(row = 0,column=1, padx = 10,pady = 10)
        self.infoMessage = tk.StringVar(self,value='Info')
        self.outLabel = tk.Message(self, textvariable=self.infoMessage, anchor=NW, fg='black', width =400,background='white', borderwidth=0.5, relief=SOLID)
        self.outLabel.grid(row=2, column=1,padx=20,pady =10, sticky="N")
        self.clearBtn = ttk.Button(self,text='Clear',command=self.clear)
        self.clearBtn.grid(row=2, column=2,padx=20,pady=10)
            
        # button to show frame 2 with text
        # layout2
        
        # button to show frame 2 with text
    def clear_entry(self,event):
        if self.entryTxt.get() == 'Enter a Sequence':
            self.entryTxt.set('')
            self.entry.config(fg='black')
    def clear(self):
        self.entryTxt.set('Enter a Sequence')
        self.entry.config(fg='grey')
        
        if self.ran: self.canvas.delete('all')
        self.infoMessage.set('Info')


    def compute(self):
        self.ran = True
        sequence = self.entry.get()
        self.seen = set() #conveniently holds all seen symbols
        self.encoded_sequence = '' #memory for our encoded sequence
        
        self.tree = [] #list of nodes to search easier
        original_message = '' 
        for letter in sequence:
            original_message += format(asciiDict[letter], "08b") #encoding message using ASCII dictionary
        
        
        self.root = adaptiveHuffman(self,sequence)
        self.depth = maxDepth(self.root)-1
        self.width = self.depth*110
        self.height =( self.depth-1)*80
        self.canvas = tk.Canvas(self, 
            width = self.width, height = self.height,bg='#F0f0f0')
        self.canvas.grid(row=1, column=1, padx = 10)
        self.angleFactor = math.pi/3
        self.sizeFactor = 1
        adisplay(self)
        # print('\n\nASCII encoded message: ' + str(original_message) + " - Length: " + str(len(original_message)))
        # print('Adaptive Huffman message: ' + str(encoded_sequence) + " - Length: " + str(len(encoded_sequence)))
        # print('Compression Ratio = ' + str(len(original_message)/len(encoded_sequence)))


    
    def home(self,controller):
        self.entryTxt.set('Enter a Sequence')
        self.entry.config(fg='grey')
        self.clear()
        controller.show_frame(StartPage)
  
  


class Golomb(tk.Frame):
     
    def __init__(self, parent, controller):
        self.count = 3
        tk.Frame.__init__(self, parent)
        
        self.ran = False
        self.controlFrame = tk.Frame(self,parent)
        self.controlFrame.grid(row=0, column=2, padx=10)
        self.choice = tk.IntVar()
        ttk.Label(self.controlFrame,text='Golomb encoding from', font='helvetica 12 bold').grid(row=0, column=0,columnspan=2)

       
        self.symEntries=[]
        self.probEntries=[]

        self.entriesFrame= tk.Frame(self,parent)
        
        self.sequenceFrame = tk.Frame(self,parent)
        
        self.seq = tk.Entry(self.sequenceFrame)
        self.seq.grid(row=2,column=1,padx = 10, pady = 10)
        ttk.Radiobutton(self.controlFrame,text='Sym : Prob pairs', value = 0, variable=self.choice, command= lambda: self.changeFrame(self.choice.get()) ).grid(row=1, column=0)
        ttk.Radiobutton(self.controlFrame,text='Sequence', value = 1, variable=self.choice, command=lambda: self.changeFrame(self.choice.get()) ).grid(row=1, column=1)
        self.caseSensitive = tk.IntVar()
        tk.Checkbutton(self.controlFrame,text='Case Sensitive (Note: This may hurt compression ratio)', variable= self.caseSensitive).grid(row=2, column=0, columnspan=2)
        label = ttk.Label(self.entriesFrame, text ="Sym : Prob")
        label.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        ttk.Label(self.sequenceFrame, text ='Enter Sequence').grid(row = 1, column = 1, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda: self.home(controller))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 0, column = 1, padx = 10)
  
        button2 = ttk.Button(self, text ="Go",
                            command = self.compute)

        # putting the button in its place by
        # using grid
        
        self.mVar = tk.StringVar(value='m Value')
        self.mEntry = tk.Entry(self,textvariable=self.mVar, fg= 'grey', width=20)
        self.mEntry.grid(row = 0, column = 3, padx = 10)
        self.mEntry.bind('<FocusIn>', self.clear_entry )
        
        button2.grid(row = 0, column = 4, padx = 10, pady = 10)
        button3 = ttk.Button(self,text='Clear', command = self.clear)
        button3.grid(row = 0, column=5, padx = 10, pady = 10)
        
        self.newBtn = ttk.Button(self.entriesFrame,text='+', command = self.add, width=5)
        self.newBtn.grid(row=self.count+1, column=2)
        # self.canvas = tk.Canvas(self, 
        # width = self.width, height = self.height,bg="white")
        # self.canvas.grid(row=2,column=2)
        self.add()
        self.frames = {}
        self.frames[0] = self.entriesFrame
        self.frames[1] = self.sequenceFrame
        self.frame = self.frames[self.choice.get()]
        self.outVar = tk.StringVar(value='Output')
        self.outLabel = tk.Message(self, textvariable=self.outVar, anchor=NW, width=200, fg='black',background='white', borderwidth=0.5, relief=SOLID)
        self.outLabel.grid(row=1, column=3,padx=20,pady =10, sticky="N",columnspan=2)
        self.changeFrame(self.choice.get())
        
    def clear_entry(self,event):
        if self.mEntry.get() == 'm Value (Default = 4)':
            self.mVar.set('')
            self.mEntry.config(fg='black')

    def changeFrame(self, frame_num):
        self.clear()
        new_frame = self.frames[frame_num]
        if self.frame is not None:
            self.frame.grid_forget()
        self.frame = new_frame
        self.frame.grid(row =1, column =2,padx = 10, pady = 10)
        
    
    
    def home(self,controller):
        self.clear()
        controller.show_frame(StartPage)
    def add(self):
        
        self.symEntries.append(tk.Entry(self.entriesFrame, width=5, borderwidth=0.5, relief=SOLID)) # Create and append to list
        self.symEntries[-1].grid(row=self.count,column=1,padx=2, pady=5) # Place the just created widget
        self.probEntries.append(tk.Entry(self.entriesFrame, width=5, borderwidth=0.5, relief=SOLID)) # Create and append to list
        self.probEntries[-1].grid(row=self.count,column=2,padx=2, pady=5) # Place the just created widget
        self.newBtn.grid(row=self.count+1, column=2)
        self.count += 1 # Increase the count by 1
    def symbols_from_sequence(self, sequence):
        syms = dict.fromkeys([ord(char)-64 for char in sequence],0)
        for char in sequence:
            syms[ord(char)-64] += round(1/len(sequence),3)
        return [(k,v) for k,v in syms.items()]
        
    def compute(self):
        
        if self.seq.get() != '' or ( self.symEntries[0].get() != '' and self.probEntries[0].get() != ''):
            if self.choice.get() == 0: 
                if self.caseSensitive.get() == 0:
                    symbols = [(ord(self.symEntries[i].get().upper())-64,float(self.probEntries[i].get())) for i in range(len(self.symEntries))]
                else:
                    symbols = [(ord(self.symEntries[i].get())-64,float(self.probEntries[i].get())) for i in range(len(self.symEntries))] 

            else: 
                if self.caseSensitive.get() == 0:
                    symbols = self.symbols_from_sequence(self.seq.get().upper())
                else:
                    
                    symbols = self.symbols_from_sequence(self.seq.get())
            if self.mVar.get() == 'm Value (Default = 4)': m = 4
            else: m = self.mVar.get()
            # symbols = [('a', 0.4), ('b', 0.2), ('c',0.1), ('d', 0.1), ('e', 0.09), ('f',0.09), ('g', 0.01), ('h', 0.01)]
            self.ran = True
            
            codebook, averageLength = compGolomb(symbols, int(m))
           
            msg = ''
            msg+= str(codebook) + '\n'
            msg+= "Average Length = " + str(round(averageLength,2)) + '\n'
            if self.choice.get() == 1: 
                if self.caseSensitive.get() == 0:
                    encoded_sequence= ''.join([codebook[letter] for letter in self.seq.get().upper()])
                else:
                    encoded_sequence= ''.join([codebook[letter] for letter in self.seq.get()])
                original_length = 8*len(self.seq.get())
                compression_ratio = original_length/len(encoded_sequence)
                msg += "Encoded Sequence: " + str(encoded_sequence) + '\n'
                msg += "Compression Ratio: " + str(compression_ratio) + '\n'
            self.outVar.set(msg)
          
            


    def clear(self):

        for sym,prob in zip(self.symEntries, self.probEntries):
            sym.grid_forget()
            prob.grid_forget()
        # if self.ran:  
        #     self.canvas.delete('all')
        #     self.canvas.grid_forget()
        #     self.outLabel.grid_forget()
        self.outVar.set('Output')
        self.mVar.set('m Value (Default = 4)')
        self.mEntry.config(fg='grey')
        self.codebook = None
        self.symEntries.clear()
        self.probEntries.clear()
        self.seq.delete(0,'end')
        self.add()



# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()