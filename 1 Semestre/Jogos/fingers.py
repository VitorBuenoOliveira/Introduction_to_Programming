import cv2
import mediapipe as mp
import pyautogui

# Inicializa a detecção de mãos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Função para contar e identificar os dedos levantados
def identify_fingers(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    finger_names = ["Polegar", "Indicador", "Médio", "Anelar", "Mindinho"]
    fingers_status = []
    
    # Verifica se é a mão direita ou esquerda
    is_right_hand = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
    
    # Polegar
    if is_right_hand:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            fingers_status.append((finger_names[0], True))
        else:
            fingers_status.append((finger_names[0], False))
    else:
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            fingers_status.append((finger_names[0], True))
        else:
            fingers_status.append((finger_names[0], False))
    
    # 4 Dedos
    for i in range(1, 5):
        tip = finger_tips[i]
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers_status.append((finger_names[i], True))
        else:
            fingers_status.append((finger_names[i], False))
    
    return fingers_status

# Função para detectar se todos os dedos estão abaixados
def all_fingers_down(fingers_status):
    return not any(finger[1] for finger in fingers_status)

# Captura de vídeo da câmera
cap = cv2.VideoCapture(0)

# Variável de estado para controlar a digitação
previous_one_hand_down = False
previous_two_hands_down = False
previous_right_hand_down = False
previous_left_hand_down = False

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
        right_hand_down = False
        left_hand_down = False
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_status = identify_fingers(hand_landmarks)
            
            # Verifica se a mão é a direita ou a esquerda
            is_right_hand = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
            
            if all_fingers_down(fingers_status):
                if is_right_hand:
                    right_hand_down = True
                else:
                    left_hand_down = True
        
        # Digita a letra correspondente
        if right_hand_down and not left_hand_down and not previous_right_hand_down:
            pyautogui.write('a')
            cv2.putText(frame, 'A', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            previous_right_hand_down = True
            previous_left_hand_down = False
            previous_two_hands_down = False
        elif left_hand_down and not right_hand_down and not previous_left_hand_down:
            pyautogui.write('c')
            cv2.putText(frame, 'C', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            previous_left_hand_down = True
            previous_right_hand_down = False
            previous_two_hands_down = False
        elif right_hand_down and left_hand_down and not previous_two_hands_down:
            pyautogui.write('b')
            cv2.putText(frame, 'B', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            previous_two_hands_down = True
            previous_right_hand_down = False
            previous_left_hand_down = False
        else:
            previous_right_hand_down = False
            previous_left_hand_down = False
            previous_two_hands_down = False
    
    # Exibe a imagem com as marcações
    cv2.imshow('Mão Detectada', frame)
    
    if cv2.waitKey(5) & 0xFF == 27:  # Pressiona 'ESC' para sair
        break

cap.release()
cv2.destroyAllWindows()
