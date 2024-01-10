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
    return numpy.matmul(m_a, m_b)
