import pygame
import time
import piano_lists as pl #piano_lists를 pl로
from pygame import mixer

pygame.init()
pygame.mixer.init()
#pygame.mixer.set_num_channels(50) #음향채널의 개수

fps = 60
timer = pygame.time.Clock() #시간을 track하는데 도움을 주는 객체
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #Display 가로 세로 설정값
pygame.display.set_caption('My Python Piano') #Display 이름

whites_rects = []
blacks_rects = []
white_sounds = []
black_sounds = []
white_notes = pl.white_notes
black_notes = pl.black_notes
'''
piano_notes = pl.piano_notes
black_labels = pl.black_labels
for in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav')) #흑건에 소리넣기i 
'''
def draw_piano(whites, blacks): #피아노 그리기
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i * 35, HEIGHT - 300, 35, 300], 0, 2) #백건 그리기
        whites.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2) #백건 사이 그리기

    skip_count = 0
    last_skip = 2
    skip_track = 2
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2) #흑건 그리기
        blacks.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1
    return whites, blacks
def sound_piano(whites, blacks): #피아노 소리 넣기
    for i in range(len(white_notes)):
        whites.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav')) #백건에 소리넣기
    for i in range(len(black_notes)):
        blacks.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav')) #흑건에 소리넣기
    return whites, blacks
def split_numbers(input_numbers):
    split_space_numbers = input_numbers.split()
    return [int(digit) for digit in split_space_numbers]
'''
# Play a sound
piano_sounds[0].play()
'''
run = True
while run: # main
    timer.tick(fps) #fps 이상 run할 수 없다.(milliseconds)
    screen.fill('gray') #스크린 회색
    white_keys, black_keys = draw_piano(whites_rects, blacks_rects)
    white_sounds, black_sounds = sound_piano(white_sounds, black_sounds)

    input_numbers = input("숫자 나열을 입력하세요: ")
    separated_numbers = split_numbers(input_numbers)

    for number in separated_numbers:
        if 0 <= number < len(white_sounds):
            white_sounds[number].play()    
            time.sleep(1)
        
    for event in pygame.event.get(): #queue로부터 events를 얻는다.
        if event.type == pygame.QUIT: #event가 pygame.QUIT이면 실행 종료.
            run = False


       
    pygame.display.flip() #전체적인 화면의 contents를 업데이트해준다.
pygame.quit() #실행종료.
