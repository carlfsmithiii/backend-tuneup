#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Carl Smith"


def profile(func):
    """A function that can be used as a decorator to meausre performance"""
    import cProfile
    import pstats
    # import io

    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(profiler).sort_stats(sortby)
        ps.print_stats()

        return result
    return wrapper


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().lower().splitlines()


def is_duplicate(needle, haystack):
    """Case insensitive search within a list"""
    return needle in haystack


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    import timeit
    t = timeit.Timer(setup='pass',
                     stmt="find_duplicate_movies('movies.txt')",
                     globals=globals())
    result = t.repeat(repeat=7, number=3)
    print("minimum of average performances: " + str(min(result)))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    # timeit_helper()
