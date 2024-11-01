from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

list_foods = ['Pizza', 'Sushi', 'Tacos', 'Baguette', 'Hamburguesa', 'Paella', 'Dim Sum', 'Kimchi']
list_drinks = ['Agua', 'Refresco', 'Cerveza', 'Vino', 'Mojito', 'Caipirinha', 'Ginebra', 'Whisky']
list_deserts = ['Tiramisú', 'Cheesecake', 'Alfajores', 'Mousse', 'Panettone', 'Coulant', 'Turrón', 'Brownie']

costs_foods = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
costs_drinks = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
costs_deserts = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_check_selections():

    for _key, _value in enumerate(checks_foods):
        if _value.get() == 1:
            if quantities_foods[_key].get() == '0':
                boxes_foods[_key].config(state=NORMAL)
                boxes_foods[_key].delete(0, END)
                boxes_foods[_key].focus()
        else:
            boxes_foods[_key].config(state=DISABLED)
            quantities_foods[_key].set('0')

    for _key, _value in enumerate(checks_drinks):
        if _value.get() == 1:
            if quantities_drinks[_key].get() == '0':
                boxes_drinks[_key].config(state=NORMAL)
                boxes_drinks[_key].delete(0, END)
                boxes_drinks[_key].focus()
        else:
            boxes_drinks[_key].config(state=DISABLED)
            quantities_drinks[_key].set('0')

    for _key, _value in enumerate(checks_deserts):
        if _value.get() == 1:
            if quantities_deserts[_key].get() == '0':
                boxes_deserts[_key].config(state=NORMAL)
                boxes_deserts[_key].delete(0, END)
                boxes_deserts[_key].focus()
        else:
            boxes_deserts[_key].config(state=DISABLED)
            quantities_deserts[_key].set('0')


def click_calc_normal_button(_value):
    calc_result.insert(END, _value)
    print(_value, calc_result.get())


def click_calc_delete_button():
    calc_result.delete(0, END)


def click_calc_result_button():
    result = str(eval(calc_result.get()))
    click_calc_delete_button()
    calc_result.insert(END, result)


def click_global_total():

    total_cost_foods = 0
    for _key, _value in enumerate(quantities_foods):
        total_cost_foods = total_cost_foods + int(_value.get()) * costs_foods[_key]
    cost_qty_foods.delete(0, END)
    cost_qty_foods.insert(END, str(round(total_cost_foods, 2)))

    total_cost_drinks = 0
    for _key, _value in enumerate(quantities_drinks):
        total_cost_drinks = total_cost_drinks + int(_value.get()) * costs_drinks[_key]
    cost_qty_drinks.delete(0, END)
    cost_qty_drinks.insert(END, str(round(total_cost_drinks, 2)))

    total_cost_deserts = 0
    for _key, _value in enumerate(quantities_deserts):
        total_cost_deserts = total_cost_deserts + int(_value.get()) * costs_deserts[_key]
    cost_qty_deserts.delete(0, END)
    cost_qty_deserts.insert(END, str(round(total_cost_deserts, 2)))

    total_cost_subtotal = total_cost_foods + total_cost_drinks + total_cost_deserts
    cost_qty_subtotal.delete(0, END)
    cost_qty_subtotal.insert(END, str(round(total_cost_subtotal, 2)))

    total_cost_taxes = total_cost_subtotal * 0.10
    cost_qty_taxes.delete(0, END)
    cost_qty_taxes.insert(END, str(round(total_cost_taxes, 2)))

    total_cost_total = total_cost_subtotal + total_cost_taxes
    cost_qty_total.delete(0, END)
    cost_qty_total.insert(END, str(round(total_cost_total, 2)))


def click_global_ticket():
    text_ticket.delete(1.0, END)
    ticket_num = random.randint(1000, 9999)
    ticket_datetime = datetime.datetime.now().strftime('%d/%m/%y %H:%M')
    text_ticket.insert(END, f' Datos: N# - {ticket_num}   Fecha: {ticket_datetime}\n')
    text_ticket.insert(END, '*' * 43 + '\n')
    text_ticket.insert(END, f'     Precio de la comida:      {cost_qty_foods.get()} €\n')
    text_ticket.insert(END, f'     Precio de la bebida:      {cost_qty_drinks.get()} €\n')
    text_ticket.insert(END, f'     Precio de los postres:    {cost_qty_deserts.get()} €\n')
    text_ticket.insert(END, '    ' + '-' * 35 + '\n')
    text_ticket.insert(END, f'     Subtotal:                 {cost_qty_subtotal.get()} €\n')
    text_ticket.insert(END, f'     Impuestos (10%):          {cost_qty_taxes.get()} €\n')
    text_ticket.insert(END, '    ' + '-' * 35 + '\n')
    text_ticket.insert(END, f'     Total:                    {cost_qty_total.get()} €\n')


