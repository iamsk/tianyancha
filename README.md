# tianyancha

Tianyancha SDK for python, which based on https://open.tianyancha.com/

## install

pip install tianyancha

## Usage

```python
from tianyancha import Tianyancha
token = "TOKEN"
word = "完美日记"

tyc = Tianyancha(token)
ret = tyc.search(word)
```

## More usages


```python
ret = tyc.get('/search/2.0', {'word': word})
```

API Mappings : https://open.tianyancha.com/api_list

## Tests

just run `pytest`
