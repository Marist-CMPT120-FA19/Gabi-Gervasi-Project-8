#Gabi Gervasi
#Gabrielle.Gervasi1@marist.edu
#average daily temperatures and computes the running total of cooling and heating days


def isAveT(aveT):
  if int(aveT)<60 or aveT>80:
    return  True
  else:
    return False
  
 
def line():
  print(50*"=")


def degreeDays(aveT):
  coolingDegreeDays = 0
  heatingDegreeDays = 0
  for i in range(len(aveT)):
    
      if aveT[i]>80:
        heatingDegreeDays = heatingDegreeDays + (aveT[i]-80)
      if aveT[i]<60:
        coolingDegreeDays = coolingDegreeDays + (60-aveT[i])
        
  return coolingDegreeDays , heatingDegreeDays

  
def intro():
  print("This program accepts a sequence of average daily")
  print("temperatures and computes the running total of")
  print("cooling and heating degree-days.")



def strToList(aveT):
  aveTList = []
  for num in aveT.split():
    num = int(num)
    aveTList.append(num)
  aveT = aveTList
  return aveT


def main():
  
  intro()
  
  aveT = input("Enter temperatures:")
  line()
  
  aveT = strToList(aveT)
  
  coolingDegreeDays, heatingDegreeDays = degreeDays(aveT)
  
  print("Cooling Degree Days: ", heatingDegreeDays)
  print("Heating Degree Days: ", coolingDegreeDays)
  line() 

main()