def click_global_save():
    info_recibo = text_ticket.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def click_global_reset():

    text_ticket.delete(0.1, END)

    for i in range(len(list_foods)):
        quantities_foods[i].set('0')
        boxes_foods[i].config(state=DISABLED)
        checks_foods[i].set(0)

    for i in range(len(list_drinks)):
        quantities_drinks[i].set('0')
        boxes_drinks[i].config(state=DISABLED)
        checks_drinks[i].set(0)

    for i in range(len(list_deserts)):
        quantities_deserts[i].set('0')
        boxes_deserts[i].config(state=DISABLED)
        checks_deserts[i].set(0)

    cost_qty_foods.delete(0, END)
    cost_qty_foods.insert(END, '0')
    cost_qty_drinks.delete(0, END)
    cost_qty_drinks.insert(END, '0')
    cost_qty_deserts.delete(0, END)
    cost_qty_deserts.insert(END, '0')
    cost_qty_subtotal.delete(0, END)
    cost_qty_subtotal.insert(END, '0')
    cost_qty_taxes.delete(0, END)
    cost_qty_taxes.insert(END, '0')
    cost_qty_total.delete(0, END)
    cost_qty_total.insert(END, '0')


def subframe_left_top(_frame, section):

    frame = LabelFrame(_frame,
                       bd=1,
                       relief=FLAT,
                       text=section,
                       bg='burlywood',
                       fg='azure4',
                       font=('Corbel', 16, 'bold'))
    frame.pack(side=LEFT)
    return frame


def element_left_top(_list, _frame):
    checks = []
    boxes = []
    quantities = []
    for _key, _value in enumerate(_list):
        checks.append(IntVar())
        check = Checkbutton(_frame,
                            text=_value,
                            font=('Corbel', 12),
                            bg='burlywood',
                            onvalue=1,
                            offvalue=0,
                            variable=checks[_key],
                            command=click_check_selections)
        check.grid(row=_key,
                   column=0,
                   sticky=W)
        quantities.append(StringVar())
        quantities[_key].set('0')
        box = Entry(_frame,
                    font=('Courier', 10),
                    bd=1,
                    width=6,
                    state=DISABLED,
                    textvariable=quantities[_key])
        box.grid(row=_key,
                 column=1,
                 sticky=W)
        boxes.append(box)

    return checks, boxes, quantities


def element_left_down(_section, _frame, _position, _variable):

    section = Label(_frame,
                    text=_section,
                    font=('Corbel', 12, 'bold'),
                    bg='azure4',
                    fg='white')
    section.grid(row=_position[0], column=_position[1])
    qty = Entry(_frame,
                font=('Courier', 10),
                bd=1,
                width=10,
                textvariable=_variable)
    qty.grid(row=_position[0], column=_position[1] + 1, padx=33)

    return section, qty


# Settings of window

app = Tk()
app.geometry('840x450+200+100')  # Tamaño y posición
app.resizable(False, False)  # No se peude cambiar ni eje x, ni eje y
app.title('Mi Restaurante - Sistema de Facturación')
app.config(bg='burlywood')

# TOP FRAME

frame_top = Frame(app, bd=1, relief=FLAT)
frame_top.pack(side=TOP)

frame_left = Frame(app, bd=1, relief=FLAT)
frame_left.pack(side=LEFT)

frame_costs = Frame(frame_left, bd=1, relief=FLAT, bg='azure4')  # Dentro del frame_left
frame_costs.pack(side=BOTTOM)

frame_foods = subframe_left_top(frame_left, 'Comidas')
frame_drinks = subframe_left_top(frame_left, 'Bebidas')
frame_deserts = subframe_left_top(frame_left, 'Postres')

frame_right = Frame(app, bd=1, relief=FLAT)
frame_right.pack(side=RIGHT)

frame_calc = Frame(frame_right, bd=1, relief=FLAT)  # Dentro del frame_right
frame_calc.pack()  # Por defecto arriba a la izquierda

