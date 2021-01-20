from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import requests
from io import BytesIO
from time import sleep 

 
while True:

    id = input("[*] Digite el ID del usuario para mostrar la nube de palabras: ")
    
    
    if id.isdigit () != True:
        print ("\n\nDato no valido.")
    else:
        url = 'https://es.stackoverflow.com/users/' + id + "/?tab=tags"
        page = requests.get (url)   # requests chequea que el url funciona



    soup = BeautifulSoup (page.content, "html.parser") # BeautifulSoup analiza el htlm
    lbls = soup.find_all ('a', class_='post-tag') # lbls = etiquetas de usuario
    labels = list ()


    for i in lbls:
        labels.append(i.text)
  
    c = None #Verificara si el usurio cuenta con tags 
    msj = ""

    for i in labels:
        if i != None:
            c = True    
            break

    #unique_string=(" ").join(labels)
    if c == True:

        url = "https://media.istockphoto.com/photos/monarch-butterfly-in-rainbow-colors-isolated-on-white-picture-id1196565484?k=6&m=1196565484&s=170667a&w=0&h=-H8O0dSlwlyFWvzRK1RR5VDV4fZo63dNoWXveFMm7JE="
        
        unique_string = (" ").join (labels)
        response = requests.get (url)
        creation = np.asarray (Image.open (BytesIO (response.content)))  #np transforma la imagen en un array
        wordcloud = WordCloud (background_color = "black", mask=creation, contour_width = 0, regexp=r"\S[\S']+").generate (unique_string)
        colors = ImageColorGenerator (creation)
        wordcloud.recolor (color_func = colors)
        plt.figure (figsize = (15, 8))
        plt.imshow (wordcloud)
        plt.axis ("off")
        plt.show ()
        plt.close ()

    else:
        print("Este usuario no posee tags que mostrar")

    msj = input("\nDesea acabar la ejecución si/no: ")
    msj.lower() #En caso de que escriba en mayuscula esta la transformara en minuscula

    if msj == "si":
        break
        print("\n")



