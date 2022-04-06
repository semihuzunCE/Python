# paketimizde her modul ve alt modullerin içerisine __init__.py dosyası oluşturduk içi boş bile olsa pythonun bunu modül oldugunu anlaması için bunu yapmamız lazım
from semihmodul import ornekfonk
from OnemliPackage import anaModul
from OnemliPackage.SubPackage import altModul
ornekfonk()
anaModul.anaFonksiyon()
altModul.altFonksiyon()