n1, n2, n3, n4 = map(float, input().split())
p1, p2, p3, p4 = 2, 3, 4, 1
media = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * p4) / (p1 + p2 + p3 + p4)

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    nota_exame = float(input())
    
    print(f"Nota do exame: {nota_exame:.1f}")
    
    media_final = (media + nota_exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
        
    print(f"Media final: {media_final:.1f}")