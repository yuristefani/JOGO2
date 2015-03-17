from random import randint #spock 1    tesoura 2    papel 3    pedra 4    lagarto 5
tipo=int(input("1 para melhor de tres, 2 para jogador vs jogador, 3 para rodadas ilimitadas: "))
pcvit=0
usvit=0
if tipo==1:
    pcvit=0
    usvit=0
    while (pcvit!=3 and usvit!=3):
        usesc=int(input("faça a sua escolha (1 para Spock, 2 para tesoura, 3 para papel, 4 para pedra e 5 para lagarto), aprendiz: "))
        pcesc=randint(1,5)
        if pcesc == 1:
            if usesc ==1:
                print("empate!")
            elif usesc ==2:
                pcvit+=1
                print("Spock esmaga tesoura!")
            elif usesc==3:
                usvit+=1
                print("Papel refuta Spock!")
            elif usesc==4:
                pcvit+=1
                print("Spock vaporiza pedra!")
            elif usesc==5:
                usvit+=1
                print("Lagarto envenena Spock!")
        
        if pcesc == 2:
            if usesc ==1:
                usvit+=1
                print("Spock esmaga tesoura!")
            elif usesc ==2:
                print("empate!")
            elif usesc==3:
                pcvit+=1
                print("Tesoura corta papel!")
            elif usesc==4:
                usvit+=1
                print("Pedra quebra tesoura!")
            elif usesc==5:
                pcvit+=1
                print("Tesoura decapita lagarto!")
        
        if pcesc == 3:
            if usesc ==1:
                pcvit+=1
                print("Papel refuta Spock!")
            elif usesc ==2:
                usvit+=1
                print("Tesoura corta papel!")
            elif usesc==3:
                print("empate!")
            elif usesc==4:
                pcvit+=1
                print("Papel cobre pedra!")
            elif usesc==5:
                usvit+=1
                print("Lagarto come papel!")
        
        if pcesc == 4:
            if usesc ==1:
                usvit+=1
                print("Spock vaporiza pedra!")
            elif usesc ==2:
                pcvit+=1
                print("Pedra quebra tesoura!")
            elif usesc==3:
                usvit+=1
                print("Papel cobre pedra!")
            elif usesc==4:
                print("empate!")
            elif usesc==5:
                pcvit+=1
                print("Pedra esmaga lagarto!")
        
        if pcesc == 5:
            if usesc ==1:
                pcvit+=1
                print("Lagarto envenena Spock!")
            elif usesc ==2:
                usvit+=1
                print("Tesoura decapita lagarto!")
            elif usesc==3:
                pcvit+=1
                print("Lagarto come papel!")
            elif usesc==4:
                usvit+=1
                print("Pedra esmaga lagarto!")
            elif usesc==5:
                print("empate!")
        print("voce tem %d" %usvit , "pontos")
        print("computador tem %d" %pcvit , "pontos")
                
    if usvit>pcvit:
        print("Voce ganhou")
    if usvit<pcvit:
        print("Voce perdeu")
if tipo==2:
    pcvit=0
    usvit=0
    while (pcvit!=3 and usvit!=3):
        usesc=int(input("faça a sua escolha (1 para Spock, 2 para tesoura, 3 para papel, 4 para pedra e 5 para lagarto), Jogador 1: "))
        pcesc=int(input("faça a sua escolha (1 para Spock, 2 para tesoura, 3 para papel, 4 para pedra e 5 para lagarto), Jogador 2: "))
        if pcesc == 1:
            if usesc ==1:
                print("empate!")
            elif usesc ==2:
                pcvit+=1
                print("Spock esmaga tesoura!")
            elif usesc==3:
                usvit+=1
                print("Papel refuta Spock!")
            elif usesc==4:
                pcvit+=1
                print("Spock vaporiza pedra!")
            elif usesc==5:
                usvit+=1
                print("Lagarto envenena Spock!")
        
        if pcesc == 2:
            if usesc ==1:
                usvit+=1
                print("Spock esmaga tesoura!")
            elif usesc ==2:
                print("empate!")
            elif usesc==3:
                pcvit+=1
                print("Tesoura corta papel!")
            elif usesc==4:
                usvit+=1
                print("Pedra quebra tesoura!")
            elif usesc==5:
                pcvit+=1
                print("Tesoura decapita lagarto!")
        
        if pcesc == 3:
            if usesc ==1:
                pcvit+=1
                print("Papel refuta Spock!")
            elif usesc ==2:
                usvit+=1
                print("Tesoura corta papel!")
            elif usesc==3:
                print("empate!")
            elif usesc==4:
                pcvit+=1
                print("Papel cobre pedra!")
            elif usesc==5:
                usvit+=1
                print("Lagarto come papel!")
        
        if pcesc == 4:
            if usesc ==1:
                usvit+=1
                print("Spock vaporiza pedra!")
            elif usesc ==2:
                pcvit+=1
                print("Pedra quebra tesoura!")
            elif usesc==3:
                usvit+=1
                print("Papel cobre pedra!")
            elif usesc==4:
                print("empate!")
            elif usesc==5:
                pcvit+=1
                print("Pedra esmaga lagarto!")
        
        if pcesc == 5:
            if usesc ==1:
                pcvit+=1
                print("Lagarto envenena Spock!")
            elif usesc ==2:
                usvit+=1
                print("Tesoura decapita lagarto!")
            elif usesc==3:
                pcvit+=1
                print("Lagarto come papel!")
            elif usesc==4:
                usvit+=1
                print("Pedra esmaga lagarto!")
            elif usesc==5:
                print("empate!")
                
    if usvit>pcvit:
        print("Jogador 1 ganhou")
    if usvit<pcvit:
        print("Jogador 2 ganhou")
if tipo==3:
    pcvit=0
    usvit=0
    while (1==1):
        usesc=int(input("faça a sua escolha (1 para Spock, 2 para tesoura, 3 para papel, 4 para pedra e 5 para lagarto), aprendiz: "))
        pcesc=randint(1,5)
        if pcesc == 1:
            if usesc ==1:
                print("empate!")
            elif usesc ==2:
                pcvit+=1
                print("Spock esmaga tesoura!")
            elif usesc==3:
                usvit+=1
                print("Papel refuta Spock!")
            elif usesc==4:
                pcvit+=1
                print("Spock vaporiza pedra!")
            elif usesc==5:
                usvit+=1
                print("Lagarto envenena Spock!")
        
        if pcesc == 2:
            if usesc ==1:
                usvit+=1
                print("Spock esmaga tesoura!")
            elif usesc ==2:
                print("empate!")
            elif usesc==3:
                pcvit+=1
                print("Tesoura corta papel!")
            elif usesc==4:
                usvit+=1
                print("Pedra quebra tesoura!")
            elif usesc==5:
                pcvit+=1
                print("Tesoura decapita lagarto!")
        
        if pcesc == 3:
            if usesc ==1:
                pcvit+=1
                print("Papel refuta Spock!")
            elif usesc ==2:
                usvit+=1
                print("Tesoura corta papel!")
            elif usesc==3:
                print("empate!")
            elif usesc==4:
                pcvit+=1
                print("Papel cobre pedra!")
            elif usesc==5:
                usvit+=1
                print("Lagarto come papel!")
        
        if pcesc == 4:
            if usesc ==1:
                usvit+=1
                print("Spock vaporiza pedra!")
            elif usesc ==2:
                pcvit+=1
                print("Pedra quebra tesoura!")
            elif usesc==3:
                usvit+=1
                print("Papel cobre pedra!")
            elif usesc==4:
                print("empate!")
            elif usesc==5:
                pcvit+=1
                print("Pedra esmaga lagarto!")
        
        if pcesc == 5:
            if usesc ==1:
                pcvit+=1
                print("Lagarto envenena Spock!")
            elif usesc ==2:
                usvit+=1
                print("Tesoura decapita lagarto!")
            elif usesc==3:
                pcvit+=1
                print("Lagarto come papel!")
            elif usesc==4:
                usvit+=1
                print("Pedra esmaga lagarto!")
            elif usesc==5:
                print("empate!")
        print("voce tem %d" %usvit , "pontos")
        print("computador tem %d" %pcvit , "pontos")