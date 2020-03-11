#!/usr/bin/env python


import sys
if _name_ == "_main_":
      if len(sys.argv) > 3:
          print ("erreur,")

      elif len (sys.argv) == 3:
          x = int(sys.argv[1])
          y = int(sys.argv[2])
          print ("somme = ", x+y)

      else:
          print("deux argument svp")
          x = int(sys.argv[1])
          y = int (input("y= ")
          print ("somme = ", x+y)


