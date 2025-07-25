# Produto Vetorial em Ambientes Computacionais: Uma Ferramenta para o Ensino de Álgebra Linear

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Este repositório apresenta uma abordagem didática para a **visualização tridimensional do produto vetorial** utilizando **Python**, **NumPy** e **Matplotlib**.

📁 Repositório: [github.com/vitor-souza-ime/pv](https://github.com/vitor-souza-ime/pv)  
📄 Arquivo principal: `main.py`

---

## 📌 Descrição

O produto vetorial é uma operação fundamental da álgebra vetorial, frequentemente utilizada em aplicações de engenharia, física e matemática. Este projeto demonstra computacionalmente como o produto vetorial entre dois vetores 3D pode ser representado geometricamente em um gráfico tridimensional.

### Vetores utilizados:

- **A = [1, 0, 0]** (eixo X)
- **B = [0, 1, 0]** (eixo Y)
- Produto vetorial: **C = A × B = [0, 0, 1]** (eixo Z)

---

## 📈 Visualização

A visualização é feita com o `matplotlib`, utilizando a função `quiver` para plotar os vetores em um sistema de coordenadas tridimensional. O vetor resultante do produto vetorial é mostrado perpendicular aos vetores originais, conforme prevê a regra da mão direita.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cross_product_visual.svg/512px-Cross_product_visual.svg.png" alt="Produto Vetorial" width="400"/>
</p>

---

## ▶️ Como executar

1. **Clone o repositório**:

```bash
git clone https://github.com/vitor-souza-ime/pv.git
cd pv
````

2. **Instale as dependências** (recomenda-se usar um ambiente virtual):

```bash
pip install matplotlib numpy
```

3. **Execute o script principal**:

```bash
python main.py
```

---

## 🎓 Aplicações Didáticas

Este projeto é ideal para:

* Aulas de Álgebra Linear
* Demonstrações em Física Vetorial
* Ensino de Geometria Analítica
* Exploração de visualizações 3D com Python

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença [MIT](LICENSE).

---

