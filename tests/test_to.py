import unittest
import datetime

from ptimedelta.to import to_timedelta, to_seconds, to_milliseconds


class TestToTimedelta(unittest.TestCase):
    def test_period_with_minutes(self):
        self.assertEqual(to_timedelta("3m4s"), datetime.timedelta(minutes=3, seconds=4))

    def test_period_with_days(self):
        self.assertEqual(
            to_timedelta("5day44s"), datetime.timedelta(days=5, seconds=44)
        )

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


class TestToSeconds(unittest.TestCase):
    def test_to_seconds(self):
        self.assertEqual(to_seconds("12min"), 720.0)

    def test_to_seconds_using_as_int(self):
        self.assertEqual(to_seconds("1m45ms", as_int=True), 60)


class TestToMilliseconds(unittest.TestCase):
    def test_to_milliseconds(self):
        self.assertEqual(to_milliseconds("8sec4msec"), 8004.0)
