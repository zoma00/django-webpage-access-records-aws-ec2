from datetime import date

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from first_app.models import AccessRecord, Topic, WebPage


class AccessRecordModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(username='hazem-test')
        cls.topic = Topic.objects.create(top_name='Backend APIs')
        cls.webpage = WebPage.objects.create(
            topic=cls.topic,
            name='Django documentation',
            url='https://docs.djangoproject.com/',
        )
        cls.record = AccessRecord.objects.create(
            name=cls.webpage,
            date=date(2026, 7, 13),
            user=cls.user,
        )

    def test_model_string_representations(self):
        self.assertEqual(str(self.topic), 'Backend APIs')
        self.assertEqual(str(self.webpage), 'Django documentation')
        self.assertEqual(
            str(self.record),
            'hazem-test accessed Django documentation on 2026-07-13',
        )

    def test_topic_deletion_cascades_to_related_records(self):
        self.topic.delete()

        self.assertFalse(WebPage.objects.exists())
        self.assertFalse(AccessRecord.objects.exists())


class IndexViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create_user(username='reviewer')
        topic = Topic.objects.create(top_name='Cloud')
        older_page = WebPage.objects.create(
            topic=topic,
            name='Older page',
            url='https://example.com/older',
        )
        newer_page = WebPage.objects.create(
            topic=topic,
            name='Newer page',
            url='https://example.com/newer',
        )
        AccessRecord.objects.create(name=newer_page, date=date(2026, 7, 13), user=user)
        AccessRecord.objects.create(name=older_page, date=date(2026, 7, 12), user=user)

    def test_index_renders_access_records_in_date_order(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'first_app/index.html')
        self.assertQuerySetEqual(
            response.context['access_records'],
            AccessRecord.objects.order_by('date'),
        )
        self.assertContains(response, 'Older page')
        self.assertContains(response, 'reviewer')

    def test_index_handles_empty_database(self):
        AccessRecord.objects.all().delete()

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NO ACCESS RECORDS FOUND')
