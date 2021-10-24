from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

def reset():
    textRecipent.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_Mixedveg.set('0')
    e_paneer.set('0')
    e_kofta.set('0')
    e_chicken.set('0')
    e_Manchurian.set('0')
    e_Korma.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_jaljera.set('0')
    e_roohfaza.set('0')
    e_masalatea.set('0')
    e_buttermilk.set('0')
    e_colddrink.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textMixedveg.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textKofta.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textManchurian.config(state=DISABLED)
    textKorma.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textjaljera.config(state=DISABLED)
    textroohfaza.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textbuttermilk.config(state=DISABLED)
    textcolddrink.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)

    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    costofcakesvar.set('')
    costofdrinksvar.set('')
    costoffoodvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def send():
    def send_msg():
        message=textarea.get(1.0,END)
        number=numberfield.get()
        auth='UVi9MI5E0rZdDC2G1jkKPWsBxOfXcnegmJSthq4vbRL7wulpoTAXxT39n1VCduNMSizgjU74pYO5r0L6'
        url='https://www.fast2sms.com/dev/bulk'
        params={
            'authoriztion':auth,
            'message':message,
            'numbers':number,
            'sender-id':'FSTSMS',
            'route':'p',
            'language':'english'
        }
        response=requests.get(url,params=params)
        dic=response.json()
        result=dic.get('return')
        if result==True:
            messagebox.showinfo('send successfully','Message sent successfully')
        else:
            messagebox.showerror('Error','Something went wrong')


    root2=Toplevel()
    root2.title('SEND BILL')
    root2.config(bg='red')
    root2.geometry('485x620+50+50')
    # root2.mainloop()

    numberLabel = Label(root2,text='Mobile Number',font=('arial',18,'bold underline') ,bg='red',fg='white')
    numberLabel.pack(pady=5)
    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=22)
    numberfield.pack(pady=5)
    billlabel= Label(root2,text='BILL DETAILS',font=('arial',18,'bold underline') ,bg='red',fg='white')
    billlabel.pack(pady=5)
    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END, 'receipt ref:\t' + billnumber + '\t' + date + '\n')

    if costoffoodvar.get() != '0 Rs':
        textarea.insert(END, f'Cost of food \t{priceofFood} Rs\n')
    if costofdrinksvar.get() != '0 Rs':
        textarea.insert(END, f'Cost of Drinks \t{priceofDrinks} Rs\n')
    if costofcakesvar.get() != '0 Rs':
        textarea.insert(END, f'Cost of Cakes\t{priceofCakes} Rs\n')

    textarea.insert(END, f'Sub Total \t{subtotalofitems} Rs\n')
    textarea.insert(END, f'Service Tax \t{50} Rs\n')
    textarea.insert(END, f'Total Cost \t{subtotalofitems + 50} Rs\n')

    sendButton=Button(root2,text='SEND',font=('arial',15,'bold'),bg='white',fg='red',bd=7,relief=GROOVE,command=send_msg)
    sendButton.pack(pady=5)
    root2.mainloop()



def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textRecipent.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','your bill is saved successfully')



