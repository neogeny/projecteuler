#!/usr/bin/env python
"""
Solutions to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/
"""
from pathlib import Path
from timeit import timeit

import sys
sys.path.insert(0, 'solutions')


def test_assertions_on():
    try:
        assert False
        print('Please turn on assertions!')
        sys.exit()
    except AssertionError:
        pass


def timed_test(name):
    return timeit(
        'test();run()',
        'from ' + name + ' import test, run',
        number=1
    )


def main():
    test_assertions_on()

    total_time = 0
    success_count = 0
    failed = 0
    modules = [p.stem for p in Path().glob('solutions/euler*.py')]
    for name in modules:
        print('%-40s ' % name, end='')
        sys.stdout.flush()
        try:
            time = timed_test(name)
            print(round(time, 3))
            total_time += time
            success_count += 1
        except KeyboardInterrupt:
            break
        except ImportError as e:
            print('untested', e)
        except AssertionError as ae:
            failed += 1
            print('FAILED!')
        except Exception as e:
            failed += 1
            print(e)

    print()
    print(
        'total time for', success_count, 'problems,',
        failed, 'failed,',
        'is:', round(total_time, 3)
    )


if __name__ == '__main__':
    main()
