class SortAlgorithm:
    def sort(self,  arr):
        raise NotImplementedError("Subclasses must implement this method")


    def name(self):
        return self.__class__.__name__