def receipt():
    global billnumber,date
    textRecipent.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date= time.strftime('%d/%m/%Y')
    textRecipent.insert(END,'Receipt Ref:\t\t' + billnumber+ '\t'+date+'\n')
    textRecipent.insert(END,'****************************************'+'\n')
    textRecipent.insert(END,'Items:\t cost of items (Rs)'+'\n')
    textRecipent.insert(END,'*****************************************'+'\n')
    if e_roti.get()!='0':
        textRecipent.insert(END,f'Roti \t{int(e_roti.get())*10}\n')

    if e_daal.get()!= '0':
        textRecipent.insert(END, f'Daal\t{int(e_daal.get())*60}\n')

    if e_fish.get() != '0':
        textRecipent.insert(END, f'Fish\t{int(e_fish.get())*100}\n')

    if e_Mixedveg.get() != '0':
        textRecipent.insert(END, f'Mixed Veg\t{int(e_Mixedveg.get())*80}\n')

    if e_paneer.get() !='0':
        textRecipent.insert(END, f'Paneer\t{int(e_paneer.get())*80}\n')

    if e_kofta.get() != '0':
        textRecipent.insert(END, f'Kofta\t{int(e_kofta.get())*90}\n')

    if e_chicken.get() != '0':
        textRecipent.insert(END, f'Chicken\t{int(e_chicken.get())*270}\n')

    if e_Manchurian.get() !='0' :
        textRecipent.insert(END, f'Manchurian\t{int(e_Manchurian.get())*90}\n')

    # if e_Korma().get() != '0':
    #     textRecipent.insert(END, f'Korma\t{int(e_Korma.get())*220}\n')

    if e_lassi.get() != '0':
        textRecipent.insert(END, f'Lassi\t{int(e_lassi.get())*75}\n')

    if e_coffee.get() != '0':
        textRecipent.insert(END, f'Coffee\t{int(e_coffee.get())*80}\n')

    if e_faluda.get() !='0':
        textRecipent.insert(END, f'Faluda\t{int(e_faluda.get())*25}\n')

    if e_shikanji.get() != '0':
        textRecipent.insert(END, f'Shikanji\t{int(e_shikanji.get())*15}\n')

    if e_jaljera.get() != '0':
        textRecipent.insert(END, f'Jaljera\t{int(e_jaljera.get())*10}\n')

    if e_roohfaza.get() != '0':
        textRecipent.insert(END, f'Roohfaza\t{int(e_roti.get())*30}\n')

    if e_masalatea.get() !='0':
        textRecipent.insert(END, f'Masala Tea\t{int(e_masalatea.get())*15}\n')

    if e_buttermilk.get() != '0':
        textRecipent.insert(END, f'Buttermilk\t{int(e_buttermilk.get())*25}\n')

    if e_colddrink.get() != '0':
        textRecipent.insert(END, f'Cold Drink\t{int(e_colddrink.get())*75}\n')

    if e_oreo.get() !='0':
        textRecipent.insert(END, f'Oreo\t{int(e_oreo.get()) * 70}\n')

    if e_apple.get() != '0':
        textRecipent.insert(END, f'Apple\t{int(e_apple.get()) * 99}\n')

    if e_kitkat.get() != '0':
        textRecipent.insert(END, f'Kitkat\t{int(e_kitkat.get()) * 66}\n')

    if e_vanilla.get() != '0':
        textRecipent.insert(END, f'Vanilla\t{int(e_vanilla.get()) * 75}\n')

    if e_banana.get() != '0':
        textRecipent.insert(END, f'Banana\t{int(e_banana.get()) * 60}\n')

    if e_brownie.get() != '0':
        textRecipent.insert(END, f'Brownie\t{int(e_brownie.get()) * 100}\n')

    if e_pineapple.get() != '0':
        textRecipent.insert(END, f'Pineapple\t{int(e_pineapple.get()) * 80}\n')

    if e_chocolate.get() != '0':
        textRecipent.insert(END, f'Chocolate\t{int(e_chocolate.get()) * 80}\n')

    if e_blackforest.get() != '0':
        textRecipent.insert(END, f'BlackForest\t{int(e_blackforest.get()) * 80}\n')

    textRecipent.insert(END, '****************************************' + '\n')
    if costoffoodvar.get()!='0 Rs':
        textRecipent.insert(END,f'Cost of food \t{priceofFood} Rs\n')
    if costoffoodvar.get() != '0 Rs':
        textRecipent.insert(END, f'Cost of Drinks \t{priceofDrinks} Rs\n')
    if costoffoodvar.get() != '0 Rs':
        textRecipent.insert(END, f'Cost of Cakes\t{priceofCakes} Rs\n')
    textRecipent.insert(END, '****************************************' + '\n')
    textRecipent.insert(END, f'Sub Total \t{subtotalofitems} Rs\n')
    textRecipent.insert(END, f'Service Tax \t{50} Rs\n')
    textRecipent.insert(END, f'Total Cost \t{subtotalofitems+50} Rs\n')
    textRecipent.insert(END, '****************************************' + '\n')


