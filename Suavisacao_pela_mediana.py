import cv2
imagem = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")


for i in range(0, imagem.shape[0],15):
    for j in range(0, imagem.shape[1],15):
        imagem[i:i+3, j:j+3] = (255, 255, 255)

suave = cv2.medianBlur(imagem, 5)
suave2 = cv2.medianBlur(imagem, 11)

cv2.imshow("original", imagem)
cv2.imshow("5", suave)
cv2.imshow("11", suave2)
cv2.waitKey(0)