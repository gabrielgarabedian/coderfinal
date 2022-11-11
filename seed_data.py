from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")

from blog.models import Post

Post(title= "Mi Post", short_content="contiene un posteo", content="agwufeajedjanejfoaewhfhiofioeqwjkjas").save()

print("Se cargo con exito los post de prueba")

from rutina.models import Rutina


Rutina(nombre_rutina= "Rutina Hipertrofia para mujer", short_content="Se trabaja el cuerpo completo, 3 Veces a la semana, ", content="""gluteos/hombros series rep peso
hip thrust 4 10 10 kg
gluteos en polea 3 12 15 kg
prensa de costado 3 8 10 kg
abductores en maquina 3 12 40 kg
hombros mancuernas 3 10 5 kg
vuelos laterales manc 3 12 3 kg
frontal con disco + 3 10 5 kg
posterior con manc 3 12 3 kg
cuadriceps/dorsales series rep peso
sentadilla libre 3 10 10kg
cuadriceps maquina 3 12 30 kg
prensa 3 10 45 kg
estocada caminando 3 16 3 kg
tiron al pecho 3 10 25 kg
remo en polea 3 10 20 kg
depresores en polea 3 12 15 kg
remo con mancuerna 3 10 7 kg
isquio/pecho/ brazos series rep peso
peso muerto 4 10 10kg
isquios en maquina 3 10 25 kg
flexion de brazos/rodillas 3 10 0 kg
aperturas mancuernas 3 12 4 kg
biceps inc/ mancuernas + 3 10 4 kg
press frances mancuernas 3 10 4 kg
biceps barra en polea + 3 12 15kg
triceps soga en polea 3 12 20 kg""").save()     

print("Se cargo con exito los post de prueba")


