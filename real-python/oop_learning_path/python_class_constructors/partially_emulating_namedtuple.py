from operator import itemgetter

def named_tuple_factory(type_name: str, *fields: str):
    num_fields = len(fields)

    class NamedTuple(tuple):
        __slots__ = ()

        def __new__(cls, *args):
            if len(args) != num_fields:
                raise TypeError(
                    f"{type_name} class expects {num_fields} arguments, {len(args)}"
                    f"were given."
                )
            cls.__name__ = type_name
            print(f"{cls=}\n{type(cls)=}")

            for index, field_name in enumerate(fields):
                setattr(cls, field_name, property(itemgetter(index)))

            print(f"{super()=}")
            return super().__new__(cls, args)

        def __repr__(self):
            return f"{self.__class__.__name__}({', '.join(repr(arg) for arg in self)})"

    return NamedTuple
