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


Link to the [YouTube Playlist](https://www.youtube.com/playlist?list=PLXATvGH4cP8alRL4xChD37lMVz27JSLBm "Learn to program with python and industrial data") for creating this repo. spesifically [this video](https://www.youtube.com/watch?v=TyEjQ0o81yg&list=PLXATvGH4cP8alRL4xChD37lMVz27JSLBm&index=6 "050 Industrial data wrangling with Python Valve diagnostic case python project CDF")
