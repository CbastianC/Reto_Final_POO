#Clase que representa a una familia recicladora
class FamiliaRecicladora:
    def __init__(self, nombre, integrantes, direccion):
        self.nombre = nombre
        self.integrantes = integrantes
        self.direccion = direccion
        self.materiales = []

#Registra un material reciclado con su tipo, peso y fecha
    def registrar_material(self, tipo, peso, fecha):
        material = MaterialReciclado(tipo, peso, fecha)
        self.materiales.append(material)

#Calcula los puntos acumulados por la familia según los materiales reciclados.
    def calcular_puntos(self):
        return sum(material.obtener_puntos() for material in self.materiales)

#Genera un resumen de reciclaje por familia.
    def resumen_reciclaje(self):
        resumen = f"\nFamilia: {self.nombre}\nMateriales Reciclados:\n"
        for material in self.materiales:
            resumen += f"- {material.tipo}: {material.peso} kg, Fecha: {material.fecha}\n"
        resumen += f"Total de puntos acumulados: {self.calcular_puntos()}\n"
        return resumen

#Clase que representa un material reciclado.
class MaterialReciclado:
    PUNTOS_POR_KG = {'Plástico': 2, 'Papel': 1, 'Vidrio': 3, 'Metal': 4}

    def __init__(self, tipo, peso, fecha):
        self.tipo = tipo
        self.peso = peso
        self.fecha = fecha

#Calcula puntos según el tipo de material reciclado.
    def obtener_puntos(self):
        return self.peso * self.PUNTOS_POR_KG.get(self.tipo, 1)

#Función que maneja la interacción en consola.
def menu():
    familias = {}
    
    while True:
        print("\n Menú de Reciclaje")
        print("1. Registrar familia")
        print("2. Registrar material reciclado")
        print("3. Mostrar resumen por familia")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la familia: ")
            integrantes = int(input("Número de integrantes: "))
            direccion = input("Dirección: ")
            familias[nombre] = FamiliaRecicladora(nombre, integrantes, direccion)
            print("✅ Familia registrada exitosamente.")
        
        elif opcion == "2":
            nombre = input("Nombre de la familia: ")
            if nombre in familias:
                tipo = input("Tipo de material (Plástico, Papel, Vidrio, Metal): ")
                peso = float(input("Peso en kg: "))
                fecha = input("Fecha (DD/MM/AAAA): ")
                familias[nombre].registrar_material(tipo, peso, fecha)
                print("♻️ Material registrado exitosamente.")
            else:
                print("⚠️ La familia no está registrada.")
        
        elif opcion == "3":
            nombre = input("Nombre de la familia: ")
            if nombre in familias:
                print(familias[nombre].resumen_reciclaje())
            else:
                print("⚠️ La familia no está registrada.")
        
        elif opcion == "4":
            print("¡Gracias por contribuir al reciclaje! 🌍")
            break
        
        else:
            print("⚠️ Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()