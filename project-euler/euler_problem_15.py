"""The answer  to this problem is discussed in the help notes"""

from itertools import combinations
from helpers import combination_value

def number_of_paths_thru_grid(grid_size=2):
    """Number of paths to traverse"""
    return combination_value(grid_size*2, grid_size)

def visualize_paths(grid_size):
    """Visualize the paths"""
    number_of_right_motions = 'r' * grid_size
    number_of_downward_motions = 'd' * grid_size

    path_from_left_edge_to_bottom = number_of_downward_motions + number_of_right_motions

    path = combinations(path_from_left_edge_to_bottom, grid_size)
    return path
