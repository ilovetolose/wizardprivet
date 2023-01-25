import random
from tkinter import *
from PIL import Image, ImageTk
otvet = ['ответ: ты завтра умрешь','ответ: все верно','ответ: три коня']
shar = ['ww.jpg','yaclown.jpg','hh.jpg']
quest = ['я жду вопрос','что тебя интересует?','пиши']
root = Tk()
root['bg'] = '#fafafa'
root.title('у меня нет друзей')
root.geometry('1024x800')
def click():
        framefor = Frame(root,bg='white')
        framefor.place(relx='0.5', rely='0.3', relwidth='0.3', relheight='0.25')
        frame2 = Frame(root,bg='white')
        frame2.place(relx='0.5', rely='0.5', relwidth='0.3', relheight='0.25')
        texe = Label(frame2,bg='white',text=(otvet[random.randint(0,2)]),font='300')
        texe.place(x='50',y='50')
        quu = Label(framefor, bg='white', text=(quest[random.randint(0, 2)]), font='300')
        quu.place(x='20',y='70')
        entr.delete(0, 'end')
        canvas = Canvas(root, height=600, width=400)
        image = Image.open((shar[random.randint(0,2)]))
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        canvas.grid(row=2, column=1)
        root.mainloop()




frame = Canvas(root,width='900',height='600',bd='0')
frame.place(relwidth='1',relheight='1')
framefor = Frame(root,bg='white')
framefor.place(relx='0.5', rely='0.3', relwidth='0.3', relheight='0.25')
entr = Entry(frame,bg='white',font='100')
entr.pack()
btn = Button(frame,bg='purple',text='нажми на меня!',font='60',command=click)
btn.pack()
texe = Label(frame,bg='green',text='',font='60')
share = Label(frame,bg='green',text='',)
quu = Label(framefor, bg='white', text=(quest[random.randint(0, 2)]), font='200')
quu.place(x='20', y='70')



root.mainloop()