"""
.. module:: algorithms
    :synopsis: Various audio algorithms

.. moduleauthor:: Steve Rubin <srubin@cs.berkeley.edu>

"""

# from .composition import Composition
from .novelty import novelty
from .build_table import build_table
from .build_table_mem_efficient import build_table as build_table_mem_efficient
import retarget