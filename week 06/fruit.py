def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f"reversed: {fruit_list}")
  fruit_list.append("orange")
  print(f"appended 'orange': {fruit_list}")
  
  index_apple = fruit_list.index("apple")
  fruit_list.insert(index_apple, "cherry")
  print(f"inserted 'cherry' before 'apple': {fruit_list}")

  fruit_list.remove("banana")
  print(f"removed 'banana': {fruit_list}")

  last_item = fruit_list.pop()
  print(f"popped last item '{last_item}': {fruit_list}")

  fruit_list.sort()
  print(f"sorted: {fruit_list}")

  fruit_list.clear()
  print(f"cleared: {fruit_list}")

main()
