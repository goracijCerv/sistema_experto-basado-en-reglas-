print("Responda todas las preguntas con un si o un no");
########Preguntas ciclo del cultivo
print("Preguntas para saber  el ciclo del cultivo");
ccp1 = input("¿El maíz se encuentra en la etapa de floracion?");
ccp2= input("¿El maiz se encuentra en la etapa de emergencia?");
if( ccp1 == "si" and ccp2=="no"):
    cc="EF" ## etaoa de floracion
elif(ccp1=="no" and ccp2=="si"):
    cc="EE"##etapa de emergencia
else:
    cc="NI"#Singnifica no hay informacion
##########Preguntas huevecillos
print("Preguntas para saber la variable huevecillos en el cultivo");
hcp1=input("¿Se visualizaron huevecillos en algun momento?");
if(hcp1 == "si"):
    hcp2=input("¿los huevecillos estaban en la parte inferior de la hoja?")
    hcp3=input("¿los huevecillos son blancos?")
    hcp4=input("¿el blanco es brillante?")
    hcp5=input("¿estaban cubuiertos por una especie de algodon?")
    hcp6=input("¿los huevecillos se encuentran en la hoja tierna del elote?")
    if(hcp2 == "si" and hcp3 == "si" and hcp4 =="no" and hcp5 == "si" and hcp6 == "no"):
        hc="HBA" #huevecillos blancos con una especie de algodón.
    elif(hcp2 == "no" and hcp3 == "si" and hcp4 =="si" and hcp5 == "no" and hcp6 == "si"):
        hc="HBB" #huevecillos blancos brillantes
    else:
        hc="NI"
else:
    hc="SNH" # sin huevecillos visibles
######Preguntas  insectos adultos similares a los adultos de la plaga
print("Preguntas para saber las caracterisitcas de los insectos adultos");
insAp1=input("¿Se han visualizado polillas en los alrededores del cultivo?")
if(insAp1 == "si"):
    insAp2=input("¿La polilla posee una tonalidad de café en la parte de la cabeza?")
    insAp3=input("¿El abdomen tiene una tonalidad café y manchas blancas?")
    insAp4=input("¿Las alas tienen una medida de 25 milímetros aproximadamente?")
    insAp5=input("¿El abdomen tiene solo una tonalidad café?")
    insAp6=input("¿Las alas tienen una tonalidad café y manchas negras?")
    insAp7=input("¿Las alas tienen una tonalidad café con manchas blancas y las las inferiores son grisáceas?")
    if(insAp2 =="si" and insAp3=="no" and insAp4=="no" and insAp5 =="si" and insAp6=="si" and insAp7=="no"):
        insA="PCMN" #polilla con color café y manchas negras a su alrededor.
    elif(insAp2 =="si" and insAp3=="si" and insAp4=="si" and insAp5 =="no" and insAp6=="no" and insAp7=="si"):
        insA="PCACG" #polilla con una tonalidad café y sus alas tienen dos tonalidades café y grisáceo.
    else:
        insA="NI"
else:
    insAp8=input("¿Se han visualizado insectos similares a pulgas verdes?")
    if(insAp8=="si"):
        insA="INSPV"
    else:
        insA="NI"
     #insectos similares a pulgas de color verde
####Preguntas insectos “infantes” similares a los de la plaga
print("Preguntas para el aspecto del insecto infante");
insNp1=input("¿Se observan gusanos en alguna parte del cultivo?")
insNp2=input("¿Se observan insectos similares a pulgas de color verde o blanco?")
if(insNp1=="si" and insNp2=="no"):
    insNp3=input("¿Se encuentran dos o un gusano en el cultivo?")
    insNp4=input("¿Se encuentran más de dos gusanos?")
    insNp5=input("¿el gusano tiene una tonalidad oscura con líneas café o presenta una tonalidad verde y las líneas son más obscuras ?")
    insNp6=input("¿El gusano está cerca del elote?")
    insNp7=input("¿el gusano tiene una tonalidad verde pálido o rojizo o café  y tienen algo de peludo?")
    if(insNp3 == "si" and insNp4=="no" and insNp5=="no" and insNp6=="si" and insNp7=="si"):
        insN="GAOCV"#gusano amarillento o oscurecido o con tonalidades cafés o verdes
    elif(insNp3 == "no" and insNp4=="si" and insNp5=="si" and insNp6=="no" and insNp7=="no"):
        insN="GOMC" #gusano color oscuro presentando manchas café y algo de blanco o presentan un color verdoso
    else:
        insN="NI"
elif(insNp1=="no" and insNp2=="si"):
    insN="PCBV" # insecto similar a una pulga con un color blanco o ya sea verde.
else:
    insN="NI"
