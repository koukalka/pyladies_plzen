# Načtení tabulky a uložení yml souboru pro přidání nových členů na web pyladies.cz

import pandas as pd

vstupni_soubor = "D:\\Stažené soubory\\Aktuální seznam koučů a pomocníků.xlsx"
vystupni_soubor = "D:\\Python\\PyLadies\\Podzim_2021_z\\plzen.yml"

def validateLink(link):

    valid_link = link

    if valid_link.startswith("https") == False:
        valid_link = "https://"+ link
    return valid_link

def saveListToFile(listname, pathtosave):
    file1 = open(pathtosave, "w", encoding = "utf-8") 
    for i in listname:
        file1.writelines("{}\n".format(i))    
    file1.close() 


print("--------------------------------NACITAM SOUBOR--------------------------------")
soubor = pd.read_excel(vstupni_soubor,"podzim 2021")
vystup = list()

soubor.info()
soubor.columns = soubor.columns.str.upper()
soubor["STAV"] = soubor["STAV"].str.lower()


print("--------------------------------ZPRACOVAVAM ...--------------------------------")

for radek in range(0,len(soubor)):

    if soubor.loc[radek]["STAV"] == "aktivní":

        vystup.append("- name: " + soubor.loc[radek]["JMÉNO A PŘÍJMENÍ"])
        
        if soubor.loc[radek]["FOTOGRAFIE"] is not None and pd.isna(soubor.loc[radek]["FOTOGRAFIE"]) == False:
            vystup.append("  img: " + "img/plzen/team/"+ soubor.loc[radek]["FOTOGRAFIE"])
        else:
            vystup.append("  img: img/plzen/team/blank.png")
        
        vystup.append("  role: " + soubor.loc[radek]["POPIS"])
        vystup.append("  links:")
        vystup.append("  - mail-link: mailto:" + soubor.loc[radek]["E-MAIL"])
        
        if soubor.loc[radek]["FB"] is not None and pd.isna(soubor.loc[radek]["FB"]) == False:
            vystup.append("  - facebook-link: " + validateLink(soubor.loc[radek]["FB"]))
        
        if soubor.loc[radek]["GITHUB"] is not None and pd.isna(soubor.loc[radek]["GITHUB"]) == False:
            vystup.append("  - github-link: " + validateLink(soubor.loc[radek]["GITHUB"]))
        
        if soubor.loc[radek]["WEB"] is not None and pd.isna(soubor.loc[radek]["WEB"]) == False:
            vystup.append("  - website-link: " + validateLink(soubor.loc[radek]["WEB"]))
        
        if soubor.loc[radek]["TWITTER"] is not None and pd.isna(soubor.loc[radek]["TWITTER"]) == False:
            vystup.append("  - twitter-link: " + validateLink(soubor.loc[radek]["TWITTER"]))
        
        if soubor.loc[radek]["LINKEDIN"] is not None and pd.isna(soubor.loc[radek]["LINKEDIN"]) == False:
            vystup.append("  - linkedin-link: " + validateLink(soubor.loc[radek]["LINKEDIN"]))
        
        vystup.append("") #prazdny radek, bude novy clen
    else:
        continue


# to save:
saveListToFile(vystup, vystupni_soubor)
print("--------------------------------HOTOVO--------------------------------")