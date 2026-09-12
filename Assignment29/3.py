"""=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
"""

from typing import NamedTuple


# Define NamedTuple
class Patient(NamedTuple):
    patient_id: str
    patient_name: str
    age: int
    disease: str


# 1. Read N patient records
patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    data = input().split()

    patient_id = data[0]
    patient_name = data[1]
    age = int(data[2])
    disease = data[3]

    patient = Patient(patient_id, patient_name, age, disease)
    patients.append(patient)


# 2. Display all patient details
print("\nAll Patient Details:")

for patient in patients:
    print(patient.patient_id, patient.patient_name,
          patient.age, patient.disease)


# 3. Display patients whose age is above 60
print("\nPatients Above 60:")

for patient in patients:
    if patient.age > 60:
        print(patient.patient_id, patient.patient_name,
              patient.age, patient.disease)


# 4. Search patient using Patient ID
search_id = input("\nEnter Patient ID: ")

found = False

for patient in patients:
    if patient.patient_id == search_id:
        print("\nPatient Found:")
        print(patient.patient_id, patient.patient_name,
              patient.age, patient.disease)
        found = True

if found == False:
    print("\nPatient Not Found")


# 5. Count patients suffering from a particular disease
disease_name = input("\nEnter Disease: ")

count = 0

for patient in patients:
    if patient.disease == disease_name:
        count = count + 1

print("\nPatients with", disease_name + ":")
print(count)