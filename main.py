#Definir la fonction calculate_total_ratio
def calculate_total_ratio(youth,working_age,elderly):
    if working_age==0:
        return "Error: Zero Working population"
    else:
        Total_ratio=100*(youth+elderly)/working_age
        return round(Total_ratio,2)
#Definir la fonction calculate_youth_ratio
def calculate_youth_ratio(youth,working_age):
    if working_age==0:
        return "Error: Zero Working population"
    else:
        Youth_ratio=100*(youth/working_age)
        return round(Youth_ratio,2)
print("------------------------------------------------------------------------------------------------------")
#Test
youth_A = 10928637
working_A = 25944272
elderly_A = 2395339
youth_B=1200000
working_B=1800000
elderly_B=250000
youth_C=400000
working_C=2500000
elderly_C=800000
youth_O= 100
working_O=0
elderly_O=50
#appel de la fonction pour les ratios totals
ratio_A=calculate_total_ratio(youth_A,working_A,elderly_A)
ratio_B=calculate_total_ratio(youth_B,working_B,elderly_B)
ratio_C=calculate_total_ratio(youth_C,working_C,elderly_C)
ratio_O=calculate_total_ratio(youth_O,working_O,elderly_O)
#appel de la fonction pour les ratios young
ratio_a=calculate_youth_ratio(youth_A,working_A)
ratio_b=calculate_youth_ratio(youth_B,working_B)
ratio_c=calculate_youth_ratio(youth_C,working_C)
ratio_o=calculate_total_ratio(youth_O,working_O,elderly_O)
# importer la fonction pour les units test
from bakery import assert_equal 
# verifier le test d'abord pour les Total ratio
assert_equal(ratio_A,51.36)
assert_equal(ratio_B,80.56)
assert_equal(ratio_C,48.00)
assert_equal(ratio_O, 23)
#verifier le test pour les youth radio 
assert_equal(ratio_a,42.12)
assert_equal(ratio_b,66.67)
assert_equal(ratio_c,16.00)
assert_equal(ratio_o,6)
print("-----------------------------------------------------------------------------------------------------------")
#Analyse sequentielle
#pour les ratio total
ratio_A=calculate_total_ratio(youth_A,working_A,elderly_A)
if ratio_A>75:
    print("Le Ratio de Dépendance Total est élevé, indiquant une Forte Dépendance.")
elif ratio_A>50 and ratio_A<=75:
    print("Le Ratio de Dépendance Total est au-dessus de $50$, indiquant une Dépendance Modérée.")
else:
    print("Le Ratio de Dépendance Total est inférieur ou égal à $50$, indiquant une Faible Dépendance.")
ratio_B=calculate_total_ratio(youth_B,working_B,elderly_B)
if ratio_B>75:
    print("Le Ratio de Dépendance Total est élevé, indiquant une Forte Dépendance.")
elif ratio_B>50 and ratio_B<=75:
    print("Le Ratio de Dépendance Total est au-dessus de $50$, indiquant une Dépendance Modérée.")
else:
    print("Le Ratio de Dépendance Total est inférieur ou égal à $50$, indiquant une Faible Dépendance.")
ratio_C=calculate_total_ratio(youth_C,working_C,elderly_C)
if ratio_C>75:
    print("Le Ratio de Dépendance Total est élevé, indiquant une Forte Dépendance.")
elif ratio_C>50 and ratio_C<=75:
    print("Le Ratio de Dépendance Total est au-dessus de $50$, indiquant une Dépendance Modérée.")
else:
    print("Le Ratio de Dépendance Total est inférieur ou égal à $50$, indiquant une Faible Dépendance.")
print("----------------------------------------------------------------------------------------------------------------")
#Pour les ratios Youth
if ratio_a>45:
    print("Le Ratio de Dépendance Jeunesse est élevé, ce qui signale une Forte Dépendance de la Jeunesse.")
elif ratio_a>30 and ratio_a<=45:
    print("Le Ratio de Dépendance Jeunesse est modéré, indiquant une Dépendance Modérée de la Jeunesse.")
else:
    print("Le Ratio de Dépendance Jeunesse est faible, ce qui signale une Faible Dépendance de la Jeunesse.")
ratio_b=calculate_youth_ratio(youth_B,working_B)
if ratio_b>45:
    print("Le Ratio de Dépendance Jeunesse est élevé, ce qui signale une Forte Dépendance de la Jeunesse.")
elif ratio_b>30 and ratio_b<=45:
    print("Le Ratio de Dépendance Jeunesse est modéré, indiquant une Dépendance Modérée de la Jeunesse.")
else:
    print("Le Ratio de Dépendance Jeunesse est faible, ce qui signale une Faible Dépendance de la Jeunesse.")
ratio_c=calculate_youth_ratio(youth_C,working_C)
if ratio_c>45:
    print("Le Ratio de Dépendance Jeunesse est élevé, ce qui signale une Forte Dépendance de la Jeunesse.")
elif ratio_c>30 and ratio_c<=45:
    print("Le Ratio de Dépendance Jeunesse est modéré, indiquant une Dépendance Modérée de la Jeunesse.")
else:
    print("Le Ratio de Dépendance Jeunesse est faible, ce qui signale une Faible Dépendance de la Jeunesse.")
print("----------------------------------------------------------------------------------------------------------------")



   
    

