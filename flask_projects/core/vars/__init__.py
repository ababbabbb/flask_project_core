# 该包的内容仅用来提供存储/操作全局挂载变量的载体，
# 该载体的使用形式为委托到project对象当中，
# 之所以以对象委托到project当中的形式，是为了为后续的变量操作留下充足的空间，
# 防止一开始使用简单的数据结构导致后续的设计受限，同时也能够避免更换存储变量的形式变换后，影响过大