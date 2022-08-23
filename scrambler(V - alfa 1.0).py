sings = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ' ', ',', '!', '?', '-', '+']
cipher = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '0A', '0B', '0C', '0D', '0E', '0F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D', '1E', '1F', '20', '21',
        '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42',
        '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C',]

def encryption(sing):
    index = sings.index(sing)
    return(cipher[index])

def unEncryption(sing):
    index = cipher.index(sing)
    return(sings[index])

while True:
    outp = ''
    inp = str(input())
    inp = inp.lower()
    if inp == 'stop':
        break
    if inp == '#':
        inp = str(input())
        for i in range(0, len(inp), 2):
            sing = inp[i] + inp[i+1]
            outp += unEncryption(sing)
    else:
        for sing in inp:
            outp += encryption(sing)
    print(outp)