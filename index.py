import os
import cv2
import numpy as np
import shutil


logo = cv2.imread('Logo_tirar.png', 0)


if logo is None:
    print("A imagem da logo não foi encontrada.")
    exit(1)


fotos = os.listdir()

for i in fotos:
    nome, extensao = os.path.splitext(i)
    if extensao == "" or extensao == ".ipynb" or nome == "Logo_tirar":
        continue  

    imagem = cv2.imread(i, 0)

    if imagem is None:
        print(f"Não foi possível abrir a imagem {i}.")
        continue  

   
    altura, largura = imagem.shape
    margem =20   
    roi = imagem[altura - logo.shape[0] - margem:, :logo.shape[1] + margem]

    
    correspondencia = cv2.matchTemplate(roi, logo, cv2.TM_CCOEFF_NORMED)

    
    limite_correspondencia = 0.1
    if np.max(correspondencia) >= limite_correspondencia:
        os.makedirs('Fotos com logo',exist_ok=True)
        origem1=os.getcwd() + "\\" +"Fotos com logo"
        arquivo_origem = os.getcwd() + "\\" + i
        destino=origem1
        shutil.move(arquivo_origem,destino)
        print(f"Logo encontrada em {i}")
        print(arquivo_origem)
    else:
        print(f'Logo não encontrada em {i}')