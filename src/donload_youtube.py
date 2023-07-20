from pytube import YouTube


class Donload_youtube:
    def download(video_url):
        # URL do vídeo que você deseja baixar
        # video_url = "https://www.youtube.com/watch?v=SEU_CODIGO_DO_VIDEO"

        # Cria uma instância do objeto YouTube
        yt = YouTube(video_url)

        # Filtra a melhor resolução disponível
        video = yt.streams.get_highest_resolution()

        # Define o local onde o vídeo será salvo
        save_path = "/videos"

        # Baixa o vídeo para o local especificado
        video.download(output_path=save_path)

        print("Vídeo baixado com sucesso!")