frame_ticket = Frame(frame_right, bd=1, relief=FLAT)
frame_ticket.pack()

frame_buttons = Frame(frame_right, bd=1, relief=FLAT)
frame_buttons.pack()


# TITLE

label_title = Label(frame_top, width=27, text='Sistema de Facturación',
                    bg='burlywood', fg='azure4', font=('Corbel', 36))
label_title.grid(row=0, column=0)

# LEFT - TOP PANEL

checks_foods, boxes_foods, quantities_foods = element_left_top(list_foods, frame_foods)
checks_drinks, boxes_drinks, quantities_drinks = element_left_top(list_drinks, frame_drinks)
checks_deserts, boxes_deserts, quantities_deserts = element_left_top(list_deserts, frame_deserts)

# LEFT - DOWN FRAME

cost_section_foods, cost_qty_foods = element_left_down('Precio Comidas', frame_costs, [0, 0], IntVar())
cost_section_drinks, cost_qty_drinks = element_left_down('Precio Bebidas', frame_costs, [1, 0], IntVar())
cost_section_deserts, cost_qty_deserts = element_left_down('Precio Postres', frame_costs, [2, 0], IntVar())
cost_section_subtotal, cost_qty_subtotal = element_left_down('SubTotal', frame_costs, [0, 2], IntVar())
cost_section_taxes, cost_qty_taxes = element_left_down('Impuestos', frame_costs, [1, 2], IntVar())
cost_section_total, cost_qty_total = element_left_down('Total', frame_costs, [2, 2], IntVar())


# RIGHT - MIDDLE FRAME

text_ticket = Text(frame_ticket,
                   font=('Courier', 10),
                   bd=1,
                   width=43,
                   height=10)
text_ticket.grid(row=0, column=0)

# RIGHT - DOWN FRAME

list_global_buttons = ['total', 'recibo', 'guardar', 'resetear']

global_buttons=[]
for _key, _value in enumerate(list_global_buttons):
    _button = Button(frame_buttons,
                     text=_value,
                     font=('Corbel', 12, 'bold'),
                     fg='white',
                     bg='azure4',
                     bd=1,
                     width=9)
    _button.grid(row=0, column=_key)
    global_buttons.append(_button)

global_buttons[0].config(command=click_global_total)
global_buttons[1].config(command=click_global_ticket)
global_buttons[2].config(command=click_global_save)
global_buttons[3].config(command=click_global_reset)

# RIGHT - TOP FRAME

calc_result = Entry(frame_calc,
                    font=('Courier', 10, 'bold'),
                    bd=1,
                    width=45)
calc_result.grid(row=0, column=0, columnspan=4)

calc_list_buttoms = ['7', '8', '9', '+',
                     '4', '5', '6', '-',
                     '1', '2', '3', 'x',
                     'R', 'B', '0', '/']
calc_buttons = []
for calc_key, calc_value in enumerate(calc_list_buttoms):
    _button = Button(frame_calc,
                     text=calc_value,
                     font=('Corbel', 12),
                     fg='white',
                     bg='azure4',
                     bd=1,
                     width=8)
    _button.grid(row=calc_key // 4 + 1, column=calc_key % 4)
    calc_buttons.append(_button)

calc_buttons[0].config(command=lambda: click_calc_normal_button('7'))
calc_buttons[1].config(command=lambda: click_calc_normal_button('8'))
calc_buttons[2].config(command=lambda: click_calc_normal_button('9'))
calc_buttons[3].config(command=lambda: click_calc_normal_button('+'))
calc_buttons[4].config(command=lambda: click_calc_normal_button('4'))
calc_buttons[5].config(command=lambda: click_calc_normal_button('5'))
calc_buttons[6].config(command=lambda: click_calc_normal_button('6'))
calc_buttons[7].config(command=lambda: click_calc_normal_button('-'))
calc_buttons[8].config(command=lambda: click_calc_normal_button('1'))
calc_buttons[9].config(command=lambda: click_calc_normal_button('2'))
calc_buttons[10].config(command=lambda: click_calc_normal_button('3'))
calc_buttons[11].config(command=lambda: click_calc_normal_button('*'))
calc_buttons[12].config(command=click_calc_result_button)
calc_buttons[13].config(command=click_calc_delete_button)
calc_buttons[14].config(command=lambda: click_calc_normal_button('0'))
calc_buttons[15].config(command=lambda: click_calc_normal_button('/'))


app.mainloop()