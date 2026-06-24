from importlib import import_module
from pathlib import Path

import pytest

SOLUTIONS_DIR = Path(__file__).resolve().parent.parent / 'solutions'


def all_solution_modules():
    return [path.stem for path in sorted(SOLUTIONS_DIR.glob('euler*.py'))]


@pytest.mark.parametrize('module_name', all_solution_modules())
def test_solution(module_name):
    mod = import_module(module_name)
    mod.run()
