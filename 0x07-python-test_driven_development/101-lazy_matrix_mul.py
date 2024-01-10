#!/usr/bin/python3
"""
module lazy_matrix_mul
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiplie m_a and m_b using matmul
    return result
    """
    if not all(isinstance(row, list) for row in m_a) or not \
     all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b \
         must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    return numpy.matmul(m_a, m_b)
