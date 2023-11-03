from question2 import run_swapper 

def test_run_swapper():
  assert run_swapper(
    [ ("a", "b"), ("c", "d"), ("e", "f") ]
  ) == [ ("b", "a"), ("d", "c"), ("f", "e")]

  assert run_swapper(
    [ (1, 1), ("foo", "bar"), (13, "cows"), (None, "Some") ]
  ) == [ (1, 1), ("bar", "foo"), ("cows", 13), ("Some", None) ]
  
  assert run_swapper(
    [ (1, 1, 1), ("foo", "bar", "foo"), (13, "cows", "dogs"), (None, "Some") ]
  ) == [ (1, 1,1), ("foo", "bar", "foo"), ("dogs", "cows", 13), ("Some", None) ]