def totalcost():
    global priceofFood,priceofDrinks, priceofCakes, subtotalofitems
    item1=int(e_roti.get())
    item2=int(e_daal.get())
    item3=int(e_fish.get())
    item4 =int(e_Mixedveg.get())
    item5 = int(e_paneer.get())
    item6=int(e_kofta.get())
    item7=int(e_chicken.get())
    item8= int(e_Manchurian.get())
    item9 = int(e_Korma.get())
    item10=int(e_lassi.get())
    item11=int(e_coffee.get())
    item12=int(e_faluda.get())
    item13=int(e_shikanji.get())
    item14=int(e_jaljera.get())
    item15=int(e_roohfaza.get())
    item16=int(e_masalatea.get())
    item17=int(e_buttermilk.get())
    item18=int(e_colddrink.get())
    item19=int(e_oreo.get())
    item20=int(e_apple.get())
    item21=int(e_kitkat.get())
    item22=int(e_vanilla.get())
    item23=int(e_banana.get())
    item24=int(e_brownie.get())
    item25=int(e_pineapple.get())
    item26=int(e_chocolate.get())
    item27=int(e_blackforest.get())

    priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*80)+(item5*80)+(item6*90)+(item7*270)+(item8*90)\
                 +(item9*220)

    priceofDrinks=(item10*75)+(item11*80)+(item12*25)+(item13*15)+(item14*10)+(item15*30)+(item16*15)\
                   +(item17*25)+(item18*75)

    priceofCakes=(item19*70)+(item20*99)+(item21*66)+(item22*75)+(item23*60)+(item24*100)\
                   +(item25*80)+(item26*80)+(item27*80)

    costoffoodvar.set(str(priceofFood)+' Rs')
    costofdrinksvar.set(str(priceofDrinks)+' Rs')
    costofcakesvar.set(str(priceofCakes)+' Rs')
    subtotalofitems=priceofFood+priceofCakes+priceofDrinks
    subtotalvar.set(str(subtotalofitems)+' Rs')
    servicetaxvar.set('50 Rs')
    tottalcost=subtotalofitems+50
    totalcostvar.set(str(tottalcost)+' Rs')


def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def Mixedveg():
    if var4.get()==1:
        textMixedveg.config(state=NORMAL)
        textMixedveg.delete(0,END)
        textMixedveg.focus()
    else:
        textMixedveg.config(state=DISABLED)
        e_Mixedveg.set('0')

def paneer():
    if var5.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def Kofta():
    if var6.get()==1:
        textKofta.config(state=NORMAL)
        textKofta.delete(0,END)
        textKofta.focus()
    else:
        textKofta.config(state=DISABLED)
        e_kofta.set('0')

def chicken():
    if var7.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def Manchurian():
    if var8.get()==1:
        textManchurian.config(state=NORMAL)
        textManchurian.delete(0,END)
        textManchurian.focus()
    else:
        textManchurian.config(state=DISABLED)
        e_Manchurian.set('0')

def Korma():
    if var9.get()==1:
        textKorma.config(state=NORMAL)
        textKorma.delete(0,END)
        textKorma.focus()
    else:
        textKorma.config(state=DISABLED)
        e_Korma.set('0')

def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def faluda():
    if var12.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')

def shikanji():
    if var13.get()==1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')

def jaljera():
    if var14.get()==1:
        textjaljera.config(state=NORMAL)
        textjaljera.delete(0,END)
        textjaljera.focus()
    else:
        textjaljera.config(state=DISABLED)
        e_jaljera.set('0')

def roohfaza():
    if var15.get()==1:
        textroohfaza.config(state=NORMAL)
        textroohfaza.delete(0,END)
        textroohfaza.focus()
    else:
        textroohfaza.config(state=DISABLED)
        e_roohfaza.set('0')

def masalatea():
    if var16.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')

def buttermilk():
    if var17.get()==1:
        textbuttermilk.config(state=NORMAL)
        textbuttermilk.delete(0,END)
        textbuttermilk.focus()
    else:
        textbuttermilk.config(state=DISABLED)
        e_buttermilk.set('0')

def colddrink():
    if var18.get()==1:
        textcolddrink.config(state=NORMAL)
        textcolddrink.delete(0,END)
        textcolddrink.focus()
    else:
        textcolddrink.config(state=DISABLED)
        e_colddrink.set('0')

