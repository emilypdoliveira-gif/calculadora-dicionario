#funcoes com *args-calculadora flexivel

def estatisticas(*numeros):
    total=sum (numeros)
    media=total/len(numeros)
    maximo=max(numeros)
    minimo=min(numeros)
    print(f"Total :{total} | Media {media:.2f} | Max:{maximo} | Min {minimo}")
estatisticas(10,20,30)
estatisticas (59,68,80,90)
estatisticas (20,30,67,34)

#listas
lista=(90,50,60)
estatisticas(*lista)

[]
()