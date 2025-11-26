import random 

def step(p_pentagon=0.8, p_kaia=0.8, audMax=50):
    skritt_count = 0
    pos = audMax
    tid = 0
    
    kaja = 80
    pentagon = 20
    
    while True:
        tid += 1 #ett sek

        if pos == pentagon and random.random() < p_pentagon:#posisjonen må være riktig og sannsynligheten for at han faktisk går inn 80%
            print(f'Pentagon, Skritt: {skritt_count}, Tid: {tid/60:.2f} min')
            break
        
        if pos == kaja and random.random() < p_kaia:
            print(f'Kaja, Skritt: {skritt_count}, Tid: {tid/60:.2f} min')
            break

        #20% sjanse for steg
        if random.random() < 0.2:
            if random.random() < 0.5:#retning 50/50
                pos += 1#mot kaja aka østover
            else:
                pos -= 1#mot pentagon vest

            #så den ikke går lengre enn koordinatsystemet vårt sin grense
            if pos < 0:
                pos = 0
            if pos > 100:
                pos = 100

            skritt_count += 1


step()
