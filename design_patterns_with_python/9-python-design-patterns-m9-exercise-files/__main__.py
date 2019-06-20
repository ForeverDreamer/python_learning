# from before_null import MyObjectFactory

# if myobj is not None:
#     myobj.do_something('something')
# else:
#     print('Not doing anything.')


from myobjectfactory import MyObjectFactory

myobj = MyObjectFactory.create_object('myotherlass')
myobj.do_something('something')
