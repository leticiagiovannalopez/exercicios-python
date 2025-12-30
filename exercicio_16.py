import random 
apresentação = [input('primeiro aluno: '),
                input('segundo aluno: '),
                input('terceiro aluno: '),
                input('quarto aluno: '),
                input('quinto aluno: ')]

print(f'a ordem escolhida dos alunos para apresentação do trabalho é: {random.shuffle(apresentação)} ')
