# Valve diagnostic case with CDF data


Set up python enviroment
```bash
pip install poetry
poetry config virtualenv.in-project true
poetry install
```

selected python interpeter and ipynb kernel.

open up a notebook and excec:

```python
from cdf import client
from valve_diagnostics import valve_diagnostic
valve_diagnostic(4146236330407219,client)
```

