from django.db import models


class Clients(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "clients"

    def __str__(self):
        return self.name


class ProductArea(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Features(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('D', 'Done'),
        ('C', 'Cancelled'),
    )

    PRIORITY_CHOICES = tuple((i, i) for i in range(0, 16))

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)  # 0 means priority is not set
    start_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField()
    product_area = models.ForeignKey(ProductArea,  null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name_plural = "features"

    def __str__(self):
        return self.title
