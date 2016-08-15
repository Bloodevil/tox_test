# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
class TemplateKoreanTestCase(TestCase):
    def setUp(self):
        pass

    def test_test(self):
        self.assertEqual(1, 1)

    def test_korean_proofread(self):
        import korean
        result = korean.l10n.proofread(u"신예지는(은) 사람이다")
        self.assertEqual(result, u"신예지는 사람이다")

    def test_korean_proofread_false(self):
        import korean
        result = korean.l10n.proofread(u"신예지는(은) 사람이다")
        self.assertNotEqual(result, u"신예지은 사람이다")

    def test_korean_proofread_tag(self):
        from django.template import Context, Template
        rendered = Template(
            '{% load proofread %}'
            '{{ string | proofread }}'
            ).render(Context({
                'string':u'신예지는(은) 밥(를)을 먹었다.',
        }))
        self.assertEqual(rendered, u'신예지는 밥을 먹었다.')


