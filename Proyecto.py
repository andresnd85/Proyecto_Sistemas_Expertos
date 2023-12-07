
class SistemaExperto:
    def __init__(self):
        self.base_conocimientos = {
            'Fiebre': {'Gripe': 0.8, 'Resfriado': 0.6, 'COVID-19': 0.9},
            'Dolor_de_cabeza': {'Gripe': 0.5, 'Migraña': 0.7, 'COVID-19': 0.6},
            'Dolor_de_garganta': {'Resfriado': 0.7, 'Gripe': 0.6, 'COVID-19': 0.8},
        }

    def obtener_diagnostico(self, sintomas):
        puntajes_enfermedades = {}

        for sintoma, intensidad in sintomas.items():
            if sintoma in self.base_conocimientos:
                for enfermedad, factor in self.base_conocimientos[sintoma].items():
                    puntaje = intensidad * factor
                    puntajes_enfermedades[enfermedad] = puntajes_enfermedades.get(enfermedad, 0) + puntaje

        # Encuentra la enfermedad con el puntaje más alto
        enfermedad_diagnosticada = max(puntajes_enfermedades, key=puntajes_enfermedades.get)
        confianza_diagnostico = puntajes_enfermedades[enfermedad_diagnosticada]

        return enfermedad_diagnosticada, confianza_diagnostico


def main():
    sistema_experto = SistemaExperto()

    # Ingresa los síntomas y su intensidad (de 0 a 1) que experimenta el usuario
    sintomas_usuario = {
        'Fiebre': 0.8,
        'Dolor_de_cabeza': 0.6,
        'Dolor_de_garganta': 0.7
    }

    enfermedad_diagnosticada, confianza_diagnostico = sistema_experto.obtener_diagnostico(sintomas_usuario)

    print(f"Diagnóstico: {enfermedad_diagnosticada}")
    print(f"Confianza del diagnóstico: {confianza_diagnostico}")


if __name__ == "__main__":
    main()