#######Preguntas clima
print("Preguntas para saber la estacion");
clp1=input("¿Se encuentra en primavera?")
clp2=input("¿Se encuentra en verano?")
if(clp1=="si" and clp2=="no"):
    cl="PRIM" #primavera
elif(clp1=="no" and clp2=="si"):
    cl="VER" #verano
else:
    cl="NI"
####Preguntas aspectos de las hojas
print("Preguntas para saber los daños de la hoja");
hojp1=input("¿Existen agujeros irregulares en las hojas que envuelven al elote?")
hojp2=input("¿Las hojas se han vuelto amarillentas y se han enroscado?")
hojp3=input("¿Existen agujeros  irregulares en las hojas del cultivo y en solo la nervadura no presenta daños?")
if(hojp1=="si" and hojp2=="no" and hojp3=="no"):
    hojA="AHEE"# gujeros sobre las hojas que envuelven el elote
elif(hojp1=="no" and hojp2=="si" and hojp3=="no"):
    hojA="AHM" #hojas se vuelven manchas (amarillentas y se enroscan)
elif(hojp1=="no" and hojp2=="no" and hojp3=="si"):
    hojA="API" #hojas tienen perforaciones irregulares y  no presenta daño a la nervadura
else:
    hojA="NI"
#####Preguntas Aspecto del elote
print("Preguntas para saber la condicion del elote");
elotp1=input("¿El elote tiene un tamaño menor al común?")
elotp2=input("¿El elote tiene agujeros irregulares en su punta, además de algunos en las hojas que lo envuelven?")
elotp3=input("¿El elote tiene agujeros irregulares en las hojas que lo envuelven?")
if(elotp1=="si" and elotp2=="no" and elotp3=="no"):
    elotA="DT" #disminución del tamaño común del elote
elif(elotp1=="no" and elotp2=="si" and elotp3=="no"):
    elotA="AIPE" #agujeros irregulares en la punta del elote.
elif(elotp1=="no" and elotp2=="no" and elotp3=="si"):
    elotA="PHE" #perforaciones en las hojas del elote.
else:
    elotA="NI"
###Preguntas Aspectos de granos
print("Preguntas para saber las condiciones de los granos");
granosp1=input("¿Presenta desarrollo incompleto?")
granosp2=input("¿Los granos están mal formados?")
granosp3=input("¿Faltan granos en el elote?")
if(granosp1=="si" and granosp2=="no" and granosp3=="no"):
    granosA="DI" #desarrollo incompleto en los granos
elif(granosp1=="no" and granosp2=="no" and granosp3=="si"):
    granosA="FG" # falta de granos
elif(granosp1=="no" and granosp2=="si" and granosp3=="si"):
    granosA="FGMF" # falta de granos del maíz y mal deformación
else:
    granosA="NI"
######Preguntas secreciones de la plaga
print("Preguntas para conocer las caracteristicas de los desechos");
secrep1=input("¿En las hojas se encuentran manchas café?")
secrep2=input("¿En las hojas se encuentra una sustancia similar a la seda?")
secrep3=input("¿En las hojas o en las espinillas se siente una sustancia viscosa?")
secrep4=input("¿En los granos se encuentran manchas marrones?")
if(secrep1=="si" and secrep2=="si" and secrep3=="no" and secrep4=="no"):
    secreA="ECYS" #excremento café sea en las hojas o cerca del elote o existe algo similar a la seda en las hojas
elif(secrep1=="no" and secrep2=="no" and secrep3=="si" and secrep4=="no"):
    secreA="EVH" #sensación viscosa en las hojas o en la espiga
elif(secrep1=="no" and secrep2=="no" and secrep3=="no" and secrep4=="si"):
    secreA="ECG" # manchas marrones en los granos del elote.
else:
    secreA="NI"
######preguntas caracteristicas del cultivo
print("Preguntas para saber como se vio afectada la producion");
carccp1=input("¿La cantidad de elotes generados es menor?")
carccp2=input("¿Algunos cultivos presentan esterilidad?")
if(carccp1=="si" and carccp2=="no"):
    carcc="MCE" # menor cantidad de elotes
elif(carccp1=="no" and carccp2=="si"):
    carcc="PE" #algunas plantas estériles
else:
    carcc="NI"
    
########Relgas variables internas
if(cc=="EF" and insN=="GAOCV"): #regla 1 para gusano elotero
    etapa_ataque_c="GE"
elif(cc=="EF" and insN=="PCBV"): #relga 1 para el pulgon verde
    etapa_ataque_c="PV"
elif(cc=="EE" and insN=="GOMC"): #regla 1 para el gusano soldado
    etapa_ataque_c="GS"
