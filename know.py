
class MedicalDiagnosticSystem:
    def __init__(self):
        # Knowledge Base: Rules that associate symptoms to diseases
        self.rules = {
            "Flu": [
                {"fever": True, "cough": True, "headache": False},
                {"fever": True, "cough": False, "headache": True}
            ],
            "Pneumonia": [
                {"fever": True, "cough": True, "difficulty_breathing": True},
                {"fever": True, "cough": False, "difficulty_breathing": True}
            ],
            "Common Cold": [
                {"fever": False, "cough": True, "headache": False},
                {"fever": False, "cough": True, "headache": True}
            ],
            "Migraine": [
                {"fever": False, "cough": False, "headache": True}
            ]
        }

        # List of symptoms we will ask the user
        self.symptoms = ["fever", "cough", "headache", "difficulty_breathing"]

    def ask_symptoms(self):
        # Ask the user about symptoms
        symptoms_data = {}
        for symptom in self.symptoms:
            response = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
            symptoms_data[symptom] = response == "yes"
        return symptoms_data

    def diagnose(self, symptoms_data):
        possible_diagnoses = []

        # Check each rule for matching symptoms
        for disease, symptom_rules in self.rules.items():
            for rule in symptom_rules:
                if all(rule[symptom] == symptoms_data[symptom] for symptom in rule):
                    possible_diagnoses.append(disease)

        return possible_diagnoses if possible_diagnoses else ["No diagnosis found."]

    def run_diagnosis(self):
        # Step 1: Ask the user about their symptoms
        symptoms_data = self.ask_symptoms()

        # Step 2: Make a diagnosis based on the symptoms provided
        diagnoses = self.diagnose(symptoms_data)

        # Step 3: Show the result
        if diagnoses:
            print("\nPossible diagnoses based on your symptoms:")
            for diagnosis in diagnoses:
                print(f"- {diagnosis}")
        else:
            print("\nWe couldn't find any matching diagnoses based on your symptoms.")

# Main function to run the system
if __name__ == "__main__":
    system = MedicalDiagnosticSystem()
    system.run_diagnosis()