def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0, END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0, END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')

def browine():
    if var24.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')

def pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def chocolate():
    if var26.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')

def blackforest():
    if var27.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

root=Tk()
root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title('RESTURANT MANAGEMENT SYSTEM')
root.config(bg='black')
topFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
topFrame.pack(side=TOP)
labelTittle=Label(topFrame, text='FOOD CORNER',font=('arial',30,'bold'),
                  fg='white',bg='red',width=51,bd=9)
labelTittle.grid(row=0,column=0)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='white')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='white',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='FOOD',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='DRINKS',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='CAKES',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calaculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calaculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()

var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()


var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()




e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_Mixedveg=StringVar()
e_paneer=StringVar()
e_kofta=StringVar()
e_chicken=StringVar()
e_Manchurian=StringVar()
e_Korma=StringVar()


e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_Mixedveg.set('0')
e_paneer.set('0')
e_kofta.set('0')
e_chicken.set('0')
e_Manchurian.set('0')
e_Korma.set('0')


e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_jaljera=StringVar()
e_roohfaza=StringVar()
e_masalatea=StringVar()
e_buttermilk=StringVar()
e_colddrink=StringVar()


e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_jaljera.set('0')
e_roohfaza.set('0')
e_masalatea.set('0')
e_buttermilk.set('0')
e_colddrink.set('0')



e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pineapple=StringVar()
e_chocolate=StringVar()
e_blackforest=StringVar()



e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_blackforest.set('0')


costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()



roti=Checkbutton(foodFrame,text='Roti',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

Mixedveg=Checkbutton(foodFrame,text='Mixed Veg',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var4,command=Mixedveg)
Mixedveg.grid(row=3,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var5,command=paneer)
paneer.grid(row=4,column=0,sticky=W)

kofta=Checkbutton(foodFrame,text='Kofta',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var6,command=Kofta)
kofta.grid(row=5,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='chicken',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var7,command=chicken)
chicken.grid(row=6,column=0,sticky=W)

Manchurian=Checkbutton(foodFrame,text='Manchurian',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var8,command=Manchurian)
Manchurian.grid(row=7,column=0,sticky=W)

Korma=Checkbutton(foodFrame,text='Korma',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var9,command=Korma)
Korma.grid(row=8,column=0,sticky=W)

textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textMixedveg=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Mixedveg)
textMixedveg.grid(row=3,column=1)

textpaneer=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=4,column=1)

textKofta=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kofta)
textKofta.grid(row=5,column=1)

textchicken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=6,column=1)

textManchurian=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Manchurian)
textManchurian.grid(row=7,column=1)

textKorma=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Korma)
textKorma.grid(row=8,column=1)


lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var13,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

jaljera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var14,command=jaljera)
jaljera.grid(row=4,column=0,sticky=W)

Roohfaza=Checkbutton(drinksFrame,text='Roohfaza',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var15,command=roohfaza)
Roohfaza.grid(row=5,column=0,sticky=W)

Masalatea=Checkbutton(drinksFrame,text='Masala Tea',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var16,command=masalatea)
Masalatea.grid(row=6,column=0,sticky=W)

Buttermilk=Checkbutton(drinksFrame,text='Buttermilk',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var17,command=buttermilk)
Buttermilk.grid(row=7,column=0,sticky=W)

Colddrink=Checkbutton(drinksFrame,text='Cold Drink',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var18,command=colddrink)
Colddrink.grid(row=8,column=0,sticky=W)




textlassi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textfaluda=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2,column=1)

textshikanji=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=3,column=1)

textjaljera=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jaljera)
textjaljera.grid(row=4,column=1)

textroohfaza=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohfaza)
textroohfaza.grid(row=5,column=1)

textmasalatea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6,column=1)

textbuttermilk=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_buttermilk)
textbuttermilk.grid(row=7,column=1)

textcolddrink=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_colddrink)
textcolddrink.grid(row=8,column=1)


oreo=Checkbutton(cakesFrame,text='Oreo',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo)
oreo.grid(row=0,column=0,sticky=W)

