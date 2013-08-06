'''
Author: Omar Andres Zapata Mesa
Grupo de Fenomenologia de Interacciones Fundamentales Gfif
AUG 2013

@package PyB3
'''

from sys import exit

B3GpioPath='/sys/class/gpio/'
B3OffsetBase=32

class B3Export:
  ''' Class to export 
  '''
  def __init__(self):
    self.__ExportFile=open(B3GpioPath+'/export','w');
  def __del__(self):
    if not self.__ExportFile.closed :
      self.__ExportFile.close()
  def Export(self,pin):
    ''' pin is a B3Pin's object
    '''
    if not self.__ExportFile.closed:
      self.__ExportFile.write(str(pin.register))
    else:
      print "Error: Gpio's export file is not open"
      print "Msg: Gpio="+pin.gpio+" Num="+pin.num+"can not be exported"
      exit(1)


class B3Unexport:
  ''' Class to export 
  '''
  def __init__(self):
    self.__UnexportFile=open(B3GpioPath+'/unexport','w');
  def __del__(self):
    if not self.__UnexportFile.closed :
      self.__UnexportFile.close()
  def Unexport(self,pin):
    ''' pin is a B3Pin's object
    '''
    if not self.__ExportFile.closed:
      self.__ExportFile.write(str(pin.register))
    else:
      print "Error: Gpio's unexport file is not open"
      print "Msg: Gpio="+pin.gpio+" Num="+pin.num+"can not be unexported"
      exit(1)


B3Exporter=B3Export();
B3Unexporter=B3Unexport();

class B3Pin:
  def __init__(self,gpio,num):
    '''gpio takes values 0,1,2 
       num  takes values [0,31] 
    '''
    self.gpio=gpio
    self.num=num
    self.offset=(gpio*B3OffsetBase)
    self.register=(gpio*B3OffsetBase)+num
    B3Exporter.Export(self)
    self.__direction=open(B3GpioPath+'gpio'+str(self.register)+'/direction','w')
  def __del__(self):
    B3Unexporter.Unexport(self)
    self.__direction.close()
  def SetReadMode(self):
    self.__direction.write("in")
    
  def SetWriteMode(self):
    self.__direction.write("out")

    
B3Pins={}
for i in range(3):
  for j in range(32):
    B3Pins["pgio"+str(i)]=B3Pin(i,j)
    

