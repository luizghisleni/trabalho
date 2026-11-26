mkdir fizzbuzz && cd fizzbuzz
git init -b main

cat > fizzbuzz.py << 'EOF'
def fizzbuzz(n):
    resultado = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado


if __name__ == "__main__":
    n = int(input("Digite N: "))
    print("\n".join(fizzbuzz(n)))
EOF

cat > test_fizzbuzz.py << 'EOF'
from fizzbuzz import fizzbuzz


def test_fizzbuzz_15():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
        "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    ]
EOF

cat > README.md << 'EOF'
# FizzBuzz

Dado N, imprime de 1 a N:
- `FizzBuzz` para múltiplos de 3 e 5
- `Fizz` para múltiplos de 3
- `Buzz` para múltiplos de 5
- o próprio número nos demais casos

Uso: `python fizzbuzz.py` | Testes: `pytest`
EOF

git add fizzbuzz.py && git commit -m "Adiciona algoritmo FizzBuzz"
git add test_fizzbuzz.py && git commit -m "Adiciona teste"
git add README.md && git commit -m "Adiciona README"

