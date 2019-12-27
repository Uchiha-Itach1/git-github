hotdogsinpackage = 10
hotdogbunsinpackage = 8

guest = int (input("How Many Guest are invited :"))
each = int(input("Number Of Hot DOgs Each Will be Given :"))

hotdogrequired = guest * each
bunsrequired = hotdogrequired

hotdogpackagerequired = int(hotdogrequired / hotdogbunsinpackage)
bunpackagerequired = int(bunsrequired / hotdogbunsinpackage)

remainderhotdog = hotdogrequired % hotdogsinpackage
remainderbun = bunsrequired % hotdogbunsinpackage

if remainderhotdog > 0 :
    exacthotdogpackage = int(hotdogpackagerequired + 1)
else :
    exacthotdogpackage = int(hotdogpackagerequired)

if remainderbun > 0 :
    exactbun = bunpackagerequired + 1
else :
    exactbun = bunpackagerequired

hotdogleftover = (exacthotdogpackage * 10) - hotdogrequired
bunleftover = (exactbun * 8) - bunsrequired

print("\nNumber of Packages of hot dog required :" + str(exacthotdogpackage))
print("Number of packages of bun required :" + str(exactbun))
print("Number of Hot DOgs Left : " + str(hotdogleftover))
print("Number of Buns Left :" + str(bunleftover))