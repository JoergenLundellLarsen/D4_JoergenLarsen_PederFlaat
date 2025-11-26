import random 

def step(p_pentagon=0.8, p_kaia=0.8, audMax=50):
    skritt_count = 0
    pos = audMax#start posisjon audmax satte midt mellom ca
    tid = 0
    
    kaja = 80
    pentagon = 20
    
    while True:
        tid += 1 #ett sek

        if pos == pentagon and random.random() < p_pentagon:#posisjonen må være riktig og sannsynligheten for at han faktisk går inn 80%
            #print(f'Pentagon, Skritt: {skritt_count}, Tid: {tid/60:.2f} min')
            return "Pentagon", skritt_count, tid
        
        if pos == kaja and random.random() < p_kaia:
            #print(f'Kaja, Skritt: {skritt_count}, Tid: {tid/60:.2f} min')
            return "Kaia", skritt_count, tid

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


def main():
    outcomes = []
    steps_list = []
    time_list = []

    for _ in range(1000):
        outcome, steps, tid = step(p_pentagon=0.8, p_kaia=0.8, audMax=50)
        outcomes.append(outcome)
        steps_list.append(steps)
        time_list.append(tid)
    
    #samlet statistikk over n simuleringer 
    print("Pentagon:", outcomes.count("Pentagon"))
    print("Kaia:", outcomes.count("Kaia"))
    print("Gjennomsnitt skritt:", sum(steps_list)/len(steps_list))
    print("Gjennomsnitt tid(min) :", (sum(time_list)/len(time_list))/60)


if __name__ == "__main__":
    main()