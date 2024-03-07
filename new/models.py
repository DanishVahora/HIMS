from django.db import models


# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_info = models.CharField(max_length=100)
    medical_history = models.TextField()


class Receptionist(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    tasks = models.TextField()


class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True, max_length=50)
    specialization = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class LabTechnician(models.Model):
    technician_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)


class Pharmacist(models.Model):
    pharmacist_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    inventory = models.TextField()


class Administrator(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    managerial_tasks = models.TextField()


class Appointment(models.Model):
    appointment_id = models.CharField(primary_key=True, max_length=50)
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class CaseRegister(models.Model):
    case_id = models.CharField(primary_key=True, max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    details = models.TextField()


class Payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   
class FollowUp(models.Model):
    followup_id = models.CharField(primary_key=True, max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    instructions = models.TextField()


class Medicine(models.Model):
    medicine_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    stock = models.IntegerField()


class Test(models.Model):
    test_id = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Expense(models.Model):
    expense_id = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class Staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


class Supply(models.Model):
    supply_id = models.CharField(primary_key=True, max_length=50)
    supply_type = models.CharField(max_length=100)
    quantity = models.IntegerField()

