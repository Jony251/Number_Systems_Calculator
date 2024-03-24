from PyQt5.QtCore import QObject, pyqtSignal

import modul_system_cal


def click(main_window):
            try:
                main_window.text_to_show = main_window.input_box.text()

                if main_window.radio_button1.isChecked():
                    main_window.text_to_show = modul_system_cal.print_system_calculator(int(main_window.text_to_show),
                                                                                        10)
                elif main_window.radio_button2.isChecked():
                    main_window.text_to_show = modul_system_cal.print_system_calculator(int(main_window.text_to_show),
                                                                                        8)
                elif main_window.radio_button3.isChecked():
                    main_window.text_to_show = modul_system_cal.print_system_calculator(int(main_window.text_to_show),
                                                                                        16)
                elif main_window.radio_button4.isChecked():
                    main_window.text_to_show = modul_system_cal.print_system_calculator(int(main_window.text_to_show),
                                                                                        2)
                elif main_window.radio_button5.isChecked():
                    main_window.text_to_show = modul_system_cal.print_system_calculator(int(main_window.text_to_show),
                                                                                        int(main_window.text_to_show_loop))
                else:
                    main_window.text_to_show = "There are some problems with the program"
            except ValueError:
                main_window.text_to_show = "The input isn't a number."
            except Exception as e:
                main_window.text_to_show = f"An error occurred: {e}"


            return main_window.text_to_show