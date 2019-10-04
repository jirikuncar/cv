class AtLookup(type):
    """Support custom class lookup."""

    def __contains__(self, name):
        """Find custom type attributes with ``@`` prefix."""
        if name.startswith('@'):
            return hasattr(self, f'_ld_{name[1:]}')
        return super().__contains__(name)


class Node(metaclass=AtLookup):
    """Base node for linked data graph."""

    def __init_subclass__(cls, context=None, type=None, **kwargs):
        """Initialize context and type."""
        super().__init_subclass__(**kwargs)
        cls._ld_context = context or {}
        cls._ld_type = type
        return cls
