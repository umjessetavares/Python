num = [3, 5, 7, 15, 33, 10]
friends = ['João', 'Maria', 'José', 'Adriana', 'Julia', 'Marcos']

friends.extend(num)
print(friends)

friends.append('Maria')
print(friends)

friends.insert(1, 'Caio')
print(friends)

friends.remove('Maria')
print(friends)

# Essa funão remove
friends.pop(2)
print(friends)

# Verficar se um item existe ou não na lista
num = [3, 5, 7, 15, 33, 10]
friends = ['João', 'Maria', 'José', 'Adriana', 'Julia', 'Marcos']
print(friends.index('Maria'))

# Contar
num = [3, 5, 7, 15, 33, 10]
friends = ['João', 'Maria', 'José', 'Maria', 'Julia', 'Marcos']
print(friends.count('Maria'))

# Organizar
num = [3, 5, 7, 15, 33, 10]
friends = ['João', 'Maria', 'José', 'Maria', 'Julia', 'Marcos']
friends.sort()
print(friends)