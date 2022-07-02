import attr

def DataClassWrapper(cls):

    @attr.define(frozen=True)
    class Wrapper(cls):
        def __init__(self):
            super().__init__()

        @staticmethod
        def Create():
            return cls()

        # def __repr__(self):
        #     return

    return Wrapper