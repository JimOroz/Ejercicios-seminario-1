#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Importamos las librerias, cargamos los datos y vemos los datos
import csv
import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv('ene_mo20.csv',';')
datos.head()


# In[26]:


#Filtramos los datos para la Plaza de España y Oxido nitrógeno y hacemos la media 
finicio = '20/01/2020'
ffin= '26/01/2020'
filtro = datos[(datos['MUNICIPIO']==79) & (datos['ESTACION']==8) & (datos['MAGNITUD']==12) & ((datos['DIA'] >= 20) & (datos['DIA']<=26))]
media = filtro.groupby(['PROVINCIA', 'MUNICIPIO', 'ESTACION', 'MAGNITUD']).mean().reset_index()
media = media.filter(regex=("H.*"))


# In[27]:


#Dibujamos la gráfica
plt.title("Óxido de Nitrógeno: " + finicio + " - " + ffin)
plt.plot(media.values[0])


# In[ ]:




