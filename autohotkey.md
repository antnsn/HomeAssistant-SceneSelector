## Autohotkey 1 Script:

```
#Home:: ; Press Win+Home to run the Python script using AutoHotkey
dir    = path\to\your\python\script\ 
script  = %dir%\sceneSwapper.py
F3::Run, %ComSpec% /k python "%script%" ,,hide
```

## Autohotkey 2 Script:
```
#Home:: ; Press Win+Home to run the Python script using AutoHotkey
dir := "path\to\your\python\script\"
script := dir . "sceneSwapper.py"
F3::Run, % ComSpec " /k python " script ,, Hide
```
