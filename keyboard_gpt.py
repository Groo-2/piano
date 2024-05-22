import pygame
from pygame.locals import *

# 키와 해당하는 음을 매핑한 딕셔너리
key_to_note = {
    K_a: "C",
    K_s: "D",
    K_d: "E",
    K_f: "F",
    K_g: "G",
    K_h: "A",
    K_j: "B",
}

def play_sound(note):
    # 피아노 음 파일 경로
    sound_file = f"sounds/{note}.wav"
    pygame.mixer.Sound(sound_file).play()

def main():
    pygame.init()
    pygame.mixer.init()

    # 창 크기 설정
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("피아노")

    # 이벤트 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                # 눌린 키가 음표에 해당하는지 확인하고 소리 재생
                if event.key in key_to_note:
                    play_sound(key_to_note[event.key])

    pygame.quit()

if __name__ == "__main__":
    main()