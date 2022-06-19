phone=input('phone Number: ')
digits_mapping={'0':'Zero',
                '1':'one',
                '2':'Two',
                '3':'Three',
                '4':'Four',
                '5':'Five',
                '6':'six',
                '7':'seven',
                '8':'Eight',
                '9':'nine',}
output=" "
for ch in phone:
    output+=digits_mapping.get(ch,'!')+' '
print(output)
