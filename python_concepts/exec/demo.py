import sys

exec('foobar=123')
print foobar


# return is collected within global
g = {'age': 1 }#, '__builtins__': {}}
exec('sample = age + 1', g)

print g['sample']
print g['__builtins__']
print sys.modules[__name__]


# local is used to collect the output
local = {}

exec('test = age**2', {'age': 2}, local)
print local