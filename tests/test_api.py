import os
from dotenv import load_dotenv

from tianyancha import Tianyancha

load_dotenv()

tyc = Tianyancha(os.getenv("TYC_TOKEN"))


def test_dynamic_method():
    # name = '广东航鑫科技股份公司'
    # ret = tyc.get('ic/changeinfo/2.0', {'keyword': name})
    assert hasattr(tyc, 'ic_changeinfo') == True
