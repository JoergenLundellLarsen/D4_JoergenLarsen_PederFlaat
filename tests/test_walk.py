import random

from walking_home.walk import step


def test_step_returns_valid_values():
    random.seed(123)
    dest, steps, t = step()

    assert dest in {"Pentagon", "Kaia"}
    assert isinstance(steps, int) and steps >= 0
    assert isinstance(t, int) and t > 0


def test_always_pentagon_when_only_pentagon_accepts():
    random.seed(0)
    outcomes = [step(p_pentagon=1.0, p_kaia=0.0)[0] for _ in range(50)]
    assert set(outcomes) == {"Pentagon"}


def test_always_kaia_when_only_kaia_accepts():
    random.seed(0)
    outcomes = [step(p_pentagon=0.0, p_kaia=1.0)[0] for _ in range(50)]
    assert set(outcomes) == {"Kaia"}

