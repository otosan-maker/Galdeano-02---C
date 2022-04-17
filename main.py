import lvgl as lv
import keypad
from ili9XXX import ili9341
from xpt2046 import xpt2046
import eigenmath

#disp = ili9341(miso=19 , mosi=23, clk=18,cs=15,dc=02,rst=04,power=-1,backlight=-1,spihost=esp.HSPI_HOST,
#                 width=320, height=240,mhz=28,rot=-4  )

disp = ili9341()
touch=xpt2046()
import math


btnm1 = None
dicVal=["last","quote()","abs()","integral()","d()","defint()","sqrt()","clear","inv()","eval()","outer()","simplify()","factorial()","float()","sum()","product()"]

def emath_exe(e):
    global ta
    label.set_text(eigenmath.run(ta.get_text()) )
    print("exec")

def cls(e):
    ta.set_text("")
    label.set_text("")

def trig_event_handler(evt):
    global ta
    code = evt.get_code()
    obj  = evt.get_target()
    id = obj.get_selected_btn()
    txt = obj.get_btn_text(id)
    ta.add_text(txt)
    ta.cursor_left()
    btnm1.delete()


def event_handler(evt):
    global btnm1
    code = evt.get_code()
    obj  = evt.get_target()

    if code == lv.EVENT.VALUE_CHANGED :
        id = obj.get_selected_btn()
        txt = obj.get_btn_text(id)
        ta.add_text(txt)
        ta.cursor_left()
        btnm1.delete()
        #print("%s was pressed"%txt)

def trig2(e):
    global btnm1
    btnm_map = ["sin()", "cos()", "tan()", "\n",
                "arcsin()", "arccos()", "arctan()", "\n",
                "sinh()", "cosh()", "tanh()", "\n",
                "arcsinh()", "arccosh()", "arctanh()", ""]

    btnm1 = lv.btnmatrix(lv.scr_act())
    btnm1.set_map(btnm_map)
    btnm1.align(lv.ALIGN.CENTER, 0, 0)
    btnm1.add_event_cb(event_handler, lv.EVENT.ALL, None)

def insertDicFun(e):
    global cont_col
    obj2  = e.get_target()
    ta.add_text(obj2.get_child(0).get_text())
    ta.cursor_left()
    cont_col.delete()
    



def dic(e):
    global dicVal
    global cont_col
    # Create a container with COLUMN flex direction
    cont_col = lv.obj(lv.scr_act())
    cont_col.move_foreground()
    cont_col.set_size(150, 150)
    cont_col.align_to(btn2, lv.ALIGN.OUT_BOTTOM_MID, 0, -170)
    cont_col.set_flex_flow(lv.FLEX_FLOW.COLUMN)
    for index,item in enumerate(dicVal):
        # Add items to the column
        obj = lv.btn(cont_col)
        obj.set_size(lv.pct(100), lv.SIZE.CONTENT)
        obj.add_event_cb(insertDicFun, lv.EVENT.CLICKED, None)
        label = lv.label(obj)
        label.set_text(item)
        label.center()




mode=0
modeLabelTxt=["Num","alp","ALP"]



#Interfaz grafico
titulo=lv.label(lv.scr_act())
titulo.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 100, 0)
titulo.set_text("Galdeano CAS 04")
modeLabel=lv.label(lv.scr_act())
modeLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 5, 0)
modeLabel.set_text(modeLabelTxt[mode])


ta = lv.textarea(lv.scr_act())
ta.align(lv.ALIGN.TOP_LEFT, 3, 30)
ta.set_one_line(True)
ta.set_width(310)
ta.set_placeholder_text( "Escribe aqui")
ta.add_state(lv.STATE.FOCUSED)

style = lv.style_t()
style.init()
style.set_text_font(lv.galdeano_14)
obj = lv.obj(lv.scr_act())
obj.set_size(310, 120)
obj.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 3, 74)
obj.add_style(style, 0)
label = lv.label(obj)
label.set_text("")

btn1 = lv.btn(lv.scr_act())
btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 0, 200)
label_btn1 = lv.label(btn1)
label_btn1.set_text("CLS")
btn1.add_event_cb(cls, lv.EVENT.CLICKED, None)

btn2 = lv.btn(lv.scr_act())
btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, math.ceil(320/4), 200)
label_btn2 = lv.label(btn2)
label_btn2.set_text("Dic")
btn2.add_event_cb(dic, lv.EVENT.CLICKED, None)

btn3 = lv.btn(lv.scr_act())
btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, math.ceil(320*2/4), 200)
label_btn3 = lv.label(btn3)
label_btn3.set_text( "Trig" )
btn3.add_event_cb(trig2, lv.EVENT.CLICKED, None)

btn4 = lv.btn(lv.scr_act())
btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, math.ceil(320*3/4), 200)
label_btn4 = lv.label(btn4)
label_btn4.set_text("Exe")
btn4.add_event_cb(emath_exe, lv.EVENT.CLICKED, None)

#bucle
while(True):
    c = keypad.get_key(mode)
    if(c!=""):
        #print (c)
        if(c=="left"):
            ta.cursor_left()
        elif(c=="rigth"):
            ta.cursor_right()
        elif(c=="del"):
            ta.del_char()
        elif(c=="mode"):
            mode=mode+1
            if (mode>2):
                mode=0
            modeLabel.set_text(modeLabelTxt[mode])
        elif( (c=="exe") or ( c=="eval")):
            label.set_text(eigenmath.run(ta.get_text()) )
        else:
            ta.add_text(c)