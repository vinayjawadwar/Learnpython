
#print(__name__)                         # value for name is main

import var                              # print name of module because it imported from file var

print("Demo says :",__name__)

# it doesn't executing main() from var file directly only execute after calling , used when you don't want to import all program

print(var.main())

# if we use from var import * means all function then not need to typr var.function only type main()



from var import *
print(main())