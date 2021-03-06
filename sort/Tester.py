from QuickSort import quick_sort
from MergeSort import merge_sort
from BubbleSort import bubble_sort
from InsertSort import insert_sort
from SelectSort import select_sort
from ShellSort import shell_sort
from HeapSort import heap_sort


def test(sort_fn, reverse=False):
    print "sort algorithm:", sort_fn.__name__
    print "doc:", sort_fn.__doc__
    print
    test_cases = [None, [], [1], [1, 2, 3], [3, 2, 1], [5, 7, 1, 3, -2], [5, 1, 7, -2, 1, 3, -2, 8]]
    for case in test_cases:
        print "test case:", case
        print "after sort:", sort_fn(case, reverse)
        print

if __name__ == "__main__":
    # test(quick_sort, True)
    # test(merge_sort, True)
    # test(bubble_sort, True)
    # test(insert_sort, True)
    # test(select_sort, True)
    # test(shell_sort, True)
    test(heap_sort, True)
