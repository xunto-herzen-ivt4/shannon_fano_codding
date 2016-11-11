from shannon_fano_codding import encode, decode

message = "Код_Шеннона-Фано"

codes, encoded = encode(message)
print(message, '=>', codes, ' | ', encoded)
print(decode(codes, encoded))
