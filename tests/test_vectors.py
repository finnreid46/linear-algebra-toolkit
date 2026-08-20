import math
import pytest

from la_toolkit.vectors import (
    add_vectors,
    scalar_multiply,
    dot_product,
    vector_magnitude,
    normalise,
    angle_between,
)


# --------------------------------------------------
# Vector addition
# --------------------------------------------------

def test_add_vectors():
    assert add_vectors([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def test_add_vectors_negative_values():
    assert add_vectors([-2, 5, 1], [3, 0, -4]) == [1, 5, -3]


def test_add_vectors_dimension_mismatch():
    with pytest.raises(ValueError):
        add_vectors([1, 2], [1, 2, 3])


def test_add_vectors_does_not_mutate_inputs():
    a = [1, 2]
    b = [3, 4]

    add_vectors(a, b)

    assert a == [1, 2]
    assert b == [3, 4]


# --------------------------------------------------
# Scalar multiplication
# --------------------------------------------------

def test_scalar_multiply():
    assert scalar_multiply(3, [1, 2, 3]) == [3, 6, 9]


def test_scalar_multiply_fraction():
    assert scalar_multiply(-0.5, [2, -4]) == [-1.0, 2.0]


def test_scalar_multiply_zero():
    assert scalar_multiply(0, [3, 7, -2]) == [0, 0, 0]


# --------------------------------------------------
# Dot product
# --------------------------------------------------

def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def test_dot_product_perpendicular_vectors():
    assert dot_product([1, 2], [-2, 1]) == 0


def test_dot_product_dimension_mismatch():
    with pytest.raises(ValueError):
        dot_product([1, 2], [1, 2, 3])


# --------------------------------------------------
# Vector magnitude
# --------------------------------------------------

def test_vector_magnitude():
    assert vector_magnitude([3, 4]) == pytest.approx(5.0)


def test_vector_magnitude_three_dimensions():
    assert vector_magnitude([1, 2, 2]) == pytest.approx(3.0)


def test_zero_vector_magnitude():
    assert vector_magnitude([0, 0, 0]) == pytest.approx(0.0)


# --------------------------------------------------
# Normalisation
# --------------------------------------------------

def test_normalise():
    result = normalise([3, 4])

    assert result == pytest.approx([0.6, 0.8])


def test_normalised_vector_has_magnitude_one():
    result = normalise([2, -2, 1])

    assert vector_magnitude(result) == pytest.approx(1.0)


def test_normalise_zero_vector():
    with pytest.raises(ValueError):
        normalise([0, 0, 0])


# --------------------------------------------------
# Angle between vectors
# --------------------------------------------------

def test_angle_between_perpendicular_vectors():
    radians, degrees = angle_between([1, 0], [0, 1])

    assert radians == pytest.approx(math.pi / 2)
    assert degrees == pytest.approx(90.0)


def test_angle_between_parallel_vectors():
    radians, degrees = angle_between([1, 0], [1, 0])

    assert radians == pytest.approx(0.0)
    assert degrees == pytest.approx(0.0)


def test_angle_between_opposite_vectors():
    radians, degrees = angle_between([1, 0], [-1, 0])

    assert radians == pytest.approx(math.pi)
    assert degrees == pytest.approx(180.0)


def test_angle_between_zero_vector():
    with pytest.raises(ValueError):
        angle_between([0, 0], [1, 0])