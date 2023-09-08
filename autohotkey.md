## Autohotkey 1 Script:

```
#Home::
dir    = path\to\your\python\script\
script  = %dir%\sceneSwapper.py
F3::Run, %ComSpec% /k python "%script%" ,,hide
```

## Autohotkey 2 Script:
```
#Home::
dir := "path\to\your\python\script\"
script := dir . "sceneSwapper.py"
F3::Run, % ComSpec " /k python " script ,, Hide
```
