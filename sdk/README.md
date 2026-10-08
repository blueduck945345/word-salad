To install:

Run from this directory.

```
pip install -e .
```

Then iniitalize:

```
from word_salad_api_client import WordSaladClient

client = WordSaladClient()

client.load('test1\ntest2\ntest3')

## {'message': 'Text processed'}

client.sample(size=3)

## ['test1', 'test2', 'test3'] -- results of previous load

client.sample(size=3)

## [] -- subsequent attempt will have exhausted all lines

```