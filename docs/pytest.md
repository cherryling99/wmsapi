# Pytest

測試的水很深，要做到單元測試是很不簡單的事。基礎的知識請參閱這一篇：\
https://iter01.com/504335.html


安裝套件，我另外多安裝pytest-sugar，這可以讓輸出好看一點\
- pip install pytest 
- pip install pytest-sugar

## 執行測試
在terminal執行： \
```
pytest
```

## 測試忽略警告
在terminal執行：
```
pytest --disable-warnings
```

# coverage
https://coverage.readthedocs.io/en/6.3.2/

coverage 6.3.2

```
pip install coverage
```

```
coverage run -m pytest
coverage report -m
coverage html
```
Wrote HTML report to htmlcov\index.html