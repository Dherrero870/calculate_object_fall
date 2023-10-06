# pregunta el nombre 
Nombre = (input("¡Hola! ¿Cómo te llamas?:"))
# pregunta edad 
Edad = float (input(f"¡Ah! {Nombre}. Que nombre más bonito. ¿Cuántos años tienes?:"))
if Edad>= 65: 
    print ("Tendrás experiencia en la vida entonces")
else:
    print ("Muy jóven todavía")
# pregunta donde vives
Ciudad = input (f"{Edad}.Bueno, estás en la flor de la vida. ¿Dónde vives?:")
# pregunta cuales son sus hobbies 
Hobbies = input(f"¨{Ciudad}, que bonito ¿Y cuál es tu hobby?:")
# frase completa. pregunta si no
Decision = input (f"¿Conoces algún sitio donde poder {Hobbies} en {Ciudad}?: (si/no)")
if Decision == "si": 
    print ("Genial. Ya me dirás donde.Un placer conocerte. Hasta luego")
else: 
    print ("Vaya. Un placer conocerte. Hasta luego")
