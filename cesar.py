def cesar(encrypt):
   ukralphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   number = '0123456789'
   key = int(1)
   encrypted = ""

   for letter in encrypt:
       position = alphabet.find(letter)
       newPosition = position + key
       if letter in alphabet:
           if newPosition >= 26:
                newPosition = newPosition - 26
           encrypted = encrypted + alphabet[newPosition]

       position2 = ukralphabet.find(letter)
       newPosition2 = position2 + key
       if letter in ukralphabet:
           if newPosition2 >= 33:
               newPosition2 = newPosition2 - 33
           encrypted = encrypted + ukralphabet[newPosition]

       position1 = number.find(letter)
       newPosition1 = position1 + key
       if letter in number:
           if newPosition1 >= 10:
               newPosition1 = newPosition1 - 10
           encrypted = encrypted + number[newPosition]
       if letter == "":
           encrypted = encrypted + letter


   return encrypted

def cesardecode(encrypt):
   ukralphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   number = '0123456789'
   key = int(-1)
   encrypted = ""

   for letter in encrypt:
       position = alphabet.find(letter)
       newPosition = position + key
       if letter in alphabet:
           if newPosition >= 26:
                newPosition = newPosition - 26
           encrypted = encrypted + alphabet[newPosition]

       position2 = ukralphabet.find(letter)
       newPosition2 = position2 + key
       if letter in ukralphabet:
           if newPosition2 >= 33:
               newPosition2 = newPosition2 - 33
           encrypted = encrypted + ukralphabet[newPosition]

       position1 = number.find(letter)
       newPosition1 = position1 + key
       if letter in number:
           if newPosition1 >= 10:
               newPosition1 = newPosition1 - 10
           encrypted = encrypted + number[newPosition]
       if letter == "":
           encrypted = encrypted + letter

   return encrypted
