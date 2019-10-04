class AtLookup(type):
    """Support custom class lookup."""

    def __contains__(self, name):
        """Find custom type attributes with ``@`` prefix."""
        if name.startswith('@'):
            return hasattr(self, f'_ld_{name[1:]}')
        return super().__contains__(name)

    def __getitem__(self, name):
        if name.startswith('@'):
            return getattr(self, f'_ld_{name[1:]}')
        return super().__getitem__(name)
        # return NS(self._ld_type + name)

    def __truediv__(self, name):
        return NS(f'{self._ld_type}{name}', final=True)

    def __eq__(self, other):
        if isinstance(other, str):
            return self._ld_type == other
        raise NotImplementedError


class Base:
    """Base class for linked data graph."""

    def __init_subclass__(cls, context=None, type=None, final=True, **kwargs):
        """Initialize context and type."""
        super().__init_subclass__(**kwargs)
        cls._ld_context = context or {}

        # for non-final annotations create new final NS / key
        cls._ld_context.update({
            key: value if value._ld_final else value / key
            for key, value in getattr(cls, '__annotations__', {}).items()
            if issubclass(value, Base)
        })

        cls._ld_type = type
        cls._ld_final = final
        return cls


class Node(Base, metaclass=AtLookup):
    pass


def NS(namespace, final=False):
    class Namespace(Node, type=namespace, final=final):

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(type=f'{namespace}{cls.__name__}', **kwargs)

    return Namespace
