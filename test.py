from unittest import TestCase, main
import vclock


class FromSizeTest(TestCase):
    def test_returns_zeros_of_size(self):
        assert vclock.from_size(1) == (0,)
        assert vclock.from_size(2) == (0, 0)


class MergeTest(TestCase):
    def test_merge_selects_max(self):
        assert vclock.merge((1, 1), (1, 1)) == (1, 1)
        assert vclock.merge((0, 1), (1, 0)) == (1, 1)

    def test_merge_commutative(self):
        A = (1, 2)
        B = (2, 1)
        assert vclock.merge(A, B) == vclock.merge(B, A)

    def test_merge_associative(self):
        A = (1, 2)
        B = (2, 1)
        C = (3, 2)
        assert vclock.merge(vclock.merge(A, B), C) == \
                vclock.merge(A, vclock.merge(B, C))

    def test_merge_idempotent(self):
        A = (1, 2)
        B = (2, 1)
        merged = vclock.merge(A, B)
        assert vclock.merge(A, merged) == merged
        assert vclock.merge(B, merged) == merged


def gen_cmp_test(pairs, expected):
    def function(*_):
        for a, b in pairs:
            assert vclock.compare(a, b) == expected
    return function


class CompareTest(TestCase):
    LESSER = [
        [(1, 0), (2, 0)],
        [(1, 0), (2, 1)],
        [(1, 0), (1, 2)],
        [(1, 0), (1, 1)],
        ]

    test_compare_lesser  = gen_cmp_test(LESSER, -1)
    test_compare_greater = gen_cmp_test(map(reversed, LESSER), 1)
    test_compare_equal   = gen_cmp_test(
        [[(0, 0), (0, 0)],
         [(1, 2), (2, 1)]],
        0)


class SortTest(TestCase):
    def test_absolute_order(self):
        assert vclock.sort([(1, 1), (2, 3), (1, 2)]) == [
                (1, 1),
                (1, 2),
                (2, 3),
                ]

    def test_concurrent_order(self):
        assert vclock.sort([(1, 1), (1, 2), (2, 1), (2, 2)]) == [
                (1, 1),
                (1, 2),
                (2, 1),
                (2, 2),
                ]

class IsConcurrentTest(TestCase):
    def test_equal_not_concurrent(self):
        assert not vclock.is_concurrent((1, 0), (1, 0))
        assert not vclock.is_concurrent((0, 0), (0, 0))

    def test_not_equal_concurrent(self):
        assert vclock.is_concurrent((0, 1), (1, 0))
        assert vclock.is_concurrent((0, 2, 1), (2, 0, 1))


if __name__ == '__main__':
    main()
