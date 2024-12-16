# def zeichne_doppelte_dreiecke(hoehe):
#     for i in range(hoehe):
#         leerzeichen = ' ' * (hoehe - i - 1)
#         sternchen = '*' * (2 * i + 1)
#         linie = leerzeichen + sternchen + leerzeichen
#         print(linie)
    
#     for i in range(hoehe - 2, -1, -1):
#         leerzeichen = ' ' * (hoehe - i - 1)
#         sternchen = '*' * (2 * i + 1)
#         linie = leerzeichen + sternchen + leerzeichen
#         print(linie)

# zeichne_doppelte_dreiecke(5)





# def triangles_bottom(hoehe):
#     for i in range(hoehe):
#         sterne_links = '*' * (i-1)
#         sterne_rechts = '*' * (i-1)
#         leer = ' ' * (2*(hoehe -i - 1))
#         linie_bottom = sterne_links + leer + sterne_rechts
#         print(linie_bottom)
# triangles_bottom(5)    




def zeichne_invertierte_dreiecke(hoehe):
    
    for i in range(hoehe):
        sternchen_links = '*' * (i + 1)
        leerzeichen = '-' * (2 * (hoehe - i - 1))
        sternchen_rechts = '*' * (i + 1)
        linie = sternchen_links + leerzeichen + sternchen_rechts
        print(linie)
    
    for i in range(hoehe - 1, 0, -1):
        sternchen_links = '*' * i
        leerzeichen = '-' * (2 * (hoehe - i))
        sternchen_rechts = '*' * i
        linie = sternchen_links + leerzeichen + sternchen_rechts
        print(linie)


zeichne_invertierte_dreiecke(5)






