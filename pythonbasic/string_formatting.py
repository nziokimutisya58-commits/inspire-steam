# musa majjid
# 2/9#02/2026
# string_formatting

# get string length
sentence = "i watch anime"

string_length = len(sentence)

print(f"the length is:{string_length}")

# splitting a string
sentence_2 = "Mathematics physic"
split = sentence_2.split(" ")

print(f"the first subject is: ",split[0])



mpesa_code = "tiff12gvd"
capitalized = mpesa_code.upper()


print("New mpesa code: ", capitalized)

# make everything lowercase
MPESA_CODE = "UB21DDsfgh"
lowercase = MPESA_CODE.lower()

print("new mpesa code: ", lowercase)
 
#replacing character in a string

balance = "100kes"
amount_added = "50kes"

cleaned_balance = balance.replace("KES", "")

print("cleaned balance is: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("KES", "")

print("cleaned amount added: ", cleaned_amount_added)

print(f"Your new mpesa balance is: ", cleaned_amount_added)

total_balance = int(cleaned_balance) + int(cleaned_amount_added)
