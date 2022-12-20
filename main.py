from pytube import YouTube
import os

# Criando funções com o parâmetro "link"
def DownloadVideo(link):
    video = YouTube(link)
    try:
        # escolhe a resolução
        resolution = input("Baixa ou alta resolução? L (baixa)/ H (alta)")
        # fromata a string pra letra minúscula
        resolution = resolution.lower()
        try:
            if resolution == "l":
                video = video.streams.get_lowest_resolution()
                video.download()
            elif resolution == "h":
                video = video.streams.get_highest_resolution()
                video.download()
            else:
                print("Escolha uma opção válida")
                return
        except:
            print("Erro, algo aconteceu. Verifique seu link!")
    except:
        # caso a entry seja diferente de uma string
        print("insira um valor válido")
        return

# Donwload apenas de áudio
def DownloadAudio(link):
    audio = YouTube(link)
    try:
        # aplicando filtro para only_audio = True
        audio = audio.streams.filter(only_audio=True).first()
        # baixando arquivo.mp4
        download_file = audio.download()
        # copiando nome do arquivo.mp4
        base, saida = os.path.splitext(download_file)
    
        # colando nome do arquivo em uma variável, só que agora com extensão.mp3
        new_file = base + '.mp3'
        # renomeando arquivo.mp4 para mp3, isso força a transformação pra um arquivo de áudio
        os.rename(download_file,new_file)
    except:
        print("Erro, algo aconteceu. Verifique seu link!")
        
### parte de interação com o usuário ###
link = input("Digite o link aqui:  ")
title_video = YouTube(link)
# print do título do vídeo
print("\n",title_video.title)

try:
# joker é o nome que eu dou pra uma variável que o nome não tem importância
    joker = input("\nEsse é o seu vídeo? s/n    ")
    joker = joker.lower()
    if joker == "s":
        video_or_audio = input("Gostaria de baixar o vídeo ou apenas o Audio? V (vídeo)/A (áudio)   ")
        video_or_audio = video_or_audio.lower()
        if video_or_audio == "v":
            DownloadVideo(link)
        elif video_or_audio == "a":
            DownloadAudio(link)
        else:
            print("digite uma opção válida")
    elif joker == "n":
        print("\nVerifique se o link está correto. Caso o problema persista, contate o suporte\nContato do suporte: jhooliveira.lopes@gmail.com")
    if video_or_audio == "v":
        print("Seu vídeo foi baixado!!")
    else:
        print("Seu áudio foi baixado!")
except:
    print("Insira uma opção válida!")

