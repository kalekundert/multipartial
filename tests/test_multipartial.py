import parametrize_from_file as pff
from multipartial.array import get
from reprfunc import repr_from_init

class MockCallable:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __eq__(self, other):
        return (
                self.args == other.args and

                # Require that keyword arguments be in the same order.
                list(self.kwargs.items()) == list(other.kwargs.items())
        )

    __repr__ = repr_from_init

with_mock = pff.Namespace('from multipartial import *', g=MockCallable)

@pff.parametrize(
        schema=pff.error_or('expected'),
)
def test_multipartial(partials, expected, error):
    with error:
        partials = with_mock.eval(partials)
        expected = with_mock.eval(expected, keys=True)

        for ijk in expected:
            assert get(partials, ijk)() == expected[ijk]

def shape_from_ijks(ijks):
    return tuple(map(max, zip(*ijks)))

