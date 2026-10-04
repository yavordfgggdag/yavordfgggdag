import unittest
from datetime import date, timedelta
from update_metrics import stats, CalendarParser

class MetricsTests(unittest.TestCase):
    today = date(2026, 10, 5)
    def series(self, values):
        return [{'date': (self.today-timedelta(days=len(values)-1-i)).isoformat(), 'count':n} for i,n in enumerate(values)]
    def test_unfinished_today_keeps_yesterday_streak(self):
        self.assertEqual(stats(self.series([1,2,0]),self.today)['current'],2)
    def test_gap_breaks_streak(self):
        self.assertEqual(stats(self.series([1,0,0]),self.today)['current'],0)
    def test_longest_is_limited_to_calendar(self):
        result=stats(self.series([1,1,0,1,1,1]),self.today)
        self.assertEqual(result['longest'],3)
        self.assertEqual(result['active'],5)
        self.assertEqual(result['total'],5)
    def test_no_activity_has_no_last_day(self):
        self.assertIsNone(stats(self.series([0,0]),self.today)['last'])
    def test_incomplete_source_fails_instead_of_zeroing(self):
        p=CalendarParser();p.feed('<html>Rate limited</html>')
        with self.assertRaises(ValueError): p.days()

if __name__=='__main__':unittest.main()
