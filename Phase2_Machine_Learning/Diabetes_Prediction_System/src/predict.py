import joblib
import pandas as pd
from pathlib import Path

file=Path(__file__)
crnt_dir=file.resolve().parent
pro_dir=crnt_dir.parent

scale_path=Path(pro_dir/'models'/'diabetes_scaler.pkl')
model_path=Path(pro_dir/'models'/'diabetes_model.pkl')

loaded_scaler=joblib.load(scale_path)
loaded_model=joblib.load(model_path)

def predict_diabetes(pregnancies, glucose, blood_pressure,
                     skin_thickness, insulin, bmi,
                     diabetes_pedigree, age):
    input_data = pd.DataFrame({
    'Pregnancies': [pregnancies],
    'Glucose': [glucose],
    'BloodPressure': [blood_pressure],
    'SkinThickness': [skin_thickness],
    'Insulin': [insulin],
    'BMI': [bmi],
    'DiabetesPedigreeFunction': [diabetes_pedigree],
    'Age': [age]})


    input_scaled=loaded_scaler.transform(input_data)
    prediction = loaded_model.predict(input_scaled)
    probability = loaded_model.predict_proba(input_scaled)

    print(prediction)
    print(probability)
    val1=probability[0][0]*100
    val2=probability[0][1]*100
    print(f'chances of non-diabetes: {val1:.2f}%')
    print(f'chances of diabetes: {val2:.2f}%')
    # Clear Output Formatting
    if prediction[0] == 1:
        print(f" Result: HIGH RISK (Diabetic) - Confidence: {probability[0][1]*100:.2f}%")
    else:
        print(f"Result: LOW RISK (Non-Diabetic) - Confidence: {probability[0][0]*100:.2f}%")

predict_diabetes(
    pregnancies=6,
    glucose=148,
    blood_pressure=72,
    skin_thickness=35,
    insulin=0,
    bmi=33.6,
    diabetes_pedigree=0.627,
    age=50)

print('\npatient 2\n')
# Patient 2 — Low Risk (young, low glucose)
predict_diabetes(1, 85, 66, 29, 0, 26.6, 0.351, 31)
print('\npatient 3\n')
# Patient 3 — High Risk (high glucose, high BMI)
predict_diabetes(8, 183, 64, 0, 0, 23.3, 0.672, 32)
print('\npatient 4\n')
# Patient 3 — High Risk (high glucose, high BMI)
predict_diabetes(3, 148,70,32,88, 31.0, 0.45, 38) # borderline mmeans average