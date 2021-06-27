# Importações
import pygame
import sys
import main
from pygame.locals import *



def gamequiz():
    # Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Aprendendo a Ler')
    pygame.mixer.init()

    # Audios
    audio_clique = pygame.mixer.Sound('educacional/audios/quiz/clique.ogg')

    # Cores
    preto = (0, 0, 0)

    # Imagens
    b1 = pygame.image.load('educacional/imagens/quiz/nuvem.png')
    fundo = pygame.image.load('educacional/imagens/quiz/fundo.jpeg')
    voltar = pygame.image.load('educacional/imagens/quiz/voltar.png')

    # Textos
    pygame.font.init()
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte11 = pygame.font.SysFont('Arial Black', 35)
    fonte2 = pygame.font.SysFont('Arial', 20)
    menu = fonte2.render('Menu Principal', 1, preto)
    portugues = fonte11.render('Vamos lá', 1, preto)


    # Tela inicial
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 50 and y > 10 and y < 50:
                        audio_clique.play()
                        main.telajogos()
                    if x > 35 and x < 355 and y > 260 and y < 430:
                        audio_clique.play()
                        inicio2('Aprender')

                    if x > 725 and x < 830 and y > 570 and y < 590:
                        audio_clique.play()
                        main.principal()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1, (100, 260))
        b1.blit(portugues, (45, 45))
        tela.blit(menu, (725, 570))
        pygame.display.update()


def placar(quantidade, disciplina):
    # Inicialização
    tela = pygame.display.set_mode((850, 600))
    pygame.mixer.init()

    # Audios
    audio_efeito = pygame.mixer.Sound('educacional/audios/quiz/efeito.ogg')
    audio_placar = pygame.mixer.Sound('educacional/audios/quiz/bateria.ogg')
    audio_perdeu = pygame.mixer.Sound('educacional/audios/quiz/errada.ogg')

    # Imagens
    quant0 = pygame.image.load('educacional/imagens/quiz/zerou.jpg')
    quant1 = pygame.image.load('educacional/imagens/quiz/dez.jpg')
    quant2 = pygame.image.load('educacional/imagens/quiz/vinte.jpg')
    quant3 = pygame.image.load('educacional/imagens/quiz/trinta.jpg')
    quant4 = pygame.image.load('educacional/imagens/quiz/quarenta.jpg')
    quant5 = pygame.image.load('educacional/imagens/quiz/cinquenta.jpg')
    quant6 = pygame.image.load('educacional/imagens/quiz/sessenta.jpg')
    quant7 = pygame.image.load('educacional/imagens/quiz/setenta.jpg')
    quant8 = pygame.image.load('educacional/imagens/quiz/oitenta.jpg')
    quant9 = pygame.image.load('educacional/imagens/quiz/noventa.jpg')
    quant10 = pygame.image.load('educacional/imagens/quiz/cem.jpg')
    if quantidade == 0:
        tela.blit(quant0, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)

    if quantidade == 1:
        tela.blit(quant1, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 2:
        tela.blit(quant2, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 3:
        tela.blit(quant3, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 4:
        tela.blit(quant4, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 5:
        tela.blit(quant5, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 6:
        tela.blit(quant6, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 7:
        tela.blit(quant7, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 8:
        tela.blit(quant8, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 9:
        tela.blit(quant9, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)
    if quantidade == 10:
        tela.blit(quant10, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair = True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair = False
        inicio2(disciplina)


def inicio2(disciplina):
    # Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Aprender/{}'.format(disciplina))
    pygame.mixer.init()

    # Audios
    audio_clique = pygame.mixer.Sound('educacional/audios/quiz/clique.ogg')

    # Cores
    preto = (0, 0, 0)

    # Imagens
    b1 = pygame.image.load('educacional/imagens/quiz/nuvem.png')
    b2 = pygame.image.load('educacional/imagens/quiz/nuvem.png')
    fundo = pygame.image.load('educacional/imagens/quiz/fundo.jpeg')
    voltar = pygame.image.load('educacional/imagens/quiz/voltar.png')

    # Textos
    pygame.font.init()
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte2 = pygame.font.SysFont('Arial', 20)
    facil = fonte1.render('Entrar', 1, preto)
    ajuda = fonte1.render('Ajuda', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)

    # Tela inicial
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 50 and y > 10 and y < 50:
                        audio_clique.play()
                        gamequiz()
                    if x > 725 and x < 830 and y > 570 and y < 590:
                        audio_clique.play()
                        main.principal()
                    if x > 100 and x < 370 and y > 235 and y < 385:
                        audio_clique.play()
                        # Inicialização
                        pygame.display.set_caption('Aprender/{}/Entrar'.format(disciplina))
                        pygame.mixer.init()

                        # Audios
                        audio_clique = pygame.mixer.Sound('educacional/audios/quiz/clique.ogg')
                        audio_efeito = pygame.mixer.Sound('educacional/audios/quiz/efeito.ogg')
                        audio_ganhou = pygame.mixer.Sound('educacional/audios/quiz/certa.ogg')
                        audio_perdeu = pygame.mixer.Sound('educacional/audios/quiz/errada.ogg')
                        # Imagens
                        acertou = pygame.image.load('educacional/imagens/quiz/acertou.jpeg')
                        errou = pygame.image.load('educacional/imagens/quiz/errou.jpeg')
                        # Imagens de Português
                        pp1 = pygame.image.load('educacional/imagens/quiz/pergunta1.jpg')
                        pp2 = pygame.image.load('educacional/imagens/quiz/pergunta2.jpg')
                        pp3 = pygame.image.load('educacional/imagens/quiz/pergunta3.jpg')
                        pp4 = pygame.image.load('educacional/imagens/quiz/pergunta4.jpg')
                        pp5 = pygame.image.load('educacional/imagens/quiz/pergunta5.jpg')
                        pp6 = pygame.image.load('educacional/imagens/quiz/pergunta6.jpg')
                        pp7 = pygame.image.load('educacional/imagens/quiz/pergunta7.jpg')
                        pp8 = pygame.image.load('educacional/imagens/quiz/pergunta8.jpg')
                        pp9 = pygame.image.load('educacional/imagens/quiz/pergunta9.jpg')
                        pp10 = pygame.image.load('educacional/imagens/quiz/pergunta10.jpg')


                        # Textos
                        pygame.font.init()
                        fonte = pygame.font.SysFont('Arial', 20)
                        menu = fonte.render('Menu Principal', 1, preto)

                        # Jogo
                        if disciplina == "Aprender":
                            # 1° Questão
                            tela.blit(pp1, (0, 0))
                            pygame.display.update()
                            cont = 0
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 2° Questão
                            tela.blit(pp2, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 3° Questão
                            tela.blit(pp3, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 4° Questão
                            tela.blit(pp4, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 5° Questão
                            tela.blit(pp5, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 6° Questão
                            tela.blit(pp6, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 7° Questão
                            tela.blit(pp7, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 8° Questão
                            tela.blit(pp8, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 9° Questão
                            tela.blit(pp9, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            # 10° Questão
                            tela.blit(pp10, (0, 0))
                            pygame.display.update()
                            sair = True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont += 1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair = False
                            placar(cont, disciplina)

                    if x > 430 and x < 700 and y > 235 and y < 385:
                        audio_clique.play()
                        # Inicialização
                        pygame.display.set_caption('Aprender/{}/Ajuda'.format(disciplina))
                        # Imagens
                        ajuda = pygame.image.load('educacional/imagens/quiz/ajuda.jpg')
                        # Tela inicial
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if pygame.mouse.get_pressed()[0]:
                                        x = pygame.mouse.get_pos()[0]
                                        y = pygame.mouse.get_pos()[1]
                                        if x > 10 and x < 50 and y > 10 and y < 50:
                                            audio_clique.play()
                                            inicio2(disciplina)
                                        if x > 725 and x < 830 and y > 570 and y < 590:
                                            audio_clique.play()
                                            main.principal()
                            pygame.time.Clock().tick(30)
                            tela.blit(ajuda, (0, 0))
                            tela.blit(voltar, (10, 10))
                            tela.blit(menu, (725, 570))
                            pygame.display.update()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(b1, (100, 235))
        b1.blit(facil, (100, 35))
        tela.blit(b2, (430, 235))
        b2.blit(ajuda, (93, 35))
        tela.blit(menu, (725, 570))
        tela.blit(voltar, (10, 10))
        pygame.display.update()
