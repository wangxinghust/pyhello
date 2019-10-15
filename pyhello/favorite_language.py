# 有序字典
from collections import OrderedDict

favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='golong'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title())