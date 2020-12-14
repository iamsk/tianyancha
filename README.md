# tianyancha - 天眼查

Tianyancha SDK for python, which based on https://open.tianyancha.com/

## install

```shell script
pip install tianyancha
```

## Usage

All API supported! please visit **[Supported methods](API.md)** for more information!

```python
from tianyancha import Tianyancha

token = "TOKEN"
word = "北京百度网讯科技有限公司"
tyc = Tianyancha(token)
ret = tyc.search(word=word)  # Limited to use `keyword arguments`
```

```json
{
  "error_code": 0,
  "reason": "ok",
  "result": {
    "items": [
      {
        "regNumber": "110108002734659",
        "regStatus": "在业",
        "creditCode": "91110000802100433B",
        "estiblishTime": "2001-06-05 00:00:00.0",
        "regCapital": "1342128万人民币",
        "companyType": 1,
        "name": "<em>北京百度网讯科技有限公司</em>",
        "id": 22822,
        "orgNumber": "802100433",
        "type": 1,
        "base": "北京",
        "legalPersonName": "梁志祥"
      },
      {
        "regNumber": "440106000623068",
        "regStatus": "在业",
        "creditCode": "91440101675657502F",
        "estiblishTime": "2008-05-20 00:00:00.0",
        "regCapital": "-",
        "companyType": 1,
        "name": "<em>北京百度网讯科技有限公司</em>广州分公司",
        "id": 139572971,
        "orgNumber": "675657502",
        "type": 1,
        "base": "广东",
        "legalPersonName": "沈抖"
      },
      ...
    ],
    "total": 56
  }
}
```

## More usages

```python
ret = tyc.get('search/2.0', {'word': word})
```

## Tests

just run `pytest`

## Changelog

* 2020-12-11 0.1.2 path bugfix and generate documents for all methods 
* 2020-12-11 0.1.1 support all methods
* 2020-12-11 0.1.0 support basic search for tianyancha

## Refs

Official API Document: https://open.tianyancha.com/api_list
