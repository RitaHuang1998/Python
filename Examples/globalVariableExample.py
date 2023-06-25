# 2023/06/26 
# Global Variable Example

# Global name = Rita
name = 'Rita'

def main():
  example()



def example():
    # 👇️ mark global
    global name # 👉️ error: local variable 'name' referenced before assignment

    #Global name = Rita
    print(name) # 👉️ 'Rita'

    name = 'Rong'

    #Global name = Rong
    print(name) # 👉️ 'Rong'

# Run first
if __name__ == "__main__":
  # Call "def main()"
  main()