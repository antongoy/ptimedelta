import random
import argparse

from collections import namedtuple

from pytictoc import TicToc

import ptimedelta as ptd


Specifier = namedtuple("Specifier", field_names=["id", "name"])

MAX_NUMBER = 1000
NDIGITS = (None, 1, 2, 3)

DAY = Specifier(id=1, name="d")
HOUR = Specifier(id=2, name="h")
MINUTE = Specifier(id=3, name="m")
SECOND = Specifier(id=4, name="s")
MILLISECOND = Specifier(id=5, name="ms")


def gen_number():
    ndigits = random.choice(NDIGITS)
    return round(random.uniform(0, MAX_NUMBER), ndigits=ndigits)


def gen_time_period():
    k = random.randint(1, 5)
    specifiers = random.sample([DAY, HOUR, MINUTE, SECOND, MILLISECOND], k=k)
    sorted_specifiers = sorted(specifiers, key=lambda specifier: specifier.id)

    return "".join(
        "%s%s" % (gen_number(), specifier.name) for specifier in sorted_specifiers
    )


def compute_avg(iterable):
    return sum(iterable) / len(iterable)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--random-state", type=int, default=None)
    parser.add_argument("--n", type=int, default=100)

    args = parser.parse_args()

    random.seed(args.random_state)

    timer = TicToc()

    avgs = []

    for _ in range(100):

        elapsed_times = []

        for _ in range(args.n):
            value = gen_time_period()

            timer.tic()
            ptd.to_timedelta(value)

            elapsed_times.append(timer.tocvalue(restart=True))

        avgs.append(compute_avg(elapsed_times))

    final_avg = round(compute_avg(avgs) * ptd.MS_IN_SEC, ndigits=4)

    print("Elapsed time: %sms" % final_avg)


if __name__ == "__main__":
    main()
