class MedicalDiagnoseSystem:

    def __init__(self):
            self.rules={
                "Flu":[
                    {"fever":True,"cough":True,"headache":False},
                    {"fever":True,"cough":False,"headache":True}
                ],
                "Pneumonia":[
                    {"fever":True,"cough":True,"difficulty_breathing":True},
                    {"fever":True,"cough":False,"difficulty_breathing":True}
                ],
                "Common Cold":[
                    {"fever":False,"cough":True,"headache":False},
                    {"fever":False,"cough":True,"headache":True}
                ],
                "Migraine":[
                    {"fever":False,"cough":False,"headache":True}, 
                ]
            }
            self.symptoms=["fever","cough","headache","difficulty_breathing"]


    def get_symptoms(self):
        user_symptoms={}
        print("Answer the following with yes or no:")
        for s in self.symptoms:
             ans=input(f"Do you have {s}? ").strip().lower()
             if ans=="yes":
                  user_symptoms[s] = True
        return user_symptoms
    
    def diagnose(self,user_symptoms):
        possible=[]
        for disease,rules in self.rules.items():
            for rule in rules:
                # check if all symptoms in this rule match user's responses
                if all(user_symptoms.get(symptom, False) == value for symptom, value in rule.items()):
                    possible.append(disease)
                    break
        return possible
    
    def run(self):
        print("Welcome to the Simple Medical Diagnostic System")
        symptoms=self.get_symptoms()
        result=self.diagnose(symptoms)

        print("Diagnosis result:")
        if result:
            for r in result:
                print(f"- {r}")

        else:
             print("No matching disease found")

if __name__=="__main__":
    system=MedicalDiagnoseSystem()
    system.run()


