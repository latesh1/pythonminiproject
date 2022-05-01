import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import matplotlib


class Vaccine(QDialog):
    def __init__(self):
        super(Vaccine, self).__init__()
        loadUi("bookvacc.ui", self)
        self.search.clicked.connect(self.vaccinesearch)

    def vaccinesearch(self):
        import requests
        pincode = self.pin.text()
        date = self.date1.text()

        # pincode = "0"
        # while len(pincode) != 6:
        #     pincode = input("Enter the pincode for which you want the status => ")
        #     if len(pincode) < 6:
        #         print(f"{pincode} is shorter than the actual length")
        #     elif len(pincode) > 6:
        #         print(f"{pincode} is longer than the actual length")

        # date = input("Enter the Date to get status (Date format: DD-MM-YYYY) => ")

        request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}"
        header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
        response = requests.get(request_link, headers=header)
        raw_json = response.json()
        Total_centers = len(raw_json['centers'])
        # print()
        # print("                        >>>>>>    RESULTS   <<<<<<<                                ")
        # print("-------------------------------------------------------------------------------------")
        # print(f"Date: {date} | Pincode: {pincode} ")

        # if Total_centers != 0:
        #     print(f"Total centers in your area is: {Total_centers}")
        # else:
        #     print(f"Unfortunately !! Seems like no center in this area / Kindly re-check the Pincode")
        #
        # print("------------------------------------------------------------------------------------")
        # print()

        for cent in range(Total_centers):

            # print()
            p1 = "[{cent + 1}] Center Name:", raw_json['centers'][cent]['name']
            p2 = "------------------------------------------------------------"
            p3 = "   Date      Vaccine Type    Minimum Age    Available "
            p4 = "  ------     -------------   ------------   ----------"
            p5 = raw_json['centers'][cent]['sessions']

            for _sess in range(len(p5)):
                print("{0:^12} {1:^12} {2:^14} {3:^16} ".format(p5[_sess]['date'],
                                                                p5[_sess]['vaccine'],
                                                                p5[_sess]['min_age_limit'],
                                                                p5[_sess]['available_capacity']))


# main
app = QApplication(sys.argv)
vaccine1 = Vaccine()
widget = QtWidgets.QStackedWidget()
widget.addWidget(vaccine1)
widget.setFixedHeight(900)
widget.setFixedWidth(1000)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
