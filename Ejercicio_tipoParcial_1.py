for i in (1,3):
    print("esta es la aplicacion:", i)
    resp=input("quiere iniciar el formulario? si/no")
    cont=0
    auxmen=0
    auxmed=0
    auxmay=0
    estu=0
    desem=0
    trabaj=0
    mg=0
    agepromed=0
    while resp != "no":
        age= float (input("Ingrese la edad del usuario:"))
        if age < 25 and age > 1:
            cont=cont+1
            ocup=input("Ingrese la ocupacin (estudiante, desempleado, trabajador) del usuario:")
            print("La pagina pythonizame")
            print("La pagina javaizame")
            print("La pagina rubhyizame")
            pag=input("ingrese la pagina que le gusta de las anteriores mensionadas:")
            if (age<13):
                auxmen=auxmen+1
            else:
                if age>=13 and age<=18 :
                    auxmed=auxmed+1
                else:
                    if age>=19 and age<=25 :
                        auxmay=auxmay+1

            if ocup=="estudiante" :
                estu=estu+1
            else:
                if ocup=="desempleado" :
                    desem=desem+1
                else:
                    if ocup=="trabajador" :
                        trabaj=trabaj+1        

            if pag=="pythonizame":
                mg=mg+1
                agepromed=agepromed+age
        else:
            print("no puede ingresar en este formulario por ser mayor de 25")  
        resp= float (input("quiere seguir agregando gente en el formulario? si/no"))   
    print("La cantidad de usuarios menores de edad es de:",auxmen)
    print("La cantidad de usuarios de mediana edad es de:",auxmed) 
    print("La cantidad de usuario mayores de edad es de:", auxmay)
    if (auxmen>=auxmed) and (auxmen>=auxmay):
        print("Los usuarios menores de 13 tiene mayor representatividad en la red social")

    if (auxmed>=auxmen) and (auxmed>=auxmay):
        print("Los usuarios mayores de 13 y menores de 18 tiene mayor representatividad en la red social") 

    if (auxmay>=auxmen) and (auxmay>=auxmed):
        print("Los usuarios mayores de 19 y menores de 25 tiene mayor representatividad en la red social")            

    if (auxmen==auxmed) and (auxmen==auxmay):
        print("Hay una igualdad en representatividad en la red social")

    print ("La cantidad de seguidores la pagina pythonizame es de ", mg, " y su promedio es de ",str(agepromed/mg))
    print ("la cantidad de estudiantes es de:", estu)
    print ("El porcentaje de estudiantes es de ",str((estu*100)/cont), "%") 
    print ("El porcentaje de menores de 13 es de ",str((auxmen*100)/cont), "%")
    print ("El porcentaje de mayores de 13 y menores de 18 es de ", str((auxmed*100)/cont), "%") 
    print ("El porcentaje de mayores de 19 y menores de 25 es de ", str((auxmay*100)/cont), "%")