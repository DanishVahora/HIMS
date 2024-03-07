from django.contrib import admin
from .models import Patient,Receptionist,Doctor,LabTechnician,Pharmacist,Administrator,Appointment,CaseRegister,Payment,FollowUp,Medicine,Test,Expense,Staff,Supply
# Register your models here.

admin.site.register(Patient)
admin.site.register(Receptionist)
admin.site.register(Doctor)
admin.site.register(LabTechnician)
admin.site.register(Pharmacist)
admin.site.register(Administrator)
admin.site.register(Appointment)
admin.site.register(CaseRegister)
admin.site.register(Payment)
admin.site.register(FollowUp)
admin.site.register(Medicine)
admin.site.register(Test)
admin.site.register(Expense)
admin.site.register(Staff)
admin.site.register(Supply)