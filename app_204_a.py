# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:33:10 2022

@author: jahop_fz60h0
"""

import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import plotly.express as px

import pandas as pd
#import numpy as np

#import plotly.graph_objects as go 


from PIL import Image

image = Image.open('pemex.png')
st.image(image)


    
st.title("Modelado de SiStemas Petroleros")
page_names = ['Ángel Moras Conde', 'Antonio Pérez Rocha', 'Armando Nava Cedillo', 'Ciro Díaz Salgado', 'Diana Roberta Tapia Juárez', 'Eduardo Fuentes Resendiz', 'Ienisei Peña Díaz', 'Lazaro Ignacio Rodríguez Arvizu', 'Lilia Ines Sanchez Vargas', 'Maribel Ramírez Bárcenas', 'Mireya Osorio Rosales', 'Pedro Peña Sánchez', 'Ricardo Padilla Bastida', 'Rodrigo Maldonado Villalón', 'Unión de los gráficos']

page = st.radio('Navegación', page_names, index = 0)
#st.write("**La variable 'page' returns:**", page)

df = pd.read_excel("NDR_PC-2.xlsx")
st.title("Datos")
st.write(df)

#1                    
if page == 'Ángel Moras Conde':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,3,3,2,2,3,2,3,2,4,3,4,3,3,3,2,3,3,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ángel Moras Conde', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
   
#2                
if page == 'Antonio Pérez Rocha':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,3,2,2,2,2,2,4,5,4,2,3,3,2,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Antonio Pérez Rocha', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#3                    
if page == 'Armando Nava Cedillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,2,2,2,2,1,2,4,4,4,2,2,4,2,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Armando Nava Cedillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#4                   
if page == 'Ciro Díaz Salgado':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,3,2,3,4,2,3,5,4,3,2,3,4,3,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ciro Díaz Salgado', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#5                   
if page == 'Diana Roberta Tapia Juárez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,1,2,3,3,2,2,2,2,2,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Diana Roberta Tapia Juárez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#6                   
if page == 'Eduardo Fuentes Resendiz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,2,1,1,2,2,1,4,3,3,2,2,3,2,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Eduardo Fuentes Resendiz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#7                   
if page == 'Ienisei Peña Díaz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,1,1,1,1,1,1,3,3,2,2,2,1,2,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ienisei Peña Díaz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#8                   
if page == 'Lazaro Ignacio Rodríguez Arvizu':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,4,3,4,3,3,3,3,4,5,3,3,3,4,3,3,2,3,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lazaro Ignacio Rodríguez Arvizu', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#9             
if page == 'Lilia Ines Sanchez Vargas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,3,3,2,3,2,2,2,1,4,3,3,1,3,4,3,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lilia Ines Sanchez Vargas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#10                    
if page == 'Maribel Ramírez Bárcenas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,1,2,3,3,3,1,3,3,4,1,3,2,2,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maribel Ramírez Bárcenas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#11                
if page == 'Mireya Osorio Rosales':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,1,5,3,2,2,3,3,2,1,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Mireya Osorio Rosales', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#12                   
if page == 'Pedro Peña Sánchez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,2,1,2,3,2,2,3,4,3,4,2,3,3,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Pedro Peña Sánchez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#13             
if page == 'Ricardo Padilla Bastida':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,2,2,3,3,3,3,2,2,4,3,2,2,3,3,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ricardo Padilla Bastida', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#14                    
if page == 'Rodrigo Maldonado Villalón':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,1,2,2,2,1,1,5,5,5,2,2,5,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Rodrigo Maldonado Villalón', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
#############################################################################################################################################################




    
if page == 'Unión de los gráficos':
     fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,1,3,3,3,3,4,3,4,2,3,3,2,2,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
     #1                    
     fig.add_scatter(name = 'Ángel Moras Conde', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,3,3,2,2,3,2,3,2,4,3,4,3,3,3,2,3,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #2                
     fig.add_scatter(name = 'Antonio Pérez Rocha', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,3,2,2,2,2,2,4,5,4,2,3,3,2,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #3                    
     fig.add_scatter(name = 'Armando Nava Cedillo', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,2,2,2,2,1,2,4,4,4,2,2,4,2,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
     #4                   
     fig.add_scatter(name = 'Ciro Díaz Salgado', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,3,2,3,4,2,3,5,4,3,2,3,4,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #5                   
     fig.add_scatter(name = 'Diana Roberta Tapia Juárez', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,1,2,3,3,2,2,2,2,2,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #6                   
     fig.add_scatter(name = 'Eduardo Fuentes Resendiz', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,2,1,1,2,2,1,4,3,3,2,2,3,2,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
     #7                   
     fig.add_scatter(name = 'Ienisei Peña Díaz', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,1,1,1,1,1,1,3,3,2,2,2,1,2,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #8                   
     fig.add_scatter(name = 'Lazaro Ignacio Rodríguez Arvizu', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,4,3,4,3,3,3,3,4,5,3,3,3,4,3,3,2,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #9             
     fig.add_scatter(name = 'Lilia Ines Sanchez Vargas', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,3,3,2,3,2,2,2,1,4,3,3,1,3,4,3,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #10                    
     fig.add_scatter(name = 'Maribel Ramírez Bárcenas', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,1,2,3,3,3,1,3,3,4,1,3,2,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #11                
     fig.add_scatter(name = 'Mireya Osorio Rosales', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,1,5,3,2,2,3,3,2,1,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #12                   
     fig.add_scatter(name = 'Pedro Peña Sánchez', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,2,1,2,3,2,2,3,4,3,4,2,3,3,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #13             
     fig.add_scatter(name = 'Ricardo Padilla Bastida', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,2,2,3,3,3,3,2,2,4,3,2,2,3,3,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #14                    
     fig.add_scatter(name = 'Rodrigo Maldonado Villalón', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[1,1,1,1,2,2,2,1,1,5,5,5,2,2,5,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
     st.plotly_chart(fig)
        
else:   
     st.subheader("")
        
          





    
