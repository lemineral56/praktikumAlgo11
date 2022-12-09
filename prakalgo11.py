#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:18:36 2022

@author: rhenatabella
"""

class student():
    "Program data Mahasiswa"
    empCount = 0
    
    def init(self, name ,nim, year):
        self.name = name
        self.nim = nim
        self.year = year
        
    def displayInput(self):
        self.name = input("Nama : ")
        self.nim = input("NIM : ")
        self.year = input("Angkatan : ")
        student.empCount += 1
        
    def displayCount(self):
        print("Total Mahasiswa %d" % student.empCount)
        
    def displayStudent(self):
        print ("Biodata Anda :")
        print ("Nama : ", self.name)
        print ("NIM : ", self.nim)
        print ("Angkatan : ", self.year)
    
        
dataStd = student()
dataStd.displayInput()
dataStd.displayStudent()
print("Total Mahasiswa %d" % student.empCount)
