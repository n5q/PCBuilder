

def buildPC(budget,processor,use):
#INPUTS THE USER'S BUDGET AND MAKES SURE THEY CAN AFFORD THE PARTS
    if budget < 650:
            print("You do not have enough money to build a PC. You should buy a laptop or a pre-built PC instead")
    else:
        
#DETERMINES RATIOS FOR EACH PART BASED OFF OF THE BUDGET AND USE SELECTED BY THE USER

        if use == "Gaming":
            cpuBudget = budget*0.25
            gpuBudget = budget*0.37
            moboBudget = budget*0.1
            psuBudget = budget*0.04
            ramBudget = budget*0.1
            storageBudget = budget*0.11
            caseBudget = budget*0.03

        if use == "Work":
            cpuBudget = budget*0.38
            gpuBudget = 0
            moboBudget = budget*0.1
            psuBudget = budget*0.08
            ramBudget = budget*0.2
            storageBudget = budget*0.21
            caseBudget = budget*0.03


#DETERMINES BEST PARTS THAT CAN BE PURCHASED UNDER THE USER'S BUDGET
        if processor == "Intel":

            if cpuBudget >= 474:
                CPU = "Intel Core i9 9900k"
                cpuPrice = 474

            elif cpuBudget >= 379:
                CPU = "Intel Core i7 9700K"
                cpuPrice = 379

            elif cpuBudget >= 244:
                CPU = "Intel Core i5 9600K"
                cpuPrice = 244

            elif cpuBudget >= 162:
                CPU = "Intel Core i3 8350K"
                cpuPrice = 162

        elif processor == "AMD":

            if cpuBudget >= 699:
                CPU = "Ryzen 9 3900X"
                cpuPrice = 699

            elif cpuBudget >= 359:
                CPU = "Ryzen 7 3700X"
                cpuPrice = 359

            elif cpuBudget >= 148:
                CPU = "Ryzen 5 2600X"
                cpuPrice = 148

            elif cpuBudget >= 79:
                CPU = "Ryzen 3 2200G"
                cpuPrice = 79
            
        if gpuBudget >= 1200:
            GPU = "RTX 2080 Ti"
            gpuPrice = 1200

        elif gpuBudget >= 700:
            GPU = "RTX 2080 SUPER"
            gpuPrice = 700

        elif gpuBudget >= 500:
            GPU = "RTX 2070 SUPER"
            gpuPrice = 500

        elif gpuBudget >= 400:
            GPU = "RTX 2060 SUPER"
            gpuPrice = 400

        elif gpuBudget >= 350:
            GPU = "RTX 2060"
            gpuPrice = 350

        elif gpuBudget >= 280:
            GPU = "GTX 1660 TI"
            gpuPrice = 280

        elif gpuBudget >= 230:
            GPU = "GTX 1660"
            gpuPrice = 230

        elif gpuBudget >= 150:
            GPU = "GTX 1560"
            gpuPrice = 150

        elif gpuBudget == 0:
            GPU = "None"
            gpuPrice = 0

        if ramBudget >= 175:
            RAM = "32GB RAM (2 Sticks of 16GB)"
            ramPrice = 175

        elif ramBudget >= 90:
            RAM = "16GB RAM (2 Sticks of 8GB)"
            ramPrice = 90

        elif ramBudget >= 50:
            RAM = "8GB RAM (2 Sticks of 4GB)"
            ramPrice = 50

#INCLUDES SSD FOR FASTER BOOT TIMES AND OS PERFORMANCE
        storageBudget = storageBudget - 31
        SSD = "256GB SSD"
        ssdPrice = 31

        if storageBudget >= 95:
            HDD = "4TB HDD"
            hddPrice = 95

        elif storageBudget >= 64:
            HDD = "2TB HDD"
            hddPrice = 64
        
        elif storageBudget >= 42:
            HDD = "1TB HDD"
            hddPrice = 42

        elif storageBudget >= 25:
            HDD = "512GB HDD"
            hddPrice = 25

        
        if processor == "Intel":
            motherboard = "Intel Compatible Motherboard"

        elif processor == "AMD":
            motherboard = "AMD compatible motherboard"


#CREATES A LIST OF PRODUCTS AND THEIR RESPCTIVE PRICES 
        part = ["Processor", "Graphics Card", "Memory", "SSD", "HDD", motherboard, "Power Supply", "Case"]
        choice = [CPU, GPU, RAM, SSD, HDD, "", "", ""]
        price = [cpuPrice, gpuPrice, ramPrice, ssdPrice, hddPrice, moboBudget, psuBudget, caseBudget]

        print("\n" + "\n" + "###              Your Parts              ###" + "\n" + "\n" + "Your budget: " + str(budget) + "\n")
        print( "Part" + " "*30 + "Selection" + " "*23 + "Price")
        print( "-"*80)
        for x in range(8):
            print(part[x] + " "*(31 - len(part[x])) + "-  " + choice[x] + " "*(29 - len(choice[x])) +  "-  " + "$" + str(round(price[x])))  
        print( "-"*80) 
        print("Budget:" + " "*56 + "-  " + "$" + str(budget))
        print("Total:" + " "*57 + "-  " + "$" + str(round(cpuPrice+gpuPrice+ramPrice+moboBudget+psuBudget+storageBudget+caseBudget)))
        print("Leftover Money:" + " "*48 + "-  " + "$" + str(round(budget - (cpuPrice+gpuPrice+ramPrice+moboBudget+psuBudget+storageBudget+caseBudget))))
    



 
