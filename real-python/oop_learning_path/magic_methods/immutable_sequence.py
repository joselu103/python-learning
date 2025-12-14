class ImmutableSequence:
    def __init__(self, iterable):
        self._data = tuple(iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self._data)})"

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __reversed__(self):
        return self.__class__(reversed(self._data))

seq = ImmutableSequence([1, 2, 3, 4])
print(
    f"{seq=} | {seq[2]=} | {len(seq)=} | {(3 in seq)=} | {reversed(seq)} | {repr(reversed(seq))}"
)
seq[0] = 3