from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField


class CommonFields(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = PhoneNumberField(blank=True)
    dateOfBirth = models.DateField()
    address = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    ideaDescription = models.TextField()
    gen = (
        ('Male',"Male"),
        ('Female', "Female"),
        ('Prefer Not to Say', "Prefer Not to Say"),
    )
    gender = models.CharField(max_length=20, choices=gen, default="None")

    cat = (
        ('General',"General"),
        ('OBC', "OBC"),
        ('SC', "SC"),
        ('ST', "ST"),
    )
    category = models.CharField(max_length=10, choices=cat, default='None')


    resume = models.FileField(upload_to='resumes/')
    conceptNote = models.FileField(upload_to='notes/')
    aspectNote = models.FileField(upload_to='notes/')

    choice = (
        ('Yes','Yes'),
        ('No','No'),
    )

    previousRecipient = models.CharField(max_length=10, choices= choice)
    fullCommitment = models.CharField(max_length=10, choices= choice)
    noOtherFellowship = models.CharField(max_length=10, choices= choice)
    businessCommitment = models.CharField(max_length=10, choices= choice)
    notBeneficiary = models.CharField(max_length=10, choices= choice)
    registerPEP = models.CharField(max_length=10, choices= choice)

    class Meta:
        abstract = True

        

class NidhiEIR(CommonFields):
    
    def __str__(self):
        return self.name


class NidhiPrayas(CommonFields):
    applicantImage = models.ImageField(upload_to="applicantImage/")
    fatherName = models.CharField(max_length=50)
    whatsappNumber = PhoneNumberField(blank=True)
    addressDocument = models.FileField(upload_to="address/")
    panNumber = models.CharField(max_length=10, unique=True)
    aadharNumber = models.CharField(max_length=12, unique=True)
    workingPrinciple = models.TextField()
    annualIncome = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')

    teammates = (
        ('None', "None"),
        ('Less than 3', "Less than 3"),
        ('More than 3', "More than 3"),
    )

    teamMembers = models.CharField(max_length=20, choices=teammates)

    choice = (
        ('Yes','Yes'),
        ('No','No'),
    )

    innovator = models.CharField(max_length=10, choices=choice)
    ownVenture = models.CharField(max_length=10, choices=choice)


    def __str__(self):
        return self.name
    

class TideEIR(CommonFields):
    whatsappNumber = PhoneNumberField(blank = True)
    instituteName = models.TextField()
    applicantImage = models.ImageField(upload_to='applicantImage/')
    aadharImage = models.ImageField(upload_to='applicantImage/')
    panImage = models.ImageField(upload_to='applicantImage/')
    teamMemberName = models.CharField(max_length=50)
    teamMemberInstituteName = models.TextField()
    teamMemberEducation = models.TextField()
    teamMemberExperience = models.TextField()
    projectTitle = models.CharField(max_length=100)
    techStack = models.TextField()
    projectVideo = models.FileField(upload_to="projectVideo/")
    companyName = models.CharField(max_length=100)
    incorporationDate = models.DateField()
    companyDescription = models.TextField()

    status = (
        ('Idea', "Idea"),
        ('POC', "POC"),
        ('Ready to commercialize', "Ready to commercialize"),
        ('Prototype', "PROTOTYPE"),
        ('Ready market product', "Ready Market Product")
    )
    projectStatus = models.CharField(max_length=40, choices=status, default='None')

    def __str__(self):
        return self.name
    

class TideGrant(TideEIR):
    panNumber = models.CharField(max_length=10, unique=True)
    aadharNumber = models.CharField(max_length=12, unique=True)
    applicantProfession = models.TextField()
    annualIncome = models.CharField(max_length=10)
    innovationBeneficiary = models.TextField()
    prototypeCostDetails = models.TextField()
    projectPeriod = models.TextField()
    activities = models.TextField()
    monitrableMilestones = models.TextField()
    duration = models.TextField()
    financialSupportStatus = models.TextField()

    def __str__(self):
        return self.name