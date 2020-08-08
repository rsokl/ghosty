# Fail Cases for Ghostwriter  👻

```shell
hypothesis write --idempotent ghosty.identity
```

```python
# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import ghosty
from hypothesis import given, strategies as st


@given(x=st.builds(Person))  # note: raises ImportError
def test_idempotent_identity(x):
    result = ghosty.identity(x=x)
    repeat = ghosty.identity(x=result)
    assert result == repeat, (result, repeat)

```
