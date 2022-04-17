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



def event_handler(evt):
    code = evt.get_code()
    obj  = evt.get_target()

    if code == lv.EVENT.VALUE_CHANGED :
        id = obj.get_selected_btn()
        txt = obj.get_btn_text(id)

        print("%s was pressed"%txt)

btnm_map = ["1", "2", "3", "4", "5", "\n",
            "6", "7", "8", "9", "0", "\n",
            "Action1", "Action2", ""]

btnm1 = lv.btnmatrix(lv.scr_act())
btnm1.set_map(btnm_map)
btnm1.set_btn_width(10, 2)        # Make "Action1" twice as wide as "Action2"
btnm1.set_btn_ctrl(10, lv.btnmatrix.CTRL.CHECKABLE)
btnm1.set_btn_ctrl(11, lv.btnmatrix.CTRL.CHECKED)
btnm1.align(lv.ALIGN.CENTER, 0, 0)
btnm1.add_event_cb(event_handler, lv.EVENT.ALL, None)