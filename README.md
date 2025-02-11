# Criptografia_MD2

## 🔐 Troca de chaves com Curvas Elípticas

### 📌 Descrição
Este projeto implementa criptografia por curvas elípticas. O objetivo é permitir que duas partes (Alice e Bob) compartilhem uma chave secreta sem que um atacante (Eve) possa interceptá-la, garantindo a segurança da comunicação.

### 📚 Contexto Acadêmico
Este projeto faz parte da disciplina **Matemática Discreta 2** do curso de **Engenharia de Software** na **Universidade de Brasília (UnB)**.

---

## 🔧 Funcionamento do Algoritmo
1. **Configuração da Curva Elíptica**
   - Define-se a equação da curva: \( y^2 \equiv x^3 + ax + b \mod p \).
   - Gera-se os pontos pertencentes à curva.
   - Escolhe-se um ponto gerador \( G \) que será utilizado na troca de chaves.
   
2. **Geração de Chaves**
   - Alice escolhe uma chave privada aleatória \( \alpha \).
   - Bob escolhe uma chave privada aleatória \( \beta \).

3. **Cálculo das Chaves Públicas**
   - Alice calcula \( A = \alpha G \) e envia para Bob.
   - Bob calcula \( B = \beta G \) e envia para Alice.

4. **Cálculo da Chave Compartilhada**
   - Alice recebe \( B \) e calcula \( P = \alpha B \).
   - Bob recebe \( A \) e calcula \( P = \beta A \).
   - Como \( \alpha B = \alpha \beta G \) e \( \beta A = \beta \alpha G \), ambos obtêm a mesma chave secreta.

5. **Segurança**
   - Um atacante (Eve) pode ver \( A \) e \( B \), mas não consegue calcular a chave secreta sem resolver o problema do logaritmo discreto em curvas elípticas, que é computacionalmente inviável para números grandes.

---

## 📜 Estrutura do Código
- `ecc_dh.c`: Implementação do protocolo Diffie-Hellman com curvas elípticas.
- `README.md`: Documento explicativo sobre o projeto.

---

## 🚀 Como Compilar e Executar
```sh
# Compilar o código
gcc ecc_dh.c -o ecc_dh

# Executar o programa
./ecc_dh <a> <b> <p>
```

### 📌 Exemplo de Execução
```sh
./ecc_dh 2 3 97
```

### 📌 Exemplo de Saída
```sh
Pontos geradores na curva elíptica:
G1 = (x1, y1)
G2 = (x2, y2)
...

Gerador escolhido (G2): (1, y2)

Chave privada de Alice: 3
Chave privada de Bob: 7
Chave pública de Alice: 3 * G2
Chave pública de Bob: 7 * G2
Chave compartilhada calculada por Alice: 3 * (7 * G2)
Chave compartilhada calculada por Bob: 7 * (3 * G2)

✅ Troca de chaves bem-sucedida! Chave compartilhada: (x_final, y_final)
```

---

## 📖 Referência
- https://youtu.be/F3zzNa42-tQ?si=4DF7ktwa5LfQqshV

---

## 👨‍💻 Autor
- **Nomes:** [Nathan Batista Santos](https://github.com/Nathan-bs) / [Tiago Sousa Nepomuceno](https://github.com/TiagoCTnepo)
- **Universidade:** Universidade de Brasília (UnB)
- **Disciplina:** Matemática Discreta 2

