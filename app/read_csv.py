import csv
import re
import matplotlib.pyplot as plt
import charts


def read_csv(path):
  with open(path,'r')as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header = next(reader)
    #print(header)
    data=[]#Aqui se guardara una lista con los diccionarios
    for row in reader:
      iterable = zip(header,row)
      #print(list(iterable))
      country_dict={key: value for key,value in iterable}
      #print(country_dict)
      data.append(country_dict)
    return data

def get_years(dict):
  #regex = re.findall('[^2022 Population$]',año)
  new_dict = { año: poblacion for (año,poblacion) in dict.items() if re.findall('^\d\d\d\d',año)}
  #print(new_dict)
  return new_dict

def get_Percentage(data):
  percentage_dict = { item["Country/Territory"]:item["World Population Percentage"] for item in data}
  names = percentage_dict.keys()
  per = percentage_dict.values()
  return names,per

def generate_bar_chart(labels,values): 
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  #print(data) #Aqui se selecciona que numero del dicciononario sequiere
  labels,values = get_Percentage(data)
  #print(result)
  charts.generate_pie_chart(labels,values)


  #Comienza solucion primer reto
  #argentina = data[8]
  #print(argentina)
  #data2 = get_years(argentina)
  #print(data2)
  #labels=[]
  #values=[]
  #labels = data2.keys()
  #values = data2.values()
  #generate_bar_chart(labels,values)
  #Termina solucion de primer reto

  #print(data2.año)
  #print(data2.poblacion)

#opciones de solucion
#dictif
#new_dict = { año: poblacion for (año,poblacion) in data.items() if año > 50}
    #print(new_dict)

#filter
#new_list = list(filter(lambda item:item['home_team_result']=='Win',matches))

#regex
#filter
#new_list = list(filter(lambda item:item['home_team_result']=='Win',matches))
#population = re.findall('[^Population$]', text)

#new_dict = { año: poblacion for (año,poblacion) in dict.items() if año == '2022 Population'}
