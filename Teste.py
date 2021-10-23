import cv2

imagem = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")
cv2.imshow('imagem',imagem)
cv2.waitKey(0)



'''''#Limiarização
for i in range(0,imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        imagem[i][j] = (0,0,0)

fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'255',(15,65),fonte,2,(255,255,255),2)
cv2.putText(imagem,'70',(125,65),fonte,2,(70,70,70),2)
cv2.putText(imagem,'100',(255,65),fonte,2,(100,100,100),2)
cv2.putText(imagem,'1',(405,65),fonte,2,(1,1,1),2)
for i in range(0,imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][0] !=0:
            imagem[i][j] = (255,255,255)'''

"""#Separar canais de cores que a imagem contém
(b,g,r) =cv2.split(imagem)
cv2.imshow("Imagem ",b)
cv2.waitKey(0)"""

'''branco = (255, 255, 255)

for i in range(0,imagem.shape[0], 10): # para deixar o pixel branco pulando de 10 em 10
    for j in range(0, imagem.shape[1],5):
        imagem [i] [j] = branco

for i in range(0,imagem.shape[0], 10): # para deixar o pixel branco pulando de 10 em 10
    for j in range(0, imagem.shape[1],10):
        imagem [i:i+5, j:j+5] = branco'''

"""for i in range(0,imagem.shape[0]): # para mudar pixel na cor azul em branco
    for j in range(0, imagem.shape[1]):
        if imagem [i] [j] [0]== 255:
            imagem [i][j] = branco"""

# ESCREVENDO NA IMAGEM
"""fonte = cv2.FONT_HERSHEY_COMPLEX       # ESCOLHENDO FONTE
cv2.putText(imagem,"Jacson",(50,50), fonte, 2, (255,255,255),2, cv2.LINE_AA)"""

#RECORTAR IMAGEM
"""imagemRecortada = imagem[100:400, 100:300]
cv2.imshow("ImagemRecortada", imagemRecortada)"""

# diminuindo/aumentando a figura
"""larguraNova = 100
alturaNova = 100
imagem = cv2.resize(imagem,(larguraNova,alturaNova)) #usando resize para diminuir/aumenta a figura"""

#mexendo no tamanho da figura na mesma proporção
"""largura = imagem.shape[1]
altura = imagem.shape[0]
proporcao=float(altura/largura)
larguraNova = 150
alturaNova = int(larguraNova*proporcao)"""

#Rotacionada no Y
"""imagemRotacionada = imagem[:, ::-1]
cv2.imshow("Imagem Rotacioanda", imagemRotacionada)"""

"""#Rotacionada no X
imagemRotacionada = imagem[::-1, :]
cv2.imshow("Imagem Rotacioanda", imagemRotacionada)"""

#Criando histograma


"""imagem[0:10][0:10] = (255,255,255) #alterando a cor do pixel para branco"""
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)



"""for i in range(0 , imagem.shape[0]):
    for j in range(0,imagem.shape[1]):
        for h in range(0, 3):
            print(imagem[i][j][h])
"""