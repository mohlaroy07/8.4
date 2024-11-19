from django.db import models


class Klass(models.Model):
    nomi = models.CharField(max_length=244)
    narxi = models.IntegerField()

    def __str__(self) -> str:
        return self.nomi
    

class Mehmonxona(models.Model):
    nomi = models.CharField(max_length=244)
    yulduzlar_soni = models.IntegerField()
    narxi = models.IntegerField()   


    def __str__(self) -> str:
        return self.nomi
    
        
class Travel(models.Model):
    nomi = models.CharField(max_length=244)
    izoh = models.CharField(max_length=244)
    muddati = models.DateTimeField(auto_created=True)
    narxi = models.IntegerField()
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    mehmonxona = models.ForeignKey(Mehmonxona, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nomi