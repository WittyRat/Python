import random
import time


#--- inimese atribuudid
level=1
xp=0  #tõstab levelit    xp=vastase level  100xp = +lvl
hp=100
max_damage=25
armor=0 # 1:1 vahendab vastase runnet
gold=0
#---------- items
potions=2

#--- Vastaste atribuudid

mob_lvl_1 = {
  "rott": 1,
  "hiir": 2,
  "orav": 3
}

entry_list = random.choice(list(mob_lvl_1.keys()))


vastase_elud=100
enemy_max_damage=15


#----------eriline koletis
bear_hp=300
bear_max_damage=50

#----------------
def intro():
    print("Sa olid metsas kõndimas")
    time.sleep(3)
    print("Järsku sa nägid, et sinu poole oli tulemas paar meest")
    time.sleep(3)
    print("Neil olid käes mõõgad")
    time.sleep(3)
    print("Arvatavasti on need mingid röövlid")
    time.sleep(3)
    print("Sa võtsid oma mõõga kätte ja hakkad kaklema")
    time.sleep(3)
    print("Aga siis muutus kõik mustaks")
    time.sleep(3)
   
#----------------
def trap():
    print("Sa proovid põgeneda")
    time.sleep(3)
    print("Jooksmise ajal sa kukud ja vigastad oma jala")
    time.sleep(3)
    print(entry_list + " jõuab sulle järgi")
    time.sleep(3)
    print("aga järsku ta vaatab üles ning jookseb sinu juurest minema.")
    time.sleep(3)
    print("Sa oled õnnelik, et " + entry_list + " minema jooksis.")
    time.sleep(3)
    print("Sa tõused püsti ja vaatad selja taha")
    time.sleep(3)
    print("sa näed kolme meetrist karu enda kohal.")
    time.sleep(3)
    print("Sa võtad oma mõõga ja hakkad temaga kaklema")
    time.sleep(3)
    print("Lootes, et sa võidad")
    time.sleep(3)

point=0
story=1
game_on=int((input("Vajuta '1' kui tahad mängu alustada ")))
if game_on!=1:
    exit()
else:    
    while game_on==1:
      #----------story
        intro()
        print("Sa ärkasid üles")
        time.sleep(1.5)
        print("Sa vaatad enda ümber ja näed, et sa oled koopas.")
        time.sleep(1.5)
        print("Hakkad liikuma")
        time.sleep(1.5)
        print("Kõndisid natukene kuni nägid ühte suurt ämbliku")
        time.sleep(1.5)
        print("Sa hakkad temaga kaklema")
        time.sleep(1)
        print("------------------\nSinu vastaseks on: ämblik")
        time.sleep(1)
        while story==1:     
            time.sleep(1)
            vastase_elud=vastase_elud-random.randint(0, max_damage)
            print("Vastase elud: " + str(vastase_elud))
            time.sleep(1)
            hp=hp+armor-random.randint(0, enemy_max_damage)
            print("sinu elud: " + str(hp))
            if hp<=0:
                game_on=0
                print("Surid ära! L")
            if vastase_elud<=0:
                print("Tapsid vaenlase\n------------")
                print("Teenisid +100xp ja 50 kulda")
                xp+=100
                gold+=50
                max_xp=100
                vastase_elud=100
                story=0

                story2=1
                
            if xp==100 and max_xp==100:
                max_xp=max_xp*1,14
                xp=0
                level+=1
                hp=100
                print(f"Level up! {level}")
                time.sleep(1.5)
                point=int(input("Kuhu tahate panna punkti kas eludele või rünnakule? (1/2) "))
                if point==1:
                    hp+=15
                    print("Elusi on sul nüüd " + str(hp))
                if point==2:
                    max_damage+=5
                    print("Sinu maksimum rünnak on nüüd " + str(max_damage))
           

     #---------- 
        while story2==1:
            time.sleep(2)
            print("Pärast ämbliku tapmist leidsid sa kirstu.")
            time.sleep(1.5)
            print("Sa katsud kirstu ning kuuled mingit heli.")
            time.sleep(1.5)
            chest=int(input("Kas sa tahaksid seda avada? (jah=1/ei=2)"))
            if chest==1:
                print("Kirstu sees oli " + str(entry_list) + "!!")
            while chest!=1:
                print("Mis mõttes sa ei taha avada kirstu!? Pööra ümber ja ava ikkagi.")
                chest=int(input("Ava see kirst nüüd! (jah=1)"))
                if chest==1:
                    time.sleep(1)
                    print("Kirstu sees oli " + str(entry_list) + "!!")
                    break
            enemy_level=random.randint(1,level)
            time.sleep(1)
            print("Tema tase on "+ str(enemy_level))
            time.sleep(1)
            vastus=int(input("Kas sa tahad temaga kakelda? (1=jah/2=ei)"))
            if vastus==1:
                print("------------\nSinu vastaseks on: "+ entry_list)
                time.sleep(1)
                battle_on=1
                while battle_on==1:
                    vastase_elud=vastase_elud-random.randint(0, max_damage)
                    print("Vastase elud: " + str(vastase_elud))
                    time.sleep(1)
                    hp=hp+armor-random.randint(0, enemy_max_damage)
                    print("Sinu elud: " + str(hp))
                    
                    if vastase_elud<=0:
                        print("Tapsid vaenlase\n------------")
                        print("Teenisid +100xp ja 50 kulda")
                        xp+=100
                        gold+=50
                        vastase_elud=100
                        battle_on=0
            if vastus==2:
                
                trap()
                battle_on=1
                while battle_on==1:
                    bear_hp=bear_hp-random.randint(0,max_damage)
                    print("Karu elud: " + str(bear_hp))
                    time.sleep(1)
                    hp=hp-random.randint(0, bear_max_damage)
                    print("sinu elud: " + str(hp))
                            
                    if hp<=0:
                        print("Surid ära!")
                        print("Game Over")
                        quit()
                
                    if bear_hp<=0:
                        print("Tapsid ära karu raske vaevaga\naga sa olid nii haavatud, et sa surid ära vere kaotuse tõttu")
                        print("Game Over")
                        quit()
    #-----------------------------------------------
            time.sleep(1)
            print("Koopa seest leiad sa ühe poe")
            vastus=int(input("Kas sa tahad poodi külastada? (1=jah/2=ei)"))
            if vastus==1:
                print("Sul on " + str(gold) + "kulda")
                print("Poes on müügil: ")
                print("Kirves - 50g (annab +5 rünnakut)\nKullast rüü - 100g (näitad sellega, et oled rikas ning +3 armor)")
                valik=int(input("Kas sa soovid osta Kirvest(1) või Kullast rüüd(2)"))
                if valik==1:
                    max_damage+=5
                    print("Ostsid endale kirve. Sinu rünnak on nüüd " + str(max_damage))
                    time.sleep(1.5)
                    vastus=2
                if valik==2:
                    print("Ostsid endale kullast rüü. Said +3 rüüd ja näed parem välja")
                    time.sleep(2.5)
                    vastus=2
            if vastus==2:
                print("Sa jätkad oma seiklust")
                time.sleep(3)
                print("Sa jalutad koopas ringi")
                time.sleep(3)
                print("Järsku märkad, et kusgilt tuleb valgus")
                time.sleep(3)
                print("Lähed valguse poole")
                time.sleep(3)
                print("Ja seal valguse juures ongi väljapääs koopast")
                time.sleep(2)
            story2=0
            story3=432
    #-------------------------
        while story3==432:
            story3=int(input("Kas sa tahad oma seiklusega jätkata(1) või lõpetada(2) "))
            if story3==1:
                print("Äitah, et mängisite!")
                time.sleep(2)
                print("Järgmine seiklus tuleb aastal 2023")
                exit()
            if story3==2:
                print("Sa lõpetasid oma seikluse")
                print("Tänud mängimast")
                exit()
            
     
      
    print("Game Over") 
