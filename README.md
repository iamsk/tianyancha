# tianyancha - 天眼查

Tianyancha SDK for python, which based on https://open.tianyancha.com/

## install

```shell script
pip install tianyancha
```

## Usage

```python
from tianyancha import Tianyancha
token = "TOKEN"
word = "北京百度网讯科技有限公司"

tyc = Tianyancha(token)
ret = tyc.search(word)
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
ret = tyc.get('/search/2.0', {'word': word})
```

API Mappings : https://open.tianyancha.com/api_list

## Tests

just run `pytest`
