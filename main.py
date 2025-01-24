import cmath
import math
#Завдання 1
age = int(input("Введіть свій вік: "))
days = age * 365
print(f"Вік у днях: {days} ")
#Завдання 2
mass = int(input("Введіть свою масу: "))
acceleration = int(input("Введіть прискорення(м/с^2): "))
force = mass * acceleration
print(f"Сила, що прикладена до тіла: {force}")
#Завдання 3
a = float(input("Введіть коефіцієнт а: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))
discriminator = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(discriminator)) / (2*a)
root2 = (-b - cmath.sqrt(discriminator)) / (2*a)
print(f"Корені рівняння: {root1}, {root2}")
#Завдання 4
def heron(a, b, c):
  s = (a + b + c) / 2
  return math.sqrt(s * (s - a) * (s - b) * (s - c))
def by_height(base, height):
  return 0.5 * base * height
def by_angle(a,b,angle):
  return 0.5 * a * b * math.sin(math.radians(angle))
print("Виберіть метод обчислення площі трикутника: ")
print("1. По формулі Герона")
print("2. За висотою")
print("3. За двома сторонами та кутом між ними")
choice = int(input("Ваш вибір: "))
if choice == 1:
  a = float(input("Введіть сторону a: "))
  b = float(input("Введіть сторону b: "))
  c = float(input("Введіть сторону c: "))
  print(f"Площа трикутника: {heron(a, b, c)}")
if choice == 2:
  base = float(input("Введіть основу трикутника: "))
  height = float(input("Введіть висоту трикутника: "))
  print(f"Площа трикутника: {by_height(base, height)}")
if choice == 3:
  a = float(input("Введіть сторону a: "))
  b = float(input("Введіть сторону b: "))
  angle = float(input("Введіть кут між сторонами: "))
  print(f"Площа трикутника: {by_angle(a, b, angle)}")
#Завдання 5
nums = [float(input("Введіть число: ")) for _ in range(3)]
print(f"Найменше число: {min(nums)}")
print(f"Найбільше число: {max(nums)}")
#Завдання 6
N = int(input("Введіть N: "))
if 1 < N and N < 100:
  total =   N * (N + 1) // 2
  print(f"Сума перших {N} натуральних чисел: {total}")
else:
  print("N повинно бути від 1 до 100")
#Завдання 7
def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True
def primes_in_range(start, end):
  return [num for num in range(start, end + 1) if is_prime(num)]
start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
print(f"Прості числа у вказаному діапазоні: {primes_in_range(start, end)}")
#Завдання 8
def previous_prime(num):
  num -= 1
  while num > 1:
    if is_prime(num):
      return num
    num -= 1
  return None
num = int(input("Введіть число: "))
print(f"Перше просте число перед {num}: {previous_prime(num)}")