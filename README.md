
# 生成 requirements.txt

```
pip freeze > requirements.txt
```

# 打包

```
pip install -U nuitka --user
```

```
python -m nuitka --lto=no --onefile --standalone main.py
```
