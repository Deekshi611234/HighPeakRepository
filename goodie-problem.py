#%%
def find_goodies(products, number_of_employees):
    products = sorted(products,key = lambda el:el[1])
    min_diff = float("inf")
    indices = (0,number_of_employees-1)
    for ind in range(len(products)-number_of_employees+1):
        curr_diff = products[ind+number_of_employees-1][1] - products[ind][1]
        if curr_diff < min_diff:
            min_diff = curr_diff
            indices = (ind,ind+number_of_employees-1)
    return {"prods":products[indices[0]:indices[1]+1],"diff":products[indices[1]][1]-products[indices[0]][1]}

# Read the input from the file
with open("sample_input.txt","r") as input_file:
    std_input = input_file.read()

std_input = std_input.split("\n")
while 1:
  try:
    std_input.remove("")
  except:
    break
number_of_employees = int(std_input[0].split(":")[1])
goodies = list(map(lambda arr: (arr[0],int(arr[1])),map(lambda line: line.split(":"),std_input[2:])))

# print(*goodies)
# print(number_of_employees)

with open("sample_output.txt","w") as sample_output:
  sample_output.write("The goodies selected for distribution are:\n\n")
  result = find_goodies(goodies,number_of_employees)
  prods = result["prods"]
  diff = result["diff"]
  for prod in prods:
    sample_output.write(f"{prod[0]}: {prod[1]}\n")
  sample_output.write(f'\nAnd the difference between the chosen goodie with highest price and the lowest price is {diff}')



    

    




    