import gc
print(gc.isenabled())
#disable gc
gc.disable()
print('Garbage Collector is disable: {}'.format(gc.isenabled()))
gc.enable()
print('Garbage Collector is enable: {}'.format(gc.isenabled()))
