from selection_sort import SelectionSortAlgorithm
from insertion_sort import InsertionSortAlgorithm
from bubble_sort import BubbleSortAlgorithm
from merge_sort import MergeSortAlgorithm
from quick_sort import QuickSortAlgorithm
from heap_sort import HeapSortAlgorithm
from sorting_benchmark import SortingBenchmark


def run_benchmark_for_size(input_size):
    absolute_value_comparator = lambda x, y: x < y

    algorithms = [SelectionSortAlgorithm(absolute_value_comparator),
                  InsertionSortAlgorithm(absolute_value_comparator),
                  BubbleSortAlgorithm(absolute_value_comparator),
                  MergeSortAlgorithm(absolute_value_comparator),
                  QuickSortAlgorithm(absolute_value_comparator),
                  HeapSortAlgorithm(absolute_value_comparator)]

    print "Running benchmark for an array with {input_size} items.".format(input_size=input_size)

    sorting_benchmark = SortingBenchmark(input_size=input_size)
    for algorithm in algorithms:
        algorithm_name = algorithm.__class__.__name__.ljust(25)
        time, comparisons, exchanges = sorting_benchmark.run(algorithm)
        print "{algorithm_name}:\t{comparisons} comparisons\t{exchanges} exchanges\t{time} sec.".format(**locals())

    print ""


def main():
    run_benchmark_for_size(10)
    run_benchmark_for_size(100)
    run_benchmark_for_size(1000)


if __name__ == "__main__":
    main()
