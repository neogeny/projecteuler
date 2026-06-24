# Changelog

## [1.0.0] - 2026-06-24

### Changed

- Migrated from Python 2.7 to Python 3.12
- Replaced all `print` statements with `print()` function calls
- Replaced `xrange()` with `range()`
- Replaced `itertools.izip()` with built-in `zip()`
- Replaced `.next()` method calls with `next()` built-in function
- Replaced `fractions.gcd` with `math.gcd`
- Updated `solutions/` path in README from `src/eulerXXX.py`
- Removed `fractions` import from `factorization.py`
- Updated test runner and Makefile to use `python3`
- Renamed all bare-number euler solution modules to descriptive names (e.g., `euler009.py` → `euler009_special_pythagorean_triplet.py`)
- Updated `.settings/org.eclipse.core.resources.prefs` to reflect current filenames and `solutions/` path

### Fixed

- Updated `euler056_powerful_digit_sum.py`, `euler057_square_root_convergents.py`, `euler058_spiral_primes.py`, `euler059_xor_decryption.py`, `euler067_maximum_path_sum_II.py` for Python 3 syntax
- Updated `factorization.py` to use `math.gcd` (removed in Python 3.9 from `fractions`)
- Fixed `primality.py:is_prime()` to check divisors only up to `√n` instead of `n`, fixing euler058 performance
- Renamed `euler052_permuted multiples.py` to `euler052_permuted_multiples.py` (space in filename)
- Added missing `run()` function to `euler067_maximum_path_sum_II.py`
