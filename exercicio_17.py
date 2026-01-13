import random 
apresentação = [input('primeiro aluno: '),
                input('segundo aluno: '),
                input('terceiro aluno: '),
                input('quarto aluno: '),
                ]

random.shuffle(apresentação)

print(f'a ordem escolhida dos alunos para apresentação do trabalho é: {apresentação} ')
