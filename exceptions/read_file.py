def read_file(path: str) -> str:
  try:
     with open(path, "r") as f:
        return f.read()
  except (FileNotFoundError, UnicodeDecodeError):
     return None
     

if __name__ == "__main__":

   PATH = r"decorators\log.txt"

   response = read_file(PATH)

   print(response)