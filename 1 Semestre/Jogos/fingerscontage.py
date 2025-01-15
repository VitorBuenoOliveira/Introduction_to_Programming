import cv2
import mediapipe as mp

# Inicializa a detecção de mãos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Função para contar os dedos levantados
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    fingers = []
    
    # Verifica se é a mão direita ou esquerda
    is_right_hand = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
    
    # Thumb
    if is_right_hand:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
    else:
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
    
    # 4 Fingers
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    return fingers.count(1)

# Captura de vídeo da câmera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Converte a imagem BGR para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Processa a imagem para encontrar as mãos
    results = hands.process(frame_rgb)
    
    # Desenha as marcações das mãos na imagem original
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_up = count_fingers(hand_landmarks)
            cv2.putText(frame, f'Dedos: {fingers_up}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    # Exibe a imagem com as marcações
    cv2.imshow('Mão Detectada', frame)
    
    if cv2.waitKey(5) & 0xFF == 27:  # Pressiona 'ESC' para sair
        break

cap.release()
cv2.destroyAllWindows()
