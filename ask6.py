# -*- coding: utf-8 -*-
#Άσκηση 6

#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει σαν είσοδο από το χρήστη μήνα
#και χρόνο και εμφανίζει το ημερολόγιο εκείνου του μήνα στη μορφή:
#January 2018
#S\tM\tT\tW\tT\tF\tS
#\t01\t02\t03...



#χρειαζόμαστε την κατάλληλη βιβλιοθήκη
import calendar

#Ερώτηση προς τον χρήστη
i = 2
while i > 1:
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))
    print(calendar.month(yy, mm))