apple=Checkbutton(cakesFrame,text='Apple',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var20,command=apple)
apple.grid(row=1,column=0,sticky=W)

kitkat=Checkbutton(cakesFrame,text='Kitkat',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var21,command=kitkat)
kitkat.grid(row=2,column=0,sticky=W)

vanilla=Checkbutton(cakesFrame,text='Vanilla',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanilla.grid(row=3,column=0,sticky=W)

banana=Checkbutton(cakesFrame,text='Banana',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var23,command=banana)
banana.grid(row=4,column=0,sticky=W)

brownie=Checkbutton(cakesFrame,text='Brownie',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var24,command=browine)
brownie.grid(row=5,column=0,sticky=W)

pineapple=Checkbutton(cakesFrame,text='Pineapple',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var25,command=pineapple)
pineapple.grid(row=6,column=0,sticky=W)

choclate=Checkbutton(cakesFrame,text='Chocolate',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var26,command=chocolate)
choclate.grid(row=7,column=0,sticky=W)

blackforest=Checkbutton(cakesFrame,text='Black Forest',font=('arial',19,'bold'),onvalue=1,offvalue=0,variable=var27,command=blackforest)
blackforest.grid(row=8,column=0,sticky=W)




textoreo=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textbrownie=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)

textpineapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textchocolate=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)

textblackforest=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)



lableCostofFood=Label(costFrame,text="COST OF FOOD",font=('arial',16,'bold'),bg='white',fg='black')
lableCostofFood.grid(row=0,column=0)
textCostofFood=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

lableCostofDrinks=Label(costFrame,text="COST OF DRINKS",font=('arial',16,'bold'),bg='white',fg='black')
lableCostofDrinks.grid(row=1,column=0)
textCostofDrinks=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

lableCostofCakes=Label(costFrame,text="COST OF CAKES",font=('arial',16,'bold'),bg='white',fg='black')
lableCostofCakes.grid(row=2,column=0)
textCostofCakes=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

lablesubtotal=Label(costFrame,text="SUB TOTAL",font=('arial',16,'bold'),bg='white',fg='black')
lablesubtotal.grid(row=0,column=2)
textsubtotal=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textsubtotal.grid(row=0,column=3,padx=41)


lableservicetax=Label(costFrame,text="SERVICE TAX",font=('arial',16,'bold'),bg='white',fg='black')
lableservicetax.grid(row=1,column=2)
textservicetax=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textservicetax.grid(row=1,column=3,padx=41)

lableTotalCost=Label(costFrame,text="TOTAL COST",font=('arial',16,'bold'),bg='white',fg='black')
lableTotalCost.grid(row=2,column=2)
textTotalCost=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)


# buttons
buttonTotal=Button(buttonFrame,text='TOTAL',font=('arial',10,'bold'),bg='white',fg='red',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='RECEIPT',font=('arial',10,'bold'),bg='white',fg='red',bd=3,padx=5,
                     command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='SAVE',font=('arial',10,'bold'),bg='white',fg='red',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='SEND',font=('arial',10,'bold'),bg='white',fg='red',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='RESET',font=('arial',10,'bold'),bg='white',fg='red',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

textRecipent=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textRecipent.grid(row=0,column=0)

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)
def clear():
        global operator
        operator=''
        calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''








calculatorField=Entry(calaculatorFrame,font=('arial',12,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calaculatorFrame,text='7',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calaculatorFrame,text='8',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calaculatorFrame,text='9',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calaculatorFrame,text='+',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calaculatorFrame,text='4',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4, command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calaculatorFrame,text='5',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calaculatorFrame,text='6',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calaculatorFrame,text='-',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calaculatorFrame,text='1',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calaculatorFrame,text='2',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calaculatorFrame,text='3',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonstar=Button(calaculatorFrame,text='*',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('*'))
buttonstar.grid(row=3,column=3)

buttonans=Button(calaculatorFrame,text='ANS',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calaculatorFrame,text='CLR',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calaculatorFrame,text='0',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttondivide=Button(calaculatorFrame,text='/',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=4,command=lambda:buttonClick('/'))
buttondivide.grid(row=4,column=3)


root.mainloop()
