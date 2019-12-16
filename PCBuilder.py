
def buildPC(budget,processor,use):

    try:

        budget = int(budget)
    #INPUTS THE USER'S BUDGET AND MAKES SURE THEY CAN AFFORD THE PARTS
        if budget < 550:
                return("You do not have enough money to build a PC. You should buy a laptop or a pre-built PC instead")
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
            if storageBudget*0.5 > 175:

                storageBudget = storageBudget - 175
                SSD = "1TB SSD"
                ssdPrice = 175

            elif storageBudget*0.5 > 80:

                storageBudget = storageBudget - 80
                SSD = "512GB SSD"
                ssdPrice = 80

            else:

                storageBudget = storageBudget - 35
                SSD = "256GB SSD"
                ssdPrice = 35

            if storageBudget >= 155:
                HDD = "4TB HDD"
                hddPrice = 155

            elif storageBudget >= 99:
                HDD = "2TB HDD"
                hddPrice = 99
            
            elif storageBudget >= 49:
                HDD = "1TB HDD"
                hddPrice = 49

            elif storageBudget >= 35:
                HDD = "512GB HDD"
                hddPrice = 35

            
            if processor == "Intel":
                motherboard = "Intel Compatible Motherboard"

            elif processor == "AMD":
                motherboard = "AMD compatible motherboard"


    #CREATES A LIST OF PRODUCTS AND THEIR RESPCTIVE PRICES 
            part = ["Processor", "Graphics Card", "Memory", "SSD", "HDD", motherboard, "Power Supply", "Case"]
            choice = [CPU, GPU, RAM, SSD, HDD, "", "", ""]
            price = [cpuPrice, gpuPrice, ramPrice, ssdPrice, hddPrice, moboBudget, psuBudget, caseBudget]

            l1 = ("\n" + "\n" + "###              Your Parts              ###" + "\n" + "\n" + "Your budget: " + str(budget) + "\n")
            l2 = ( "Part" + " "*30 + "Selection" + " "*23 + "Price")
            l3 = ( "-"*80)

            array = []
            for x in range(8):
                array.append(part[x] + " "*(31 - len(part[x])) + "-  " + choice[x] + " "*(29 - len(choice[x])) +  "-  " + "$" + str(round(price[x])))

            l4 = array[0]
            l5 = array[1]
            l6 = array[2]
            l7 = array[3]
            l8 = array[4]
            l9 = array[5]
            l10= array[6]
            l11= array[7]
            

            l12 = ( "-"*80) 
            l13 = ("Budget:" + " "*56 + "-  " + "$" + str(budget))
            l14 = ("Total:" + " "*57 + "-  " + "$" + str(round(cpuPrice+gpuPrice+ramPrice+moboBudget+psuBudget+storageBudget+caseBudget)))
            l15 = ("Leftover Money:" + " "*48 + "-  " + "$" + str(round(budget - (cpuPrice+gpuPrice+ramPrice+moboBudget+psuBudget+storageBudget+caseBudget))))
        
            return (l1 + "\n" + l2 + "\n" + l3 + "\n" + l4 + "\n" + l5 + "\n" + l6 + "\n" + l7 + "\n" + l8 + "\n" + l9 + "\n" + l10 + "\n" + l11 + "\n" + l12 + "\n" + l13 + "\n" + l14 + "\n" + l15)

    except:
        if not type(budget) == int:
            return "ERROR: Please enter a valid budget in US dollars"

        else:
            return "ERROR: Please open an issue on GitHub describing your problem"

    
