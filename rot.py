def reverse_rot():
    with open("rot.in", 'r') as file: 
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
        results = []
    
        for line in file:
            white_space = line.find(" ")
            if white_space == -1:
                continue  # Skip lines without a space
            
            n = int(line[:white_space])  # get the integer
            plain_text = line[white_space+1:].strip()  # get the entire string and strip newline
            reversed_s = plain_text[::-1]  # reverse the string
            
            if n == 0:
                break
            
            result = ''.join(alphabet[(alphabet.index(c) + n) % len(alphabet)] for c in reversed_s)
            results.append(result)
    
        print('\n'.join(results))

reverse_rot()