else:
    etapa_ataque_c="ND" #no determinado
#Regla dos
if(hc=="HBB" and insA=="PCMN"): #regla 2 para gusano elotero
    aten_plaga="GE"
elif(hc=="HBA" and insA=="PCACG"): #para gusano soldado
    aten_plaga="GS"
elif(hc=="SNH" and insA=="INSPV"): #para pulgon verde
    aten_plaga="PV"
else:
    aten_plaga="ND"
#Regla tres
if(cl=="PRIM" and insN=="GAOCV"): #gusano elotero
    tiempo_presencia="GE"
elif(cl=="VER" and insN=="PCBV"): #pulgon verde
    tiempo_presencia="PV"
elif(cl=="VER" and insN=="GOMC"): #gusano soldado 
    tiempo_presencia="GS"
else:
    tiempo_presencia="ND"
#Regla cuatro
if(hojA=="AHEE" and elotA=="AIPE"): #gusano elotero
    sintomas_v="GE"
elif(hojA=="AHM" and elotA=="DT"): #pulgon verde
    sintomas_v="PV"
elif(hojA=="API" and elotA=="PHE"): #gusano soldado
    sintomas_v="GS"
else:
    sintomas_v="ND"
#Regla cinco
if(secreA=="ECG" and insN=="GAOCV"): #gusano elotero
    evidencia_pre_c="GE"
elif(secreA=="EVH" and insN=="PCBV"): #pulgon verde
    evidencia_pre_c="PV"
elif(secreA=="ECYS" and insN=="GOMC"): #gusano soldado
    evidencia_pre_c="GS"
else:
    evidencia_pre_c="ND"
##Regla seis
if(carcc=="MCE" and granosA=="FGMF"): #gusano elotero
    evidencia_pre_nc="GE"
elif(carcc=="PE" and granosA=="DI"): #pulgon verde
    evidencia_pre_nc="PV"
elif(carcc=="MCE" and granosA=="FG"): #gusano elotero
    evidencia_pre_nc="GS"
else:
    evidencia_pre_nc="ND"
##Regla siete
if(etapa_ataque_c=="GE" and tiempo_presencia=="GE" or aten_plaga=="GE"):
    contexto_plaga="GE"
elif(etapa_ataque_c=="PV" and tiempo_presencia=="PV" or aten_plaga=="PV"):
    contexto_plaga="PV"
elif(etapa_ataque_c=="GS" and tiempo_presencia=="GS" or aten_plaga=="GS"):
    contexto_plaga="GS"
else:
    contexto_plaga="ND"
####Regla ocho
if(sintomas_v=="GE"and evidencia_pre_c=="GE" or evidencia_pre_nc=="GE"):
    presencia="GE"
elif(sintomas_v=="PV" and evidencia_pre_c=="PV" or evidencia_pre_nc=="PV"):
    presencia="PV"
elif(sintomas_v=="GS" and evidencia_pre_c=="GS" or evidencia_pre_nc=="GS"):
    presencia="GS"
else:
    presencia="ND"

##Regla nueve
if(contexto_plaga=="GE"and presencia=="GE"):
    print("Por los datos analisados podemos decir que es 100%  seguro de que su cultivo tenga la plaga gusano eloero")
elif(contexto_plaga=="PV"and presencia=="PV"):
    print("Por los datos analisados podemos decir que es 100% seguro  de que su cultivo tenga la plaga pulgon verde tambien conocido como pulgon collogo")
elif(contexto_plaga=="GS"and presencia=="GS"):
    print("Por los datos analisados podemos decir que es 100% seguro  de que su cultivo tenga la plaga gusano soldado")
elif(contexto_plaga=="GE" and presencia=="ND"):
    print("Por los datos analisados podemos decir que  posiblemente se de la plaga de gusano elotero")
elif(contexto_plaga=="PV" and presencia=="ND"):
    print("Por los datos analisados podemos decir que  posiblemente se de la plaga de pulgon verde")
elif(contexto_plaga=="GS" and presencia=="ND"):
    print("Por los datos analisados podemos decir que  posiblemente se de la plaga de gusano soldado")
elif(contexto_plaga=="ND" and presencia=="GE"):
    print("Por los datos analisados podemos decir que es 60% seguro de que su cultivo tenga la plaga de gusano elotero")
elif(contexto_plaga=="ND" and presencia=="PV"):
    print("Por los datos analisados podemos decir que es 60% seguro de que su cultivo tenga la plaga de pulgon verde")
elif(contexto_plaga=="ND" and presencia=="GS"):
    print("Por los datos analisados podemos decir que es 60% seguro de que su cultivo tenga la plaga de gusano soldado")
else:
    print("Con los datos analisados no podemos establcer una detecion")