from capitalize import capitalize  # type: ignore


if capitalize('hello') != "Hello":
    raise Exception('Function works wrong')


if capitalize('') != '':
    raise Exception('Function works wrong')


print('All tests are finished')
