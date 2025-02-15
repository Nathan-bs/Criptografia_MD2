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
     \[ y^2 \equiv x^3 + ax + b \pmod{p} \]
   - O usuário fornece os coeficientes \( a \), \( b \) e o módulo primo \( p \).
   - O programa calcula os pontos pertencentes à curva.

2. **Geração de Chaves**  
   - Alice escolhe uma chave privada \( \alpha \).
   - Bob escolhe uma chave privada \( \beta \).
   - O programa seleciona os geradores para Alice e Bob com base em \( \alpha \) e \( \beta \).

3. **Cálculo das Chaves Públicas**  
   - Alice calcula \( A = \alpha G \) e envia para Bob.
   - Bob calcula \( B = \beta G \) e envia para Alice.

4. **Cálculo da Chave Compartilhada**  
   - Alice recebe \( B \) e calcula \( P = \alpha B \).
   - Bob recebe \( A \) e calcula \( P = \beta A \).
   - Como \( \alpha B = \alpha \beta G \) e \( \beta A = \beta \alpha G \), ambos obtêm a mesma chave secreta.

5. **Segurança**  
   - Um atacante (Eve) pode ver os pontos públicos, mas não consegue calcular a chave secreta sem resolver o problema do logaritmo discreto em curvas elípticas, que é computacionalmente inviável para números grandes.

---

## 📜 Estrutura do Código
- `ecc_dh.c`: Implementação do algoritmo de troca de chaves usando curvas elípticas.
- `README.md`: Documento explicativo do projeto.

---

## 🚀 Como Compilar e Executar

### 📥 Requisitos
- Compilador GCC instalado no sistema.

### ⚙️ Compilação
```sh
gcc ecc_dh.c -o ecc_dh
```

### ▶️ Execução
```sh
./ecc_dh <a> <b> <p>
```
- `<a>`: Coeficiente da curva elíptica.
- `<b>`: Coeficiente da curva elíptica.
- `<p>`: Módulo primo.

### 📌 Exemplo de Execução
```sh
./ecc_dh 2 3 17
```

### 📌 Exemplo de Saída
```
Pontos geradores na curva elíptica:
G1 = (0, 6)
G2 = (0, 11)
G3 = (3, 1)
...
Novo gerador escolhido para Alice (G8): (6, 14)  
Novo gerador escolhido para Bob (G8): (6, 14)  

A chave de Alice é: 6  
A chave de Bob é: 6
```

---

## 📊 Análise do Resultado
- A lista de pontos na curva é exibida.
- São escolhidos pontos geradores para Alice e Bob.
- A chave compartilhada final é exibida, que deve ser a mesma para ambos, confirmando o sucesso da troca de chaves.

---

## ⚠️ Observações
- O código utiliza o cálculo modular para determinar os pontos na curva elíptica.
- A escolha das chaves privadas \( \alpha \) e \( \beta \) é fixa no código, podendo ser ajustada para ser aleatória.
- O algoritmo é funcional para curvas pequenas; para curvas maiores, considere otimizações na busca de pontos.

---

## 👨‍💻 Autores
- **Nathan Batista Santos** ([GitHub](https://github.com/Nathan-bs))
- **Tiago Sousa Nepomuceno** ([GitHub](https://github.com/TiagoCTnepo))

---

## 🏫 Universidade
- **Universidade de Brasília (UnB)**
- **Disciplina:** Matemática Discreta 2

---

## 📖 Referências
- [Explicação sobre curvas elípticas](https://youtu.be/F3zzNa42-tQ?si=4DF7ktwa5LfQqshV)
- Documentação do GCC: [https://gcc.gnu.org/](https://gcc.gnu.org/)