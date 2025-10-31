# Simple Medical Diagnostic System
# Beginner-friendly version

class MedicalDiagnosticSystem:
    def __init__(self):
        # Simple rules connecting symptoms to diseases
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

        # List of symptoms to ask
        self.symptoms = ["fever", "cough", "headache", "difficulty_breathing"]

    def get_symptoms(self):
        user_symptoms = []
        print("Answer the following with 'yes' or 'no':\n")

        for s in self.symptoms:
            ans = input(f"Do you have {s}? ").strip().lower()
            if ans == "yes":
                user_symptoms.append(s)

        return user_symptoms

    def diagnose(self, user_symptoms):
        possible = []

        for disease, needed_symptoms in self.rules.items():
            # If all required symptoms are present in user's symptoms
            if all(symptom in user_symptoms for symptom in needed_symptoms):
                possible.append(disease)

        return possible

    def run(self):
        print("=== Welcome to the Simple Medical Diagnostic System ===")
        symptoms = self.get_symptoms()
        results = self.diagnose(symptoms)

        print("\n--- Diagnosis Result ---")
        if results:
            for r in results:
                print(f"- {r}")
        else:
            print("No matching disease found based on your symptoms.")


# Run the system
if __name__ == "__main__":
    system = MedicalDiagnosticSystem()
    system.run()
