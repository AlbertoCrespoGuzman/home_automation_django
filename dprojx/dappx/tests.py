from django.test import TestCase
from dappx.models import Object
from dappx.forms import ObjectForm

# Create your tests here.


class AnimalTestCase(TestCase):
    
    def test_valid_data(self):
        form = ObjectForm({
            'name': "Turanga Leela",
            'description': "Hi there",
            'activated': False,
            'slug': "url"
        }, entry=self.entry)
        self.assertTrue(form.is_valid())
        object = form.save()
        self.assertEqual(object.name, "Turanga Leela")
        self.assertEqual(object.description, "Hi there")
        self.assertEqual(object.activated, True)
        self.assertEqual(object.slug, "url")

    def test_blank_data(self):
        form = ObjectForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['required'],
            'description': ['required'],
            'activated': ['required'],
            'slug': ['required'],
        })