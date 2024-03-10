from tkinter import *
from tkinter import ttk

#cor 
cor1= '#1E1E1E'
cor2= '#050505'
cor3= '#FEFEFE'
cor4= '#FF3037'
cor5= '#302F36'

#windows
window=Tk()
window.title('CALCULADORA')
window.geometry('235x310')
window.configure(bg=cor2) 




#bloco de frame
# Frame 1
frame1 = Frame(window, width=235, height=50, bg=cor2)
frame1.grid(row=0, column=0)
 
# Frame 2
frame2 = Frame(window, width=235, height=268)
frame2.grid(row=1, column=0)

#variavel label
valores_cheios = ''

#variavel texto
valoresTexto = StringVar()

#criando a função 1 e entendo o que funciona event
def entrar_valores(event):

    global valores_cheios
    valores_cheios = valores_cheios + str(event)

    valoresTexto.set(str(valores_cheios))

# Calcular
def calcular():
    global valores_cheios
    resultado = eval(valores_cheios)

    valoresTexto.set(str(resultado))

#limpar tela
def limpar_tela():
    global valores_cheios
    valores_cheios =''
    valoresTexto.set('')


#label
tela = Label(frame1, textvariable=valoresTexto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor5, fg=cor3,)
tela.place(x=0, y=0)

#botões bloco 1
btn1=Button(frame2, command= limpar_tela, text="C", bg=cor5, fg=cor3, width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn1.place(x=0, y=0)

btn2=Button(frame2,  command= lambda: entrar_valores('%'), text="%", bg=cor5, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn2.place(x=118, y=0)

btn3=Button(frame2, command= lambda: entrar_valores('/'), text="/", bg=cor5, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn3.place(x=177, y=0)

#botões bloco 2
btn4=Button(frame2, command= lambda: entrar_valores('7'), text="7", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn4.place(x=0, y=52)

btn5=Button(frame2, command= lambda: entrar_valores('8'), text="8", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn5.place(x=59, y=52)

btn6 =Button(frame2, command= lambda: entrar_valores('9'), text="9", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn6.place(x=118, y=52)

btn7=Button(frame2, command= lambda: entrar_valores('*'), text="*", bg=cor5, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn7.place(x=177, y=52)

#bloco 3
btn8=Button(frame2, command= lambda: entrar_valores('6'), text="6", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn8.place(x=0, y=104)

btn9=Button(frame2, command= lambda: entrar_valores('5'), text="5", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn9.place(x=59, y=104)

btn10=Button(frame2, command= lambda: entrar_valores('4'), text="4", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn10.place(x=118, y=104)

btn11=Button(frame2, command= lambda: entrar_valores('+'), text="+", bg=cor5, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn11.place(x=177, y=104)

#bloco 4
btn113=Button(frame2, command= lambda: entrar_valores('3'), text="3", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn113.place(x=0, y=156)

btn13=Button(frame2, command= lambda: entrar_valores('2'), text="2", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn13.place(x=59, y=156)

btn14=Button(frame2, command= lambda: entrar_valores('1'), text="1", bg=cor1, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn14.place(x=118, y=156)

btn15=Button(frame2, command= lambda: entrar_valores('-'), text="-", bg=cor5, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn15.place(x=177, y=156)

#bloco 5
btn16=Button(frame2, command= lambda: entrar_valores('0'), text="0", bg=cor1, fg=cor3, width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn16.place(x=0, y=208)

btn17=Button(frame2, command= lambda: entrar_valores('.'), text=".", bg=cor5, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn17.place(x=118, y=208)

btn18=Button(frame2, command= calcular, text="=", bg=cor4, fg=cor3, width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge')
btn18.place(x=177, y=208)


window.mainloop()














































































































