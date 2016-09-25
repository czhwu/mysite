from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Qusetions


# Create your tests here.
class QuestionMethonTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for question whose pub_date is in the future.
        :return:
        """
        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Qusetions(pub_date=time)
        self.assertEqual(future_question.was_published_recentlsy(), False)