from multipartial.require import *
import parametrize_from_file as pff

with_py = pff.Namespace()

@pff.parametrize(
        schema=[
            pff.cast(
                x=with_py.eval,
                y=with_py.eval,
                rows=int,
                cols=int,
            ),
            pff.defaults(rows=None, cols=None),
            pff.error_or('y'),
        ],
)
def test_require_grid(x, y, rows, cols, error):
    with error:
        assert require_grid(x, rows=rows, cols=cols) == y

