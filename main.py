meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "FR": "Intenta expresar una confirmación a lo dicho anteriormente",
     "YOLO": "Una especie de equivalente la vida es una",
  "FOMO": "Miedo a perderse o faltar a cualquier evento o situación social",
    
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

f word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
print (meme_dict [word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print ("No esta en nuestro diccionario")
