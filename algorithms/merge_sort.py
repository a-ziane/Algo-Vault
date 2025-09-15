from algorithms.base import SortAlgorithm

class MergeSort(SortAlgorithm):
    def sort(self, arr):
        data = arr.copy()
        self._merge_sort(data)
        return data

    def _merge_sort(self, data):
        if len(data) > 1:
            mid = len(data)//2
            L = data[:mid]
            R = data[mid:]

            self._merge_sort(L)
            self._merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1
