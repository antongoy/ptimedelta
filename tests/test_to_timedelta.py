import unittest
import datetime

from ptimedelta import to_timedelta


class TestValidTimePeriods(unittest.TestCase):
    def test_period_with_minutes(self):
        self.assertEqual(to_timedelta("3m4s"), datetime.timedelta(minutes=3, seconds=4))

    def test_only_seconds(self):
        self.assertEqual(to_timedelta("43s"), datetime.timedelta(seconds=43))

    def test_period_with_milliseconds(self):
        self.assertEqual(
            to_timedelta("1h310ms"), datetime.timedelta(hours=1, milliseconds=310)
        )

    def test_float_and_int_values_in_period(self):
        self.assertEqual(
            to_timedelta("1m45.5s"), datetime.timedelta(minutes=1, seconds=45.5)
        )


class TestInvalidTimePeriods(unittest.TestCase):
    def test_none_instead_of_string(self):
        with self.assertRaises(TypeError):
            to_timedelta(None)

    def test_int_instead_of_string(self):
        with self.assertRaises(TypeError):
            to_timedelta(60)

    def test_zero(self):
        with self.assertRaises(TypeError):
            to_timedelta(0)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            to_timedelta("")

    def test_only_seconds_specifier(self):
        with self.assertRaises(ValueError):
            to_timedelta("s")

    def test_just_float_without_period_specifier(self):
        with self.assertRaises(ValueError):
            to_timedelta("40.9")

    def test_specify_seconds_before_minutes(self):
        with self.assertRaises(ValueError):
            to_timedelta("34s1m")

    def test_random_string(self):
        with self.assertRaises(ValueError):
            to_timedelta("its just string")
