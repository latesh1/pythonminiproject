import sys
import loginimg
import doctorimg
import getvacc
import graph
import homepage
import bookvacc
import certificate
import covaxin
import covidsheild
import status
import faqs
import getvaccine
import setting
import profile
import appoint
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import sqlite3

con = sqlite3.connect("vaccination_db")


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.registerin.clicked.connect(self.gotoregister)

    def loginfunction(self):
        user = self.namefield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error1.setText("Please input all fields.")

        else:
            conn = sqlite3.connect("vaccination_db")
            cur = conn.cursor()
            query = 'SELECT password FROM signup WHERE username =\'' + user + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Successfully logged in.")
                self.error1.setText("")
                self.gotohomepage()
            else:
                self.error1.setText("Invalid username or password")

    def gotohomepage(self):
        login = Homepage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoregister(self):
        register1 = Registration()
        widget.addWidget(register1)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Homepage(QDialog):
    def __init__(self):
        super(Homepage, self).__init__()
        loadUi("homepage.ui", self)
        self.profile.clicked.connect(self.gotoprofile)
        self.setting.clicked.connect(self.gotosetting)
        self.health.clicked.connect(self.gotohealth)
        self.vaccstatus.clicked.connect(self.gotovaccstatus)
        self.getvacc.clicked.connect(self.gotogetvacc)
        self.logout.clicked.connect(self.directtologin)

    def gotoprofile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosetting(self):
        setting = Setting()
        widget.addWidget(setting)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotohealth(self):
        health = Health()
        widget.addWidget(health)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotovaccstatus(self):
        vaccstatus = Vaccstatus()
        widget.addWidget(vaccstatus)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotogetvacc(self):
        getvaccination = Getvaccination()
        widget.addWidget(getvaccination)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtologin(self):
        login2 = Login()
        widget.addWidget(login2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("profile.ui", self)
        self.back.clicked.connect(self.directtohome)
        self.logout.clicked.connect(self.directtologin)

    def directtohome(self):
        home2 = Homepage()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtologin(self):
        login2 = Login()
        widget.addWidget(login2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Registration(QDialog):
    def __init__(self):
        super(Registration, self).__init__()
        loadUi("registration.ui", self)
        self.back.clicked.connect(self.directtologin)
        self.createaccount.clicked.connect(self.signup)

    def signup(self):
        user = self.namefield.text()
        password = self.passwordfield.text()
        confirmpassword = self.password.text()
        emailid = self.email.text()
        mobile = self.phone.text()
        city = self.city.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0 or len(emailid) == 0 or len(
                mobile) == 0 or len(city) == 0:
            self.error2.setText("please enter all the necessary details!")

        elif password != confirmpassword:
            self.error2.setText("passwords are not matching!")
        else:

            conn = sqlite3.connect("vaccination_db")
            cur = conn.cursor()

            reg_data = [user, password, confirmpassword, emailid, mobile, city]
            cur.execute(
                'INSERT INTO signup (username, password ,confirmpassword,email,phone,city) VALUES (?,?,?,?,?,?)',
                reg_data)

            conn.commit()
            conn.close()

            self.error2.setText("registered successfully!")

    def directtologin(self):
        login2 = Login()
        widget.addWidget(login2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Setting(QDialog):
    def __init__(self):
        super(Setting, self).__init__()
        loadUi("setting.ui", self)
        self.back.clicked.connect(self.directtohome)
        self.change.clicked.connect(self.directtopass)
        self.click.clicked.connect(self.directtofaq)

    def directtohome(self):
        home2 = Homepage()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtopass(self):
        change = Changepassword()
        widget.addWidget(change)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtofaq(self):
        faq1 = Faq()
        widget.addWidget(faq1)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Health(QDialog):
    def __init__(self):
        super(Health, self).__init__()
        loadUi("health.ui", self)
        self.back.clicked.connect(self.directtohome)
        self.ok.clicked.connect(self.okset)
        self.video.clicked.connect(self.videoset)

    def videoset(self):
        import numpy as np
        import cv2 as cv
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here

            # Display the resulting frame
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()

    def directtohome(self):
        home2 = Homepage()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def okset(self):
        date = self.lineEdit.text()
        time = self.lineEdit_2.text()
        sideeffects = self.txt.toPlainText()

        if len(date) == 0 or len(time) == 0 or len(sideeffects) == 0:
            self.error4.setText("please enter alld the necessary details!")

        else:

            conn = sqlite3.connect("vaccination_db")
            cur = conn.cursor()

            cur.execute(
                'INSERT INTO health (date , time , text) VALUES (?,?,?)',
                (date, time, sideeffects))

            conn.commit()
            conn.close()

    def okset(self):
        appointment = Appoint()
        widget.addWidget(appointment)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Vaccstatus(QDialog):
    def __init__(self):
        super(Vaccstatus, self).__init__()
        loadUi("Vaccination_stats.ui", self)
        self.back.clicked.connect(self.directtohome)
        self.get.clicked.connect(self.getnow)

    def directtohome(self):
        home2 = Homepage()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def getnow(self):
        import requests
        import lxml
        from bs4 import BeautifulSoup
        import textwrap
        url = "https://www.bing.com/search?q=covid+vaccination+status+india&qs=n&form=QBRE&sp=-1&ghc=1&pq=covid+vaccination+status+india&sc=8-30&sk=&cvid=C891657A6F774C9C8750F178FE672423"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29",
            "Accept-Language": "en-US,en;q=0.9"
        }

        response = requests.get(url, headers=header)

        soup = BeautifulSoup(response.content, "lxml")
        # print(soup.prettify())

        seconddose = soup.find(class_="cov_leg").get_text()
        self.label_9.setText(textwrap.fill(seconddose))


class Getvaccination(QDialog):
    def __init__(self):
        super(Getvaccination, self).__init__()
        loadUi("getvaccination.ui", self)
        self.back.clicked.connect(self.directtohome)
        self.vaccinfo.clicked.connect(self.directtovaccinfo)
        self.bookvacc.clicked.connect(self.directtobookvaccine)
        self.dont.clicked.connect(self.directtodos)
        # self.cert.clicked.connect(self.directtocertificate)

    def directtohome(self):
        home2 = Homepage()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtovaccinfo(self):
        vaccination = Vaccinfo()
        widget.addWidget(vaccination)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtobookvaccine(self):
        book = Bookvaccine()
        widget.addWidget(book)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtodos(self):
        dos = Dos()
        widget.addWidget(dos)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def directtocertificate(self):
    #     certificate = Vaccinecert()
    #     widget.addWidget(certificate)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)


class Vaccinfo(QDialog):
    def __init__(self):
        super(Vaccinfo, self).__init__()
        loadUi("vaccinfo.ui", self)
        self.back.clicked.connect(self.directtogetvacc)

    def directtogetvacc(self):
        getvacc = Getvaccination()
        widget.addWidget(getvacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Bookvaccine(QDialog):
    def __init__(self):
        super(Bookvaccine, self).__init__()
        loadUi("bookvacc.ui", self)
        self.back.clicked.connect(self.directtogetvacc)

        self.search.clicked.connect(self.vaccinesearch)

    def vaccinesearch(self):
        import requests
        pincode = self.pincode.text()
        date = self.date.text()

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

        for cent in range(Total_centers):
            print()
            print(f"[{cent + 1}] Center Name:", raw_json['centers'][cent]['name'])
            print("------------------------------------------------------------")
            print("   Date      Vaccine Type    Minimum Age    Available ")
            print("  ------     -------------   ------------   ----------")
            this_session = raw_json['centers'][cent]['sessions']

            for _sess in range(0, 1):
                data = "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'],
                                                                 this_session[_sess]['vaccine'],
                                                                 this_session[_sess]['min_age_limit'],
                                                                 this_session[_sess]['available_capacity'])
                self.label_7.setText(data)

            for _sess in range(1, 2):
                data = "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'],
                                                                 this_session[_sess]['vaccine'],
                                                                 this_session[_sess]['min_age_limit'],
                                                                 this_session[_sess]['available_capacity'])
                self.label_8.setText(data)
            #
            # for _sess in range(2, 3):
            #             data = "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'],
            #                                                              this_session[_sess]['vaccine'],
            #                                                              this_session[_sess]['min_age_limit'],
            #                                                              this_session[_sess]['available_capacity'])
            #             self.label_9.setText(data)

            # for _sess in range(3, 4):
            #     data = "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'],
            #                                                      this_session[_sess]['vaccine'],
            #                                                      this_session[_sess]['min_age_limit'],
            #                                                      this_session[_sess]['available_capacity'])
            #     self.label_10.setText(data)
            #
            # for _sess in range(4, 5):
            #     data = "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'],
            #                                                      this_session[_sess]['vaccine'],
            #                                                      this_session[_sess]['min_age_limit'],
            #                                                      this_session[_sess]['available_capacity'])
            #     self.label_11.setText(data)
            #
            # for _sess in range(5, 6):
            #     data = "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'],
            #                                                      this_session[_sess]['vaccine'],
            #                                                      this_session[_sess]['min_age_limit'],
            #                                                      this_session[_sess]['available_capacity'])
            #     self.label_12.setText(data)
            #

    def directtogetvacc(self):
        getvacc = Getvaccination()
        widget.addWidget(getvacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Dos(QDialog):
    def __init__(self):
        super(Dos, self).__init__()
        loadUi("dos.ui", self)
        self.back.clicked.connect(self.directtogetvacc)

    def directtogetvacc(self):
        getvacc = Getvaccination()
        widget.addWidget(getvacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Vaccinecert(QDialog):
    def __init__(self):
        super(Vaccinecert, self).__init__()
        loadUi("vacccc.ui", self)
        self.back.clicked.connect(self.directtogetvacc)

    def directtogetvacc(self):
        getvacc = Getvaccination()
        widget.addWidget(getvacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Faq(QDialog):
    def __init__(self):
        super(Faq, self).__init__()
        loadUi("faq.ui", self)
        self.back.clicked.connect(self.directtosetting)

    def directtosetting(self):
        setting1 = Setting()
        widget.addWidget(setting1)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Changepassword(QDialog):

    def __init__(self):
        super(Changepassword, self).__init__()
        loadUi("change_password.ui", self)
        self.back.clicked.connect(self.directtosetting)
        self.submit.clicked.connect(self.directtopasschange)

    def directtosetting(self):
        setting1 = Setting()
        widget.addWidget(setting1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def directtopasschange(self):
        password = Passwordchange()
        widget.addWidget(password)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Passwordchange(QDialog):
    def __init__(self):
        super(Passwordchange, self).__init__()
        loadUi("password_changed.ui", self)
        self.back.clicked.connect(self.directtosetting)
        self.submit.clicked.connect(self.passwordchanged)

    def directtosetting(self):
        setting1 = Setting()
        widget.addWidget(setting1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def passwordchanged(self):
        password = self.password.text()
        passwordnew = self.newpassword.text()
        renewpass = self.retypepass.text()

        if len(passwordnew) == 0 or len(renewpass) == 0 or len(password) == 0:
            self.error3.setText("please enter username and password fields!")

        elif passwordnew != renewpass:
            self.error3.setText("passwords are not matching!")
        else:

            conn = sqlite3.connect("vaccination_db")
            cur = conn.cursor()

            reg_data = [passwordnew, password, renewpass]
            cur.execute(
                'UPDATE INTO signup (password) VALUES (?)',
                reg_data)

            conn.commit()
            conn.close()

            self.error3.setText("registered successfully!")


class Appoint(QDialog):
    def __init__(self):
        super(Appoint, self).__init__()
        loadUi("accountcreated.ui", self)
        self.ok.clicked.connect(self.directtohome)

    def directtohome(self):
        home2 = Homepage()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# main
app = QApplication(sys.argv)
login1 = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login1)
widget.setFixedHeight(800)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
