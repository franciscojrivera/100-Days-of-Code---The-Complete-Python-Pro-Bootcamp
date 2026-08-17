enemies = 1

#enemies will not change outside this loop
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

# will print 2 then 1
increase_enemies()
print(f"enemies outside function: {enemies}")
