# 🔐 Criptografia por Curvas Elípticas

## 📌 Descrição
Este projeto implementa um algoritmo de troca de chaves usando curvas elípticas, baseado no protocolo Diffie-Hellman (ECC-DH). Ele permite que duas partes (Alice e Bob) compartilhem uma chave secreta de forma segura, sem que um atacante (Eve) consiga interceptá-la, garantindo a integridade e a confidencialidade da comunicação.

---

## 📚 Contexto Acadêmico
Este projeto foi desenvolvido como parte da disciplina **Matemática Discreta 2** do curso de **Engenharia de Software** na **Universidade de Brasília (UnB)**.

---

## 🔧 Funcionamento do Algoritmo

1. **Configuração da Curva Elíptica**  
   - Define-se a equação da curva:
     
         y² = x³ + ax + b  (mod p)
     
   - O usuário fornece os coeficientes \( a \), \( b \) e o módulo primo \( p \).
   - O programa calcula os pontos pertencentes à curva.

2. **Escolha do Gerador**
   - São escolhidos aleatoriamente 50 pontos que satisfazem a curva elíptica.
   - Seleciona-se o de maior ordem e faz ele funcionar como gerador G.
   - Faz-se repetidas somas em G, dadas por:

         Para pontos diferentes: P != Q
            s=(xQ​−xP)/(​yQ−yP) ​​mod p

         Para pontos iguais: P = Q
            s=(3xP²+a)/2yP mod p

         Soma: P + Q = R
            xR=s²-xP-xQ mod p
            yR=s(xP-xQ)-yP mod p

3. **Geração de Chaves**  
   - Alice escolhe uma chave privada \( alpha \).
   - Bob escolhe uma chave privada \( beta \).
   - O programa seleciona os pontos para Alice e Bob com base em \( alpha \) e \( beta \).

4. **Cálculo das Chaves Públicas**  
   - Alice calcula \( A = alpha.G \) e envia para Bob.
   - Bob calcula \( B = beta.G \) e envia para Alice.

5. **Cálculo da Chave Compartilhada**  
   - Alice recebe \( B \) e calcula \( P = alpha.B \).
   - Bob recebe \( A \) e calcula \( P = beta.A \).
   - Como \( alpha.B = alpha.beta.G \) e \( beta.A = beta.alpha.G \), ambos obtêm a mesma chave secreta.

6. **Segurança**  
   - Um atacante (Eve) pode ver os pontos públicos, mas não consegue calcular a chave secreta sem resolver o problema do logaritmo discreto em curvas elípticas, que é computacionalmente inviável para números grandes.

---

## 📜 Estrutura do Código
- `criptografia.py`: Implementação do algoritmo de troca de chaves usando curvas elípticas.
- `README.md`: Documento explicativo do projeto.

---

## 🚀 Como Executar

### 📥 Requisitos
- Python 3.x instalado no sistema.

### ⚙️ Execução

```sh
python criptografia.py <a> <b> <p>
```
- `<a>`: Coeficiente da curva elíptica.
- `<b>`: Coeficiente da curva elíptica.
- `<p>`: Módulo primo.

### 📌 Exemplo de Execução
```sh
python criptografia.py 2 2 53
```

### 📌 Exemplo de Saída
```
Pontos geradores na curva elíptica:
1g = (8, 0)
2g = (9, 22)
3g = (9, 31)

Ordens dos 50 pontos selecionados:
Ordem do ponto 1G = (8, 0): 2
Ordem do ponto 2G = (9, 22): 23
Ordem do ponto 3G = (9, 31): 23
Ordem do ponto 4G = (10, 11): 46

Ponto de maior ordem encontrado: Ponto(10, 11), ordem = 46

Múltiplos do Gerador
1G = (10, 11)
2G = (9, 22)
3G = (49, 47)

Chave privada de Alice: 3
Chave privada de Bob: 9

Gerador escolhido para Alice (3G): (49, 47)
Gerador escolhido para Bob (9G): (28, 11)

Novo gerador escolhido para Alice (27G): (16, 7)
Novo gerador escolhido para Bob (27G): (16, 7)

A chave de Alice é: 16
A chave de Bob é: 16
```

---

## 📊 Análise do Resultado
- A lista de pontos na curva é exibida.
- São escolhidos pontos geradores para Alice e Bob.
- A chave compartilhada final é exibida, que deve ser a mesma para ambos, confirmando o sucesso da troca de chaves.

---

## ⚠️ Observações
- O código utiliza o cálculo modular para determinar os pontos na curva elíptica.
- A escolha das chaves privadas \( alpha \) e \( beta \) é fixa no código, podendo ser ajustada para ser aleatória.
- Escolha sempre p primo.

---

## 👨‍💻 Autores
- **Nathan Batista Santos** ([GitHub](https://github.com/Nathan-bs))
- **Tiago Sousa Nepomuceno** ([GitHub](https://github.com/TiagoCTnepo))

---

## 🏫 Universidade
- **Universidade de Brasília (UnB)**
- **Disciplina:** Matemática Discreta 2

---

## 📖 Referência
- [Explicação sobre curvas elípticas](https://youtu.be/F3zzNa42-tQ?si=4DF7ktwa5LfQqshV)
