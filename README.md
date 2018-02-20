# Cálculo com Sympy

## Instruções

```sh
# Utilizando virtualenv
virtualenv -p python3 .env

# ou utilizando virtualenvwrapper
mkvirtualenv -p python3 jupyter

# Com o ambiente virtual ativado, instale as dependências
pip install -r requirements.txt

# Instale um kernel para o jupyter
ipython kernel install --user --name="python3"
```

Para minha comodidade, utilizei o plugin [Hydrogen](https://atom.io/packages/hydrogen) para o [Atom](https://atom.io/), no entanto, você pode utilizar a interface do Jupyter diretamente apenas executando `jupyter notebook` no terminal (será necessário exportar os arquivos `.py` para `.ipynb`).
