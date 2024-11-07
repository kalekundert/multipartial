from multipartial.array import *
import parametrize_from_file as pff

with_py = pff.Namespace()

@pff.parametrize(
        schema=pff.cast(
            shape=with_py.eval,
            expected=with_py.eval,
        ),
)
def test_make_array(shape, expected):
    x = make_array(shape, lambda y: y)
    assert x == expected

@pff.parametrize(
        schema=pff.cast(
            array=with_py.eval,
            expected=with_py.eval(keys=True),
        )
)
def test_get(array, expected):
    for ijk in expected:
        assert get(array, ijk) == expected[ijk]
