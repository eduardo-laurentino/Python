"""Reverte video espelhado pela câmera frontal"""
import cv2

def espelhar_video(input_file, output_file):
    # Abrir o vídeo
    cap = cv2.VideoCapture(input_file)

    # Obter propriedades do primeiro frame
    ret, first_frame = cap.read()
    if not ret:
        print("Erro ao ler o primeiro frame.")
        return

    height, width, _ = first_frame.shape
    print(height, width)

    # Criar objeto VideoWriter para salvar o vídeo espelhado
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    # Reiniciar a leitura do vídeo
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Loop através de cada frame do vídeo
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Espelhar o frame horizontalmente
        frame = cv2.flip(frame, 4)

        # Escrever o frame no arquivo de saída
        out.write(frame)

        cv2.imshow('Video Espelhado', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar os recursos
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Substitua 'video_camera_frontal.mp4' pelo nome do arquivo de entrada e 'video_espelhado.mp4' pelo nome do arquivo de saída
espelhar_video('video.mp4', 'video_espelhado.mp4')