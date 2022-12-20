from pytube import YouTube

# Criando funções com o parâmetro "link"
def Download(link):
    video = YouTube(link)

    # escolhe a resolução
    resolution = input("Qual baixa ou alta resolução? L (baixa)/ H (alta)")
    # fromata a string pra letra minúscula
    resolution = resolution.lower()
    if resolution == "l":
        video = video.streams.get_lowest_resolution()
    elif resolution == "h":
        video = video.streams.get_highest_resolution()
    else:
        print("Escolha uma opção válida")
        return

### parte 
link = input("Digite o link aqui:  ")
Download(link)