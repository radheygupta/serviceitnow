from django.test import TestCase
from .models import Features, Clients, ProductArea
from datetime import datetime


class FeatureTestCase(TestCase):
    def setUp(self):
        c1 = Clients.objects.create(name="ClientA", address="Noida", enddate="2019-12-02", status="A")
        p1 = ProductArea.objects.create(name="Billing", description="Billing", status="A")
        f1 = Features.objects.create(title="Test1", description="This is description", client=c1, priority=1,
                                     target_date="2018-12-02", product_area=p1, status="A")
        f2 = Features.objects.create(title="Test2", description="This is description", client=c1, priority=2,
                                     target_date="2018-12-02", product_area=p1, status="A")

    def test_feature_start_date(self):
        f1 = Features.objects.get(title="Test1")
        self.assertEqual(f1.start_date.strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
