# MadLibsGame 
# Loop back to this point once code finishes
loop = 1

while (loop < 3):

    # All the questions that the program asks the user
    noun = input("Ingrese un sustantivo: ")
    p_noun = input("Ingrese un sustantivo plural: ")
    noun2 = input("Ingrese otro sustantivo: ")
    place = input("Ingrese un lugar: ")
    adjective = input("Ingrese un adjetivo (Palabra descriptiva): ")
    noun3 = input("Ingrese otro sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Se amable con tu ",noun," perrito porque es ", p_noun)
    print ("Para un perrito el mundo es ", noun2,",")
    print ("Cuida la naturaleza ",p_noun," que hay en ",place)
    print ("El tiempo en Tijuana es siempre muy ",adjective,".")
    print ()
    print ("Puedes soñar con ",noun3,",")
    print ("es bastante bonito.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1