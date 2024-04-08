from PyQt5.QtCore import QObject, pyqtSignal

import modul_system_cal


def click(main_window):
    str_dec = "10"
    str_oct = "8"
    str_hex = "16"
    str_bin = "2"
    try:
        main_window.text_to_show = ""
        input_t = main_window.input_box.text()
        input_tipe = main_window.input_base.text()
        if main_window.radio_but_dec.isChecked():
            main_window.text_to_show = modul_system_cal.system_calculator(str_dec, input_t)

        elif main_window.radio_but_oct.isChecked():
            main_window.text_to_show = modul_system_cal.system_calculator(str_oct, input_t)

        elif main_window.radio_but_hex.isChecked():
            main_window.text_to_show = modul_system_cal.system_calculator(str_hex, input_t)

        elif main_window.radio_but_bin.isChecked():
            main_window.text_to_show = modul_system_cal.system_calculator(str_bin, input_t)

        elif main_window.radio_but_user_base.isChecked():
            main_window.text_to_show = modul_system_cal.system_calculator(input_tipe, input_t)

        else:
            main_window.text_to_show = "There are some problems with the program"

    except ValueError:
        main_window.text_to_show = "The input isn't a number."

    except Exception as e:
        main_window.text_to_show = f"An error occurred: {e}"

    return main_window.text_to_show
