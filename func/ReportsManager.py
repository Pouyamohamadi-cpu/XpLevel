class ReportWorker:
  def every(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
  def ancir(iterable):
    while True:
        for item in iterable:
            yield item
  def repeat_in(item, times=None):
    if times is None:
        while True:
            yield item
    else:
        for _ in range(times):
            yield item
  def chainer(*iterables):
    for it in iterables:
        for element in it:
            yield element
  def producter_build(*iterables):
    if not iterables:
        yield ()
    else:
        for item in iterables[0]:
            for prod in product(*iterables[1:]):
                yield (item,) + prod