import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")
listaAzul = []
listaVerde = []
listaVermelho = []
resultadoAzul = []
resultadoVerde = []
resultadoVermelho = []

cv2.imshow("janela", imagem)
cv2.waitKey(0)

for i in range (0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        listaAzul.append(imagem[i][j][0])
        listaVerde.append(imagem[i][j][1])
        listaVermelho.append(imagem[i][j][2])




listaSemAzul = sorted(set(listaAzul))

for i in range(0,len(listaSemAzul)):
    somatoria = 0
    for j in range (0,len(listaAzul)):
        if listaSemAzul[i]==listaAzul[j]:
            somatoria+=1
    resultadoAzul.append(somatoria)

#-----------------------------------------

listaSemVerde = sorted(set(listaVerde))

for i in range(0,len(listaSemVerde)):
    somatoria = 0
    for j in range (0,len(listaVerde)):
        if listaSemVerde[i]==listaVerde[j]:
            somatoria+=1
    resultadoVerde.append(somatoria)


#-----------------------------------------

listaSemVermelho = sorted(set(listaVermelho))

for i in range(0,len(listaSemVerde)):
    somatoria = 0
    for j in range (0,len(listaVermelho)):
        if listaSemVermelho[i]==listaVermelho[j]:
            somatoria+=1
    resultadoVermelho.append(somatoria)

plt.plot(resultadoVermelho, color='red')
plt.plot(resultadoVerde, color='green')
plt.plot(resultadoAzul, color='blue')
plt.show()