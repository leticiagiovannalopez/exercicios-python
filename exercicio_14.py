import math
angulo = float(input('digite o angulo que voce deseja: '))
print(f'O ângulo {angulo:.2f} tem o SENO de {math.sin(math.radians(angulo)):.2f}, '
      f'o COSSENO de {math.cos(math.radians(angulo)):.2f} e '
      f'a TANGENTE de {math.tan(math.radians(angulo)):.2f}')

#ou:

import math

angulo = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O ângulo {angulo:.2f} tem SENO {seno:.2f}, COSSENO {cosseno:.2f} e TANGENTE {tangente:.2f}')
