# Índice

|  |  |  |  |
| :-: | :-: | :-: | :-: |
| [Comparação](#Comparison) | [Objetos](#Objects) | [Eu tenho que conhecer C?](#do -eu tenho que saber-c) | [Tuplas nomeadas](#named -tuple-1) |
| [Variáveis](#Variables) | [`self.__init__()`](#self__init__) | [Strings, F-Strings](#Strings) | [Listas](#Lists) |
| [Nomeando de variáveis](#variable -naming) | [Espaçamento consistente](#consistent -spacing) | [Escopo](#scoping) | [Argumentos mutáveis](#mutable -arguments) |
| [Imports](#Imports) | [Intervalos](#Ranges) | [Operações com cadeias de caracteres](#string -ops) | [List Comprehensions](#List-Comprehensions) |
| [try/import/except](#tryimportexcept) | [Verificações estática de limites](#static -bounds-check) | [Coalescência nula](#null -coalescência) | [`with` Gerenciador de Contextos](#with -context-manager) |
| [Matrizes](#Arrays) | [Fatias](#Slices) | [Tuplas](#Tuples) | [Dict Compreensions](#Dict -Compreensões) |
| [Set Comprehensions](#Set -Compreensões) | [Lendo e gravando arquivos](#Reading -and-writing-files) | [Decoradores](#Decorators) | [Lambdas](#Lambdas) |
| [Conjuntos](#Sets) | [JSON](#JSON) | [Map e filter](#map —filter) | [Indentação opcional](#Optional -Indentação) |
| [Dicionários](#Dictionaries) | [CamelCase](#CamelCase) | [DocStrings](#Docstrings) | [Importar arquivos Nim em Python](#Import -Nim-files-on-Python) |
| [Operadores ternários](#Ternary -operadores) | [Testes unitários](#Unittests) | [def x proc/func](#def -vs-procfunc) | [Autoexecução do módulo principal](#Self -Execução do módulo principal) |
| [Sintaxe Python para Nim](#Python -Syntax-for-NIM) | [Publicar no PYPI](#Publish para PYPI) | [Compilação silenciosa](#Silent -Compilação) | [Ajuda do compilador](#Compiler -Help) |
| [Modos de construção](#Build -Modes) | [ABC - Classes básicas abstratas](#ABC) | [Decoradores](#Decorators) | [WebAssembly](https://github.com/nim-lang/Nim/wiki/Nim-for-TypeScript-Programmers#WebAssembly) |
| [Modelos](#Templates) | [Nim executando interpretado](https://nim-lang.org/docs/nims.html) | [Nim no navegador](https://github.com/nim-lang/Nim/wiki/Nim-for-TypeScript-Programmers#table-of-contents) | [Equivalentes da biblioteca padrão](#Standard-Library-Equivalents) |
| [Assíncrono](#Async) | [Instale o Nim do PIP](https://github.com/juancarlospaco/choosenim_install#use) | [Folha de dicas em PDF](https://github.com/lskbr/nim_cheat_seat_pt_br/releases) | [Funções Arrow](https://github.com/nim-lang/Nim/wiki/Nim-for-TypeScript-Programmers#Arrow-Functions) |
| [Como compartilhar variáveis entre funções?](#How-to-share-variables-between-functions) | [Alterar permissões do arquivo](#Change -File-Permissions) | [Alterar pasta temporariamente](#Temporarily -Change-Folder) | [Pattern Matching - Correspondência de padrões](https://github.com/nim-lang/fusion/blob/master/src/fusion/matching.rst) |
| [Melhores práticas](https://github.com/nim-lang/Nim/wiki/best-practices#best-practices) | [No local versus fora do lugar](#in -Place-vs-Out-Place) | [Executar no NodeJS](https://github.com/nim-lang/Nim/wiki/Nim-for-TypeScript-Programmers#nodejs-compatibility) | [Expansão de código](#run -time-code-expansion) |
| [Arduino, MicroPython, ESP32, RTOS grátis](#MicroPython) | [Codificação ao vivo, FoxDot, SuperCollider](#SuperCollider) | [Nim instalável por PIP incorporado em Python](https://github.com/juancarlospaco/nim4py#nim4python) | [Instale pacotes Nim do PIP](https://github.com/juancarlospaco/nimble_install#use) |

* [Versão em inglês](https://github.com/nim-lang/Nim/wiki/Nim-for-Python-Programmers#table-of-contents)
* [Versão em espanhol](https://github.com/nim-lang/Nim/wiki/Nim-for-Python-Programmers-ES#tabla-de-contenidos)

## Comparação

| Característica | :snake: Python | :crown: Nim |
| --- | --- | --- |
| Modelo de execução | Máquina virtual (interpretador) | Código de máquina via C/C++ (compilador) |
| Escrito usando | C (CPython) | Nim |
| Licença | Licença da Python Software Foundation | [MIT](https://tldrlegal.com/license/mit-license) |
| Versão (principal) | `3.x` | `1.x` |
| Metaprogramação | :heavy_check_mark: metaclass, exec, eval, [ast](https://docs.python.org/3/library/ast.html)
(expansão de código em tempo de execução) | :heavy_check_mark: [modelo, macros](https://nim-lang.github.io/Nim/manual.html#macros)
(expansão do código em tempo de compilação) |
| Gerenciamento de memória | Coletor de lixo | [Gerenciamento de memória multiparadigma](https://nim-lang.github.io/Nim/gc.html)
(coletores de lixo, [ARC/ORC](https://www.youtube.com/watch?v=aUJcYTnPWCg),
manual) |
| Tipagem | Dinâmica, Duck Typing | Estática |
| Tipos dependentes | :negative_squared_cross_mark: | :heavy_check_mark: Suporte parcial |
| Genéricos | Duck Typing | :heavy_check_mark: |
| tipos
int8/16/32/64 | :negative_squared_cross_mark: | :heavy_check_mark: |
| tipos uint8/16/32/64 | :negative_squared_cross_mark: | :heavy_check_mark: |
| tipos float32/float64 | :negative_squared_cross_mark: | :heavy_check_mark: |
| Tipos de caractere | :negative_squared_cross_mark: | :heavy_check_mark: |
| Tipos de subfaixa | :heavy_check_mark: | :heavy_check_mark: |
| Tipos de enum | :heavy_check_mark: | :heavy_check_mark: |
| Bigints (tamanho arbitrário) | :heavy_check_mark: | :heavy_check_mark: [jsbigints](https://nim-lang.github.io/Nim/jsbigints.html),
[#14696](https://github.com/nim-lang/Nim/issues/14696#issue-640117621) |
| Maior número inteiro embutido | Desconhecido, limitado pela memória livre | `18_446_744_073_709_551_615` para o tipo `uint64` |
| Matrizes | :heavy_check_mark: | :heavy_check_mark: |
| Inferência de tipo | Duck typing | :heavy_check_mark: |
| Closures | :heavy_check_mark: | :heavy_check_mark: |
| Sobrecarga do operador | :heavy_check_mark: | :heavy_check_mark: em qualquer tipo |
| Operadores personalizados | :negative_squared_cross_mark: | :heavy_check_mark: |
| Orientado a objetos | :heavy_check_mark: | :heavy_check_mark: |
| Métodos | :heavy_check_mark: | :heavy_check_mark: |
| Exceções | :heavy_check_mark: | :heavy_check_mark: |
| Funções anônimas | :heavy_check_mark: várias linhas, expressão única | :heavy_check_mark: várias linhas, várias expressões |
| List comprehensions | :heavy_check_mark: | :heavy_check_mark: |
| Dict comprehensions | :heavy_check_mark: | :heavy_check_mark: |
| Set comprehensions | :heavy_check_mark: | :heavy_check_mark: |
| Compreensões personalizadas de objetos | :heavy_check_mark: expressão geradora | :heavy_check_mark: |
| Pattern Matching embutido | :heavy_check_mark: A partir do Python 3.10 | :heavy_check_mark: |
| Imutabilidade dos tipos | Tipos básicos (número, string, bool), tuple, frozenset | :heavy_check_mark: |
| Imutabilidade das variáveis | :negative_squared_cross_mark: | :heavy_check_mark: |
| Imutabilidade dos argumentos da função | Dependendo do tipo | Imutável |
| Literais de string formatados | :heavy_check_mark: f-strings | :heavy_check_mark: [strformat](https://nim-lang.github.io/Nim/strformat.html) |
| FFI | :heavy_check_mark: ctypes, API de extensão C (Cython via pip) | :heavy_check_mark: C, C++, Objective C, JS (dependendo do backend usado) |
| Assíncrono | :heavy_check_mark: | :heavy_check_mark: |
| Tópicos | :heavy_check_mark: GIL - Bloqueio de intérprete global | :heavy_check_mark: |
| Regex | :heavy_check_mark: compatível com Perl | :heavy_check_mark: compatível com Perl |
| Comentários da documentação | :heavy_check_mark: cadeias de texto simples com várias linhas (reStructuredText
via Sphinx) | :heavy_check_mark: [reStructuredText/Markdown](https://nim-lang.github.io/Nim/rst.html) |
| Publicação de pacotes | :heavy_check_mark: não embutido, requer `twine` | :heavy_check_mark: embutido, `nimble` |
| Gerenciador de pacotes | :heavy_check_mark: `pip` | :heavy_check_mark: `nimble` |
| Formatador automático de código | :heavy_check_mark: `black` e outros via pip | :heavy_check_mark: `nimpretty` embutido, [nimlint](https://github.com/nim-dev/nimlint) |
| Extensões de arquivo | .py, .pyw, .pyc, .pyd, .so | .nim, .nims |
| Formato de representação intermediária temporária (IR) | .pyc (código de bytes da VM do CPython) | C, C++, Objective C (LLVM IR via nlvm) |
| Usa #! shebang em arquivos | :heavy_check_mark: | :heavy_check_mark: `nimr`, `nimcr` |
| REPL | :heavy_check_mark: | [inim](https://github.com/inim-repl/INim#inim-interactive-nim-shell —),
[Nim4Colab](https://github.com/demotomohiro/nim4colab) |
| Indentação | Tabulações e espaços, uniformes por bloco de código, 4 espaços por convenção | Somente espaços, uniforme por bloco de código, 2 espaços por convenção |

Notas:

- Sabe-se que as funções anônimas do Python (lambdas) são lentas em comparação
com as funções normais.
- O Python Regex afirma ser compatível com PCRE, mas na prática os PCRE Regexes
podem não funcionar.
- As funções anônimas “de várias linhas” do Python podem exigir o uso de `;` e o
Linters/IDE pode reclamar disso.

## Variáveis

A criação de uma nova variável usa `var` ou `let` ou `const`. Nim tem
imutabilidade e execução de funções em tempo de compilação. Você pode atribuir
funções às variáveis.

| Característica | `const` | `let` | `var` |
| --- | --- | --- | --- |
| Tempo de execução | NÃO | :heavy_check_mark: SIM | :heavy_check_mark: SIM |
| Tempo de compilação | :heavy_check_mark: SIM | NÃO | NÃO |
| Imutável | :heavy_check_mark: SIM | :heavy_check_mark: SIM | NÃO |
| Inicializado automaticamente | :heavy_check_mark: SIM | :heavy_check_mark: SIM | :heavy_check_mark: SIM |
| Reatribuível | NÃO | NÃO | :heavy_check_mark: SIM |
| Requer atribuição | :heavy_check_mark: SIM | :heavy_check_mark: SIM | NÃO |
| Pode ser global | :heavy_check_mark: SIM | :heavy_check_mark: SIM | :heavy_check_mark: SIM |

[Para usuários avançados, é possível ignorar a inicialização automática de
variáveis.](https://nim-lang.github.io/Nim/manual.html#statements-and-expressions-var-statement)

### Nomeação de variáveis

As variáveis podem ter várias linhas sem “escapar” delas ou usar parênteses.
Isso é útil para linhas longas e operadores ternários longos. Exemplo mínimo:

```python
variable = 666 +  \
  420 *  \
  42 -   \
  9           

assert variable == 18297
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
var variable = 666 +
  420 *
  42 -
  9

assert variable == 18297
```

Isso também funciona com chamadas de função:

```nim
import std/strutils

var variable = "  12345  "
  .strip
  .parseInt

assert variable == 12345
```

Você pode usar sublinhados, novas linhas (new lines) e espaços em branco nos
nomes das variáveis:

```nim
let `this must  be  
     positive`: Positive = 42

assert this_must_be_positive == 42

const `this is my nice named variable` = 42
```

[Você pode usar palavras-chave reservadas como nomes de variáveis.](https://nim-lang.github.io/Nim/manual.html#lexical-analysis-stropping)

Não há problema em usar `var` enquanto aprende Nim ou para prototipagem rápida,
embora seja muito melhor aprender a diferença entre diferentes declarações de
variáveis.

## Espaçamento consistente

Os espaços devem ser consistentes em seu código, principalmente em torno dos
operadores:

```nim
echo 2 - 1 # OK
echo 2-1   # OK
```

Espaços inconsistentes incorretos:

```nim
echo 2 -1 # Error
#      ^ parses as "-1"
```

Omitir espaços em seu código não afeta o desempenho.

Todos os operadores são funções no Nim.

## Escopo

- Escopo: “vazamentos”, “bugs”, “falhas”, etc.

```python
for x in range(0, 9):
  if x == 6:
    print(x)

print(x)
```

Saída:

```
6
8  # Leak!
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
for x in 0..9:
  if x == 6:
    echo x

echo x
```

Saída:

```
Error: undeclared identifier: 'x'
```

Observe que, no exemplo acima, usamos um simples `int`, então o problema pode
não parecer grave. Mas se `x` tivesse alguns gigabytes de RAM, ele “vazaria” do
loop `for` para o resto do escopo externo ou principal, em vez de ser
recuperado. Nim evita esse problema.

Outro exemplo:

```python
x = 0
y = 0

def example():
  x = 1
  y = 1
  class C:
    nonlocal x, y
    assert x == 1 and y == 1
    x = 2

example()
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
var x = 0
var y = 0

proc example() =
  var x = 1
  var y = 1
  type C = object
  assert x == 1 and y == 1
  x = 2

example()
```

Outro exemplo:

```python
x = 0
y = 0

def example():
  x = 1
  y = 1
  class C:
    nonlocal x, y
    assert x == 1 and y == 1
    x = 2
    try:
      raise
    except Exception as _:
      pass

example()
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
var x = 0
var y = 0

proc example() =
  var x = 1
  var y = 1
  type C = object
  assert x == 1 and y == 1
  x = 2
  try:
    raise
  except Exception as y:
    discard

example()
```

# Condicionais booleanos

- Comparações booleanas “bugs”, “falhas”, etc.

```python
assert True == not False
```

Falha com o erro:

```
SyntaxError: invalid syntax.
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

O exemplo do Nim é compilado e executado sem incidentes; a precedência do
operador é resolvida corretamente:

```nim
assert true == not false
```

Outro exemplo:

```python
assert False + 1
assert not True - 1
```

Isso é executado porque `bool` é um subtipo de `int` em Python, portanto, ele
suporta as mesmas operações matemáticas. Em Nim, esse não é o caso:

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
assert false + 1
assert not true - 1
```

Não compila:

```
Error: type mismatch: got <bool, int>
```

# bloco

`block` cria explicitamente um novo escopo, sem a sobrecarga de uma função. Ele
pode ter um “nome” sem que o nome polua o namespace local e pode ser
interrompido em qualquer lugar sem exigir `retornar`.

`block` também pode ser usado com `var`, `let` e `const`.

Imagine que você precise sair de um `if` aninhado, sem executar nenhum outro
código de outros blocos `if` e `else`. Você pode fazer:

```python
print("Before")

# this is a function, has overhead, pollutes namespace, must return to interrupt, etc.
def example():
  if True:
    print("Inside if true")
    if 42 > 0:
      print("Inside if 42 > 0")
      if 'z' > 'a':
        print("Inside if z > a")
        return  # Must return to interrupt
        if 3.14 > 0.0:
          print("Inside if 3.14 > 0.0")
      else:
        print("else of z > a")
    else:
      print("else of 42 > 0")
  else:
    print("else of true")

example()  # example in namespace
print("After")
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
echo "Before"

block example:  # Creates a new explicit named scope. This is not a function; there is no overhead.
  if true:
    echo "Inside if true"
    if 42 > 0:
      echo "Inside if 42 > 0"
      if 'z' > 'a':
        echo "Inside if z > a"
        break example  # Gets out of block example.
        if 3.14 > 0.0:
          echo "Inside if 3.14 > 0.0"
      else:
        echo "else of z > a"
    else:
      echo "else of 42 > 0"
  else:
    echo "else of true"

# No function call. "example" is not polluting the local namespace.
echo "After"
```

- https://nim-lang.github.io/Nim/manual.html#statements-and-expressions-block-statement
- https://nim-lang.github.io/Nim/manual.html#statements-and-expressions-block-expression

## Argumentos mutáveis

```python
def example(argument = [0]):
  argument.append(42)
  return argument

print(example())
print(example())
print(example())
```

Saída:

```python
[0, 42]
[0, 42, 42]
[0, 42, 42, 42]
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
func example(argument = @[0]): auto =
  argument.add 42
  return argument

echo example()
echo example()
echo example()
```

Saída:

```nim
Error: type mismatch: got <seq[int], int literal(42)>

but expected one of: 
proc add[T](x: var seq[T]; y: sink T)
  first type mismatch at position: 1
  required type for x: var seq[T]
  but expression 'argument' is immutable, not 'var'
```

## Importações

| Importar | :snake: Python | :crown: Nim |
| --- | --- | --- |
| Apenas um símbolo, use não qualificado | `from math import sin` | `from std/math import sin` |
| Todos os símbolos, use sem qualificação | `from math import *` | **`import std/math` (recomendado) ** |
| Todos os símbolos, use totalmente qualificados | **`import math` (recomendado) ** | `from std/math import nil` |
| “importar as” outro nome | `import math as batata` | `import std/math as batata` |
| Ambos os itens acima ao mesmo tempo | :negative_squared_cross_mark: | `from std/math as m import nil` |
| Todos os símbolos, exceto um, usam sem qualificação | :negative_squared_cross_mark: | `import std/math except sin` |
| Todos os símbolos, exceto vários, usam sem qualificação | :negative_squared_cross_mark: | `import std/math except sin, tan, PI` |
| Incluir outro módulo neste módulo | :negative_squared_cross_mark: | `incluir algum módulo` |

**Seus módulos e tipos não vão colidir! , mesmo que você tenha tipos chamados de
módulos, relaxe e continue codificando... **

No Nim, `import std/math` importa todos os símbolos do módulo `math` (`sin`,
`cos`, etc) para que eles possam ser usados sem qualificação. O equivalente em
Python é `from math import *`.

Se você preferir não importar todos os símbolos e sempre usar nomes
qualificados, o código Nim é `from std/math import nil`. Então você pode chamar
`math.sin () `, `math.cos ()`, etc. O equivalente em Python é `import math`.

Geralmente, é seguro importar todos os nomes no Nim porque o compilador não
compilará nenhuma função não utilizada (portanto, não há sobrecarga). Além
disso, como o Nim é estaticamente tipado, ele geralmente pode distinguir entre
as duas funções importadas com os mesmos nomes com base nos tipos de argumentos
com os quais são chamadas. Nos raros casos em que os tipos são iguais, você
ainda pode qualificar totalmente o nome para desambiguar.

O prefixo `std/` impõe que o módulo seja importado da biblioteca padrão. Se um
pacote Nimble tiver um módulo com o mesmo nome, o compilador pode resolver a
ambiguidade e isso está explícito no código.

Módulos locais e módulos Nimble não precisam do prefixo `std/`.

Python e Nim compartilham essas declarações de importação:

```
# Python and Nim
import foo, bar, baz

import foo
import bar
import baz
```

Sintaxes alternativas:

```python
# Python
import foo, \
       bar, \
       baz
```

```nim
# Nim
import foo,
       bar,
       baz

# Useful for small diffs when adding/removing imports
import
  foo,
  bar,
  baz

import 
  foo, bar, baz,
  more, imports
```

A variante com uma instrução `import` por linha é comum em Python e Nim, mas em
Nim a forma `import foo, bar, baz` também é vista com frequência.

Mais exemplos:

```nim
## This is documentation for the module.
#  This is a comment.
include prelude
import std/sugar as stevia
from std/math import nil
from std/with as what import nil
```

### Programaticamente

```python
__import__("math")
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
template imports(s) = import s
imports math
```

### Código sem importações

Às vezes, na natureza, você pode ver exemplos de código ou arquivos **sem** as
importações, mas eles de alguma forma funcionam de qualquer maneira. O motivo é
que Nim pode usar `import` do comando compile ou de um arquivo `.nims`:

- `nim c --import:sugar file.nim`
- `nim c --import:folder/mymodule file.nim`
- `nim js --import:strutils --include:mymodule file.nim`

Às vezes, projetos ou exemplos de código rápido usam isso para evitar a
digitação. Graças ao Dead Code Elimination (Eliminação de código morto), se os
símbolos importados não forem usados, eles não existirão na saída compilada.

Veja também:

- [Interruptores de linha de comando Nim](https://nim-lang.github.io/Nim/nimc.html#compiler-usage-command-line-switches)

### Prelúdio

Às vezes, você pode achar que o Python tem mais símbolos disponíveis por padrão
sem qualquer `importação` em comparação com o Nim. Para ter uma experiência
semelhante de ter as estruturas básicas de dados e as importações mais comuns
prontas para que você possa começar a codificar imediatamente, você pode usar
[prelude](https://nim-lang.github.io/Nim/prelude.html):

```nim
include prelude

echo now()             
echo getCurrentDir() 
echo "Hello $1".format("World")
```

[prelude](https://nim-lang.github.io/Nim/prelude.html) é um arquivo [`include`](https://nim-lang.github.io/Nim/manual.html#modules-include-statement)
que simplesmente importa módulos comuns para sua conveniência, para evitar a
digitação. [prelúdio](https://nim-lang.github.io/Nim/prelude.html) também
funciona para destinos em JavaScript.

### De onde vêm os símbolos?

- Se os símbolos não são qualificados, como você sabe de onde vêm os símbolos?

Dado que `foo () `é um símbolo:

- Nota: você normalmente tem `foo () `, [com suporte do UFCS](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax#Nim_programming_language).
- Python: você normalmente tem `object.foo () `em vez de `module.foo ()`, sem
UFCS.

Normalmente, o [Editor/IDE](https://marketplace.visualstudio.com/items?itemName=kosz78.nim)
deve sugerir de onde vêm os símbolos, como em qualquer outra linguagem de
programação:

! [](https://raw.githubusercontent.com/pragmagic/vscode-nim/master/images/nim_vscode_output_demo.gif)

O Nim vem integrado com o [NimSuggest](https://nim-lang.org/docs/nimsuggest.html)
para integrações de editor/IDE.

Ao contrário do Python, o sistema de tipos de Nim tem todas as informações sobre
todos os símbolos:

```nim
import std/macros
macro findSym(thing: typed) = echo thing.getType.lineInfo

findSym:
  echo  # Where echo comes from?.
```

`echo` vem de:

```
lib/system.nim(1929, 12)
```

Ao aprender Nim ou para prototipagem rápida, não há problema em usar os símbolos
totalmente qualificados. Fazer isso não produz erros, mas o Nim idiomático evita
isso.

### Exportações

Em Python, todos os símbolos no módulo são visíveis e mutáveis dos módulos que o
importam, incluindo símbolos que não devem ser usados ou alterados fora do
módulo.

No Nim, tudo é privado por padrão e, portanto, não é visível em outros módulos.
Para tornar os símbolos públicos e visíveis em outros módulos, você precisa usar
o asterisco `*`:

```nim
let variable* = 42
const constant* = 0.0
proc someFunction*() = discard
template someTemplate*() = discard
type Platypus* = object
  fluffyness*: int
```

O asterisco não apenas torna o símbolo visível para o mundo exterior, mas também
aparecerá na documentação gerada (`nim doc`). Quando você importa o módulo, o
símbolo será automaticamente adicionado ao namespace, mas símbolos privados (não
exportados) sem `*` não estarão visíveis. O asterisco é como uma **dica visual**
para humanos. Você pode entender imediatamente quais símbolos fazem parte da
“API pública” apenas examinando o código-fonte do módulo. O asterisco `*` é
pronunciado como “estrela”.

Para obter mais informações, leia:
https://narimiran.github.io/2019/07/01/nim-import.html

## try/import/except

Em Python, os imports são uma operação em tempo de execução e podem falhar. É um
padrão bastante comum que os imports dependentes da plataforma sejam colocadas
dentro de um bloco try e uma alternativa ou fallback dentro do bloco except:

```python
try:
    import module
except ImportError:
    import othermodule as module

try:
    from module import some_func
except ImportError:
    # Fallback implementation
    def somefunc():
        return some_value
```

O Nim resolve todas as importações em tempo de compilação, então algo como um
`ImportError` não existe. Não há necessidade de lidar com erros de importação em
tempo de execução.

## Matrizes

As matrizes em Nim são de tamanho fixo, começam no índice `0` e devem conter
elementos do mesmo tipo.

Ao passar uma matriz para uma função em Nim, o argumento é uma referência
imutável. O Nim incluirá verificações em tempo de execução nos limites das
matrizes.

Você pode usar um [`openarray`](https://nim-lang.github.io/Nim/manual.html#types-open-arrays)
para aceitar uma matriz de qualquer tamanho nos argumentos da função, e você
pode usar `low (seu_array) `e `high (seu_array)` para consultar os limites da
matriz.

Nim `string` é compatível com `openArray [char] `para evitar cópias
desnecessárias para otimização, e `char` é compatível com `int`. Portanto, a
manipulação de `strings` pode ser feita com a matemática no local de forma
transparente. Uma função que usa `openArray [char] `aceita `"abcd"` *e*
`['a', 'b', 'c', 'd']`.

O conteúdo da matriz é sempre contíguo na memória, assim como as matrizes de
matrizes.

Veja também:

- [Visualizações](https://nim-lang.github.io/Nim/manual_experimental.html#view-types)

## Tamanhos dos tipos de dados

- Qual é o tamanho dos diferentes tipos de dados?.

```nim
import std/json

type Foo = object            
type Bar = enum true, false  

# (Weird spacing intended)
assert sizeOf( Foo )        == 1
assert sizeOf( Bar )        == 1
assert sizeOf( bool )       == 1
assert sizeOf( {true} )     == 1
assert sizeOf( [true] )     == 1
assert sizeOf( (true) )     == 1
assert sizeOf( int8 )       == 1

assert sizeOf( {'k': 'v'} ) == 2
assert sizeOf( int16 )      == 2

assert sizeOf( int32 )      == 4
assert sizeOf( float32 )    == 4

assert sizeOf( int )        == 8
assert sizeOf( float )      == 8
assert sizeOf( @[true] )    == 8
assert sizeOf( %*{} )       == 8
assert sizeOf( pointer )    == 8
```

Essa é apenas uma aproximação para as primitivas vazias em 64 bits.

## Objetos

Objetos em Nim se comportam de forma bem diferente das classes em Python. Os
objetos suportam herança e OOP. As classes são denominadas tipos em Nim. Funções
(procs) são funções flutuantes livres, não vinculadas a objetos (no entanto,
você pode usá-las de uma forma muito semelhante ao Python). Você pode chamar uma
função em objetos com a sintaxe `object.function () `, bem como
`function (object)`; [estes são totalmente equivalentes](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax).
Nim não tem um `eu` implícito nem `isso`. É uma boa prática colocar todos os
tipos no topo do arquivo, mas isso não é obrigatório.

Uma forma de imaginar isso é que **procs ficam “grudados” nos tipos de seus
argumentos em tempo de compilação** e, em seguida, você pode usá-los em tempo de
execução como se fossem classes e métodos do Python.

Do Python ao Nim, *o mínimo possível* exemplo:

```python
class Kitten:
    """ Documentation Here """

    def purr(self):
        print("Purr Purr")

Kitten().purr()
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
type Kitten = object  ## Documentation Here
proc purr(self: Kitten) = echo "Purr Purr"
Kitten().purr()
```

Exemplo de herança mínima:

```nim
type Animal = object of RootObj
type Kitten = object of Animal
assert Kitten is Animal
```

Exemplos de orientação de objetos semelhantes aos do Python:

```Nim
type Animal = ref object of RootObj ## Animal base object.
  age: int                          
  name: string                      ## Attributes of base object.

type Cat = ref object of Animal     ## Cat inherited object.
  playfulness: float                ## Attributes of inherited object.

func increase_age(self: Cat) =
  self.age.inc()                    # Cat object function, access and *modify* object.

var kitten = Cat(name: "Tom")       # Cat object instance.
kitten.increase_age()               # Cat object function used.

assert kitten.name == "Tom"         # Assert on Cat object.
assert kitten.age == 1
```

Exemplo de herança:

```nim
type
  LUCA        = ref object of RootObj
  Archea      = ref object of LUCA
  Prokaryota  = ref object of Archea
  Eukaryota   = ref object of Prokaryota
  Animalia    = ref object of Eukaryota
  Chordata    = ref object of Animalia
  Mammalia    = ref object of Chordata
  Primates    = ref object of Mammalia
  Haplorhini  = ref object of Primates
  Simiiformes = ref object of Haplorhini
  Hominidae   = ref object of Simiiformes
  Homininae   = ref object of Hominidae
  Hominini    = ref object of Homininae
  Homo        = ref object of Hominini
  Homosapiens = ref object of Homo

assert Homosapiens() is LUCA
assert LUCA() isnot Homosapiens
assert sizeOf(Homosapiens) == sizeOf(LUCA)
let human = Homosapiens()
assert human is Homosapiens
```

Veja também:

- [Tipagem dinâmica via metaprogramação](https://github.com/Carpall/nobject#here-a-simple-object-for-allowing-dynamic-typing-in-nim)

## `self.__init__()`

Depois do exemplo do Cat, você provavelmente está se perguntando como fazer
`def __init__ (self, arg) :`.

Python `__init__ () `é Nim `newObject ()` ou `initObject () `. Vamos fazer um
`__init__ () `para o Cat:

```nim
type Cat = object                # Cat object.
  age: int                          
  name: string                   # Attributes of Cat object.

func initCat(age = 2): Cat =     # Cat.__init__(self, age=2)                    
  result.age = age               # self.age = age         
  result.name = "adopt_me"       # self.name = "adopt_me" 

var kitten = initCat()            # Cat object instance.

assert kitten.name == "adopt_me" # Assert on Cat object.
assert kitten.age == 2
```

A nomenclatura é uma convenção e uma boa prática. Quando você quiser init para
`Foo`, basta criar `newFoo () `ou `initFoo ()`. Como você pode notar, `initCat`
é apenas uma função que retorna um `Cat`.

- `initFoo () `para `object`.
- `newFoo () `para `ref object`.

[Leia a documentação para nomear coisas seguindo as convenções e as melhores
práticas.](https://nim-lang.org/docs/apis.html)

#### Valores padrão do atributo do objeto

O construtor de objetos também é a forma de definir valores padrão
personalizados para os atributos de seus objetos:

```nim
type Cat = object
  age: int                 # AutoInitialized to 0
  name: string             # AutoInitialized to ""
  playfulness: float       # AutoInitialized to 0.0
  sleeping: bool           # AutoInitialized to false 
func initCat(): Cat =    
  result.age = 1           # Set default value to 1
  result.name = "Bastet"   # Set default value to "Bastet"
  result.playfulness = 9.0 # Set default value to 9.0
  result.sleeping = true   # Set default value to true
```

Uma estrutura mais completa para um programa básico pode ser algo como:

```nim
## Simple application to  do Foo with the Bar.

type
  Animal = ref object of RootObj 
    age: int                          
    name: string                     

  Cat = ref object of Animal
    playfulness: float   


func initCat(age = 2): Cat =   
  result.age = age            
  result.name = "adopt_me"     

func increase_age(self: Cat) =
  self.age.inc()               

proc main() =
  var kitten = Cat(name: "Tom")  
  kitten.increase_age()           

  assert kitten.name == "Tom"      
  assert kitten.age == 1


when isMainModule:
  main()

runnableExamples:
  echo "Optionally some documentation code examples here"
  assert 42 == 42
```

## Expansão do código de execução

Objetos Python que *internamente* usam geração de código são muito, muito
lentos, escalonando com o tamanho. Quanto mais você o usa, mais lento ele
executa. `dataclass`, `metaclasse`, decoradores, etc. podem ser mais de 25 ~ 50x
mais lentos do que uma `classe` normal. [`Pathlib.path` e seus métodos podem ser
mais de 25 ~ 50x mais lentos do que um `str`] normal
(https://youtu.be/tFrh9hKMS6Y) e anulam qualquer otimização, incluindo um
arquivo `.pyc`. O Cython não tem CTFE, então isso não ajuda especificamente.

- A expansão do código Nim é feita em tempo de compilação, tornando seu custo de
geração de código zero em tempo de execução.

Por exemplo, você pode ver o resultado da expansão do código ARC durante a
compilação usando `—expandArc`. É assim que o Nim faz o gerenciamento de memória
em tempo de compilação (aproximação):

! [](https://raw.githubusercontent.com/juancarlospaco/nim-presentation-slides/master/Nim_ARC.png)

Veja também:

- [`Macros.expandMacros` mostra a expansão do código no terminal durante a
compilação](https://nim-lang.github.io/Nim/macros.html#expandMacros.m%2Ctyped)

# Unsafe Type Hints (dicas de tipagem inseguras)

As “type hints” do Python podem ser quase qualquer coisa e são executadas
implicitamente em tempo de execução. Não é preciso dizer que isso pode ser muito
inseguro:

```console
$ cat example.py
class X: _: "print('PWNED')"  # os.system("rm -rf /folder ")
__import__("typing").get_type_hints(X)

$ python3 example.py

'PWNED'

$
```

Os tipos de Nim devem ser válidos; os tipos são verificados no momento da
compilação:

```console
$ cat example.nim
type X = object
  a: "echo('PWNED')"
echo X()

$ nim r example.nim    # Will not compile.

Error: type expected, but got: "echo('PWNED')"

$
```

Outro exemplo

```console
$ cat example.nim
var example: "echo('PWNED')"
echo example

$ nim r example.nim    # Will not compile.

Error: type expected, but got: "echo('PWNED')"

$
```

# Por valor x por referência

- Nim transmite dados “por valor” ou “por referência”? Depende...

O compilador Nim determina automaticamente se um parâmetro é passado por valor
ou por referência com base no tamanho do tipo de parâmetro.

Se um parâmetro precisar ser passado por valor ou por referência (como ao fazer
interface com uma biblioteca C), use os pragmas `{.bycopy.}` ou `{.byref.}`.

**Nim passa objetos maiores que `3 * sizeOf (int) `por referência para
desempenho**, mas isso é arquitetura e implementação definidas. Portanto, as
informações a seguir são apenas uma *aproximação* para `x86_64`:

| Declaração | Valor ou referência? | Implícito ou explícito? | Gerenciado ou não gerenciado? | Observações |
| --- | --- | --- | --- | --- |
| `symbol: int` | Por valor | Implícito | Gerenciado | Uso frequente |
| `symbol: var int` | Por referência | Implícito | Gerenciado | Uso frequente |
| `symbol: ref int` | Por referência | Explícito | Gerenciado | Raro |
| `symbol: ptr int` | Por referência | Explícito | Não gerenciado | C/C++ FFI |
| `symbol: var ref int` | Por referência | Implícito | Gerenciado | Raro |
| `symbol: var ptr int` | Por referência | Implícito | Não gerenciado | Raro |
| `symbol: pointer` | Por referência | Explícito | Ponteiro não gerenciado | C/C++ FFI |

- Se um símbolo “por valor” for grande, ele será transmitido “por referência”
automaticamente.
- [Você pode desativar essa otimização usando o pragma `{.bycopy.}` no
símbolo.](https://nim-lang.github.io/Nim/manual.html#foreign-function-interface-bycopy-pragma)
- [O `{.byref.}` força a passagem “por referência”, o inverso de `{.bycopy.}`.](https://nim-lang.github.io/Nim/manual.html#foreign-function-interface-byref-pragma)
- Nim `seq` é passado “por referência” por padrão.
- Sua `string` é [Copy-On-Write](https://en.wikipedia.org/wiki/Copy-on-write)
COW (ARC/ORC).
- [A aritmética do ponteiro pode ser executada com o ponteiro.](https://en.wikipedia.org/wiki/Pointer%20arithmetic)

## Intervalos

Em Python, um número inteiro simples para loops usa a função geradora `range`.
Para as formas de argumento 1 e 2 dessa função, o [`..` iterator](https://nim-lang.org/docs/system.html#...i%2CT%2CT)
de nim funciona quase da mesma maneira:

```Nim
for i in 0 .. 10:
  echo i  # Prints 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for i in 5 .. 10:
  echo i  # Prints 5, 6, 7, 8, 9, 10
```

Observe que o operador `..` inclui o final do intervalo, enquanto o
`range (a, b) `do Python não inclui `b`. Se você preferir esse comportamento,
use o iterador [`.. <`](https://nim-lang.org/docs/system.html#..%3C.i%2CT%2CT)
em vez disso:

```Nim
for i in 0 ..< 10:
  echo i  # Prints 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

O `range () `do Python também tem um terceiro parâmetro opcional, que é o valor
a ser incrementado em cada etapa. Isso pode ser positivo ou negativo. Se você
precisar desse comportamento, use os iteradores [`countup`](https://nim-lang.org/docs/system.html#countup.i%2CT%2CT%2CPositive)
ou [`countdown`](https://nim-lang.org/docs/system.html#countdown.i%2CT%2CT%2CPositive):

```Nim
for i in countup(1, 10, 2):
  echo i  # Prints 1, 3, 5, 7, 9

for i in countdown(9, 0, 2):
  echo i  # Prints 9, 7, 5, 3, 1
```

Converta de `range` para `seq`:

```nim
import sequtils

const subrange = 0..9
const seqrange = toSeq(subrange)
assert seqrange is seq[int]
```

Veja também:

- [enumerate](https://nim-lang.github.io/Nim/enumerate.html#enumerate.m%2CForLoopStmt)

## Fatias

A sintaxe dos intervalos de fatias é diferente. `a [x:y] `do Python é
`a [x.. < y]` de Nim.

```Nim
let variable = [1, 2, 3, 4]
assert variable[0 .. 0] == @[1]
assert variable[0 .. 1] == @[1, 2]
assert variable[0 ..< 2] == @[1, 2]
assert variable[0 .. 3] == @[1, 2, 3, 4]
```

#### Fatias de índice reverso

Em Nim, um índice reverso ou índice inverso usa `^` com o número, como `^1`. Os
índices retroativos têm um tipo específico `backwardsIndex` e também podem ser
“preparados” em tempo de compilação como `const`:

```nim
const lastOne = ^1  # Compile-time
assert lastOne is BackwardsIndex
assert [1, 2, 3, 4, 5][2 .. lastOne] == @[3, 4, 5]
assert [1, 2, 3, 4, 5][2 .. ^1] == @[3, 4, 5]
var another = ^3    # Run-time
assert [1, 2, 3, 4, 5][0 .. another] == @[1, 2, 3]
assert [1, 2, 3, 4, 5][^3 .. ^1] == @[3, 4, 5]  # 2 Reverse index
```

## Verificação estática de limites

- Nim tem [verificação estática de limites em tempo de compilação.](https://en.wikipedia.org/wiki/Static_program_analysis)

Vamos comparar exemplos muito simplificados:

```python
[0, 1, 2][9]  # No Index 9
```

Isso falha em tempo de execução porque não há índice 9:

```console
$ python3 example.py
Traceback (most recent call last):
  File "example.py", line 1, in <module>
    [0, 1, 2][9]
IndexError: list index out of range

$
```

Vamos ver Nim:

```nim
discard [0, 1, 2][9] # No Index 9
```

Compile e execute:

```console
$ nim compile --run example.nim
example.nim(1, 19) Warning: can prove: 9 > 2  [IndexCheck]
example.nim(1, 18) Error: index 9 not in 0..2 [0, 1, 2][9]

$
```

Nim verifica em tempo de compilação que `[0, 1, 2]` não tem índice `9`, porque
`9 > 2`. Portanto, ele não será compilado nem executado.

Isso também funciona com o Subrange. Digamos que você tenha uma variável inteira
que **deva ser positiva**:

```nim
let must_be_positive: Positive = -9
```

Compile e execute:

```console
$ nim compile --run example.nim
example.nim(1, 34) Warning: can prove: 1 > -9 [IndexCheck]
example.nim(1, 34) Error: conversion from int literal -9 to Positive is invalid.

$
```

Nim verifica em tempo de compilação se `must_be_positive` não é `Positivo`
porque `1 > -9`. Ele não será compilado nem executado.

Outro exemplo:

```nim
var variable0: 5..8 = 5        # int range type, value must be between '5' and '8'.
variable0 = 8
variable0 = 7
assert not compiles(variable0 = 4)
assert not compiles(variable0 = 9)
assert not compiles(variable0 = 0)
assert not compiles(variable0 = -1)
assert not compiles(variable0 = -9)


var variable1: 3.3..7.5 = 3.3  # float range type, value must be between '3.3' and '7.5'.
variable1 = 7.5
variable1 = 5.5
assert not compiles(variable1 = 3.2)
assert not compiles(variable1 = 7.6)
assert not compiles(variable1 = 0.0)
assert not compiles(variable1 = -1.0)
assert not compiles(variable1 = -9.0)


var variable2: 'b'..'f' = 'b'  # char range type, value must be between 'b' and 'f'.
variable2 = 'f'
variable2 = 'c'
assert not compiles(variable2 = 'g')
assert not compiles(variable2 = 'a')
assert not compiles(variable2 = 'z')
assert not compiles(variable2 = '0')
assert not compiles(variable2 = '9')


var variable3: Positive = 1    # Positive type, value must be > 0.
variable3 = 1
variable3 = 999
assert not compiles(variable3 = 0)
assert not compiles(variable2 = -1)
assert not compiles(variable2 = -9)


var variable4: Natural = 0     # Natural type, value must be >= 0.
variable4 = 1
variable4 = 999
assert not compiles(variable4 = -1)
assert not compiles(variable4 = -9)
```

Você pode controlar isso com `—staticBoundChecks:on` ou `—staticBoundChecks:off`.

Com `—staticBoundChecks:off`, isso pode gerar um erro em tempo de execução, como
o Python faz.

- Para obter uma documentação melhor, consulte:
https://nim-lang.github.io/Nim/drnim.html

# Coalescência nula

O Python não tem um [operador de coalescência nula](https://en.wikipedia.org/wiki/Null_coalescing_operator)
(no momento em que este artigo foi escrito).

Em vez disso, os programadores de Python usam o operador condicional ternário:

```python
other = bar if bar is not None else "default value"  # "bar" may be null?, or not ?.
```

Nim tem um [módulo wrapnils](https://nim-lang.github.io/Nim/wrapnils.html) com
um `?. `operador de coalescência nula, que simplifica o código ao reduzir a
necessidade de ramificações `if.. elif... else` em torno de **valores
intermediários que podem ser nulos**.

```nim
assert ?.foo.bar.baz == ""  # "bar" may be Null?, or not ?.
```

Null é `None` em Python. Null é `nil` em Nim.

Veja: https://nim-lang.github.io/Nim/wrapnils.html

## With Context Manager

Não há equivalente nativo direto à construção `with` do Python. No Nim, existem
as seguintes opções:

- [`modelo`](#templates)
- [`macros`](https://nim-lang.github.io/Nim/manual.html#macros)
- Nomeado [`block`](https://nim-lang.github.io/Nim/manual.html#statements-and-expressions-block-statement)

[Consulte a seção Modelos para ver exemplos.](#templates)

## Strings

| Lang | String | String de várias linhas | String Raw | String Raw de múltiplas linhas | Literais formatados | Quote (mascarando) |
| --- | --- | --- | --- | --- | --- | --- |
| :snake: Python | `"foo"` | `""""foo"""` | `r"foo"` | `r"""foo"""` | `f"" "{1 + 2}" ""` | `"``'` |
| :crown: Nim | `"foo"` | `""""foo"""` | `r"foo"` | `r"""foo"""` | `fmt"" "{1 + 2}" ""` | `"` |

#### Operações de string

| Operações | :snake: Python | :crown: Nim |
| --- | --- | --- |
| Lower | `"ABCD” .lower () ` | `"ABCD".toLowerAscii()` |
| Strip | `” ab “.strip ()` | `” ab “.strip ()` |
| Split | `"a,b,c".split(",")` | `"a,b,c".split(",")` |
| Concatenação | `"a” + “b"` | `"a” e “b"` |
| Find | `"abcd".find("c")` | `"abcd".find("c")` |
| Começa com | `"abc".startswith("ab")` | `"abc".startswith("ab")` |
| Termina com | `"abc".endswith("ab")` | `"abc".endswith("ab")` |
| Dividindo por Linha | `"1\n2\n3".splitlines()` | `"1\n2\n3".splitlines()` |
| Fatiando | `"abcd"[0:2]` | `"abcd"[0 ..< 2]` |
| Cortando 1 caractere | `"abcd"[2]` | `"abcd"[2]` |
| Corte reverso | `"abcd"[-1]` | `"abcd"[^1]` |
| Normalize | [`unicodedata.normalize("NFC", "Foo")`](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "str().lower() não é a forma recomendada") | `"Foo".normalize()` |
| Contando Linhas | `len("1\n2\n3".splitlines())` | `"1\n2\n3".countLines()` |
| Repeat (repetir) | `"foo" * 9` | `"foo".repeat(9)` |
| Recuar (indent) | `textwrap.indent("foo", " " * 9)` | `"foo".indent(9)` |
| Unindent | [`textwrap.dedent(“foo”)`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent
“textwrap.dedent () Remove TODA a indentação!”) | `"foo".unindent(9)` |
| Parse Bool | [`bool(distutils.util.strtobool (“fALse”)) `](https://stackoverflow.com/q/715417
“bool ('FalSE') == True”) :pergunta: | `parseBool("fALse")` |
| Parse Int | `int("42")` | `parseInt("42")` |
| Parse Float | `float("3.14")` | `parseFloat("3.14")` |
| Literais de string formatados | `f"foo {1 + 2} bar {variable}"` | [`fmt"foo {1 + 2} bar {variable}"`](https://nim-lang.org/docs/strformat.html) |
| Distância de Levenshtein | :negative_squared_cross_mark: | [`editDistance (“Kitten”, “Bitten”) `](https://nim-lang.org/docs/editdistance.html) |

- **As operações de string Nim requerem [`import std/strutils`.](https://nim-lang.org/docs/strutils.html)
**
- [Uma comparação muito detalhada.](https://scripter.co/notes/string-functions-nim-vs-python/)

#### Eficiência de String

Strings podem ser alocadas em memória de uma só vez com
`newStringOfCap (capacity = 42) `, que retorna uma nova string vazia `""`, mas
com `capacidade` alocada de `42`. Se você ultrapassar a `capacidade`, ela não
falhará nem estourará o buffer:

```python
variable = ""
assert variable == "" # length is 0, capacity is 0, 1 allocations, 0 copies
variable += "a"       # length is 1, capacity is 1, 2 allocations, 1 copies
variable += "b"       # length is 2, capacity is 2, 3 allocations, 2 copies
variable += "c"       # length is 3, capacity is 3, 4 allocations, 3 copies
variable += "d"       # length is 4, capacity is 4, 5 allocations, 4 copies
assert variable == "abcd" 
# TOTAL: 5 allocations, 4 copies
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
var variable = newStringOfCap(2)
assert variable == "" # length is 0, capacity is 2, 1 allocations, 0 copies
variable.add "a"      # length is 1, capacity is 2, 1 allocations, 0 copies
variable.add "b"      # length is 2, capacity is 2, 1 allocations, 0 copies
variable.add "c"      # length is 3, capacity is 3, 2 allocations, 0 copies
variable.add "d"      # length is 4, capacity is 4, 3 allocations, 0 copies
assert variable == "abcd" 
# TOTAL: 3 allocations, 0 copies
```

Essa diferença pode ficar maior para strings dentro de laços for ou while.

### F-Strings

Nim `strformat` implementa literais de string formatados inspirados nas
f-strings do Python. O `strformat` é implementado usando metaprogramação e a
expansão do código é feita em tempo de compilação. Também funciona para o
destino JavaScript.

Semelhante às f-strings do Python, você pode [depurar o valor da chave
dentro da string usando um sinal de igual](https://nim-lang.github.io/Nim/strformat.html#debugging-strings).
`fmt "{key=}" `se expande para `fmt"key= {value} "`:

```nim
let x = "hello"
assert fmt"{x=}" == "x=hello"
assert fmt"{x   =  }" == "x   =  hello"
```

Nim `strformat` suporta barra invertida, enquanto as strings f do Python não:

```python
>>> print( f"""{ "yep\nope" }""" ) # Run-time error.
Error: f-string expression part cannot include a backslash.
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
echo fmt"""{ "yep\nope" }"""       # Nim works.

yep
ope
```

Você pode escolher um par de caracteres personalizado para abrir e fechar a
formatação dentro da string passando o `char` como argumento:

```nim
import std/strformat
let variable = 42
assert fmt("( variable ) { variable }", '(', ')') == "42 { variable }"
assert fmt("< variable > { variable }", '<', '>') == "42 { variable }"
```

Usar caracteres como apóstrofo invertido e espaço `' '`funciona:

```nim
import std/strformat
let variable = 42
assert fmt(" variable`{variable}", ' ', '`') == "42{variable}"
```

- [É recomendável ler a documentação completa do `strformat`.](https://nim-lang.github.io/Nim/strformat.html)

## String Raw

A string raw do Python não pode terminar em `"\"`, mas a string raw do Nim
funciona muito bem:

```python
>>> print(r"\")  # Run-time error.
SyntaxError: EOL while scanning string literal.
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
nim> echo r"\"
"\"
```

Isso pode ser relevante ao trabalhar com cadeias de caracteres que usam `"\"`,
como caminhos de sistemas de arquivos `r” C:\mypath\ "`, etc.

## Equivalentes de biblioteca padrão

- [Biblioteca padrão Python para Nim.](https://github.com/juancarlospaco/cpython#alternative-stdlib-for-nim-for-python-targets)

| Use | :snake: Python | :crown: Nim |
| --- | --- | --- |
| Sistema operacional | os | [os](https://nim-lang.org/docs/os.html) |
| Operações de string | string | [strutils](https://nim-lang.org/docs/strutils.html) |
| Data e hora | datetime | [times](https://nim-lang.org/docs/times.html) |
| Random | random | [random](https://nim-lang.org/docs/random.html) |
| Expressões regulares (Backend) | re | [re](https://nim-lang.org/docs/re.html) |
| Expressões regulares (Frontend) | :negative_squared_cross_mark: | [jsre](https://nim-lang.github.io/Nim/jsre.html) |
| HTTP | urllib | [httpclient](https://nim-lang.org/docs/httpclient.html) |
| Logando | logging | [registro](https://nim-lang.org/docs/logging.html) |
| Executando comandos externos | subprocess | [osproc](https://nim-lang.org/docs/osproc.html) |
| Manipulação de caminhos (path) | pathlib, os.path | [os](https://nim-lang.org/docs/os.html) |
| Matemática | math, cmath | [math](https://nim-lang.org/docs/math.html) |
| Tipos MIME | tipos MIME | [mimetypes](https://nim-lang.org/docs/mimetypes.html) |
| SQLite SQL | sqlite3 | [db_sqlite](https://nim-lang.org/docs/db_sqlite.html) |
| Postgres SQL | :negative_squared_cross_mark: | [db_postgres](https://nim-lang.org/docs/db_postgres.html) |
| Distância de Levenshtein | :negative_squared_cross_mark: | [editdistance](https://nim-lang.github.io/Nim/editdistance.html) |
| Serialização | pickle | [json](https://nim-lang.org/docs/json.html), [jsonutils](https://nim-lang.github.io/Nim/jsonutils.html),
[marshal](https://nim-lang.org/docs/marshal.html) |
| Base64 | base64 | [base64](https://nim-lang.org/docs/base64.html) |
| Abre o URL do navegador da web | webbrowser | [browsers](https://nim-lang.org/docs/browsers.html) |
| Assíncrono | asyncio | [asyncdispatch](https://nim-lang.org/docs/asyncdispatch.html), [asyncfile](https://nim-lang.org/docs/asyncfile.html),
[asyncnet](https://nim-lang.org/docs/asyncnet.html), [asyncstreams](https://nim-lang.org/docs/asyncstreams.html) |
| Testes unitários | unittest | [unittest](https://nim-lang.org/docs/unittest.html) |
| Diff | difflib | [diff](https://nim-lang.org/docs/diff.html) |
| Cores | colorsys | [colors](https://nim-lang.org/docs/colors.html) |
| MD5 | hashlib.md5 | [md5](https://nim-lang.org/docs/md5.html) |
| SHA1 | hashlib.sha1 | [sha1](https://nim-lang.org/docs/sha1.html) |
| Servidor HTTP | http.server | [asynchttpserver](https://nim-lang.org/docs/asynchttpserver.html) |
| Lexer | shlex | [lexbase](https://nim-lang.org/docs/lexbase.html) |
| Multi-Threading | threading | [threadpool](https://nim-lang.org/docs/threadpool.html) |
| URL E URI | urllib.parse | [uri](https://nim-lang.org/docs/uri.html) |
| CSV | csv | [parsecsv](https://nim-lang.org/docs/parsecsv.html) |
| Parâmetros da linha de comando | argparse | [parseopt](https://nim-lang.org/docs/parseopt.html) |
| SMTP | smtplib | [smtp](https://nim-lang.org/docs/smtp.html) |
| Cookies HTTP | http.cookies | [cookies](https://nim-lang.org/docs/cookies.html) |
| Estatísticas | statistics | [stats](https://nim-lang.org/docs/stats.html) |
| Empacotamento de texto (Text Wrapping) | textwrap | [wordwrap](https://nim-lang.org/docs/wordwrap.html) |
| Registro do Windows | winreg | [registry](https://nim-lang.org/docs/registry.html) |
| POSIX | posix | [posix](https://nim-lang.org/docs/posix.html), [posix_utils](https://nim-lang.org/docs/posix_utils.html) |
| SSL | ssl | [openssl](https://nim-lang.org/docs/openssl.html) |
| CGI | cgi | [cgi](https://nim-lang.org/docs/cgi.html) |
| Profiler | cprofile, profile | [nimprof](https://nim-lang.github.io/Nim/nimprof.html) |
| Tempo monotônico | time.monotonic | [monotimes](https://nim-lang.github.io/Nim/monotimes.html) |
| Executar funções na saída | atexit | [exitprocs](https://nim-lang.github.io/Nim/exitprocs.html) |
| Definir permissões de arquivo | os, stat | [os](https://nim-lang.github.io/Nim/os.html), [filepermissions](https://nim-lang.github.io/Nim/filepermissions.html) |
| Percurso recursivo do sistema de arquivos | os.walk | [os.walkDirRec](https://nim-lang.github.io/Nim/os.html#walkDirRec.i%2Cstring),
[globs.walkDirRecFilter](https://nim-lang.github.io/Nim/globs.html#walkDirRecFilter.i%2Cstring%2Cproc%28PathEntry%29) |
| Mecanismo de modelagem | string.Template | [Source Code Filters](https://nim-lang.github.io/Nim/filters.html) |
| Deques | collections.deque | [deques](https://nim-lang.github.io/Nim/deques.html) |
| Dicionário ordenado baseado na árvore B | :negative_squared_cross_mark: | [btreetables](https://nim-lang.github.io/Nim/btreetables.html) |
| Critical Bit Tree Dict/Set | :negative_squared_cross_mark: | [critbits](https://nim-lang.github.io/Nim/critbits.html) |
| Alocação de memória agrupada | :negative_squared_cross_mark: | [pools](https://nim-lang.github.io/Nim/pools.html) |
| Analisar JSON | json | [parsejson](https://nim-lang.org/docs/parsejson.html), [json](https://nim-lang.org/docs/json.html) |
| Analisar INI | configparser | [parsecfg](https://nim-lang.org/docs/parsecfg.html) |
| Analisar XML | xml | [parsexml](https://nim-lang.org/docs/parsexml.html), [xmltree](https://nim-lang.org/docs/xmltree.html) |
| Analisar HTML | html.parser | [htmlparser](https://nim-lang.org/docs/htmlparser.html) |
| Analisar SQL | :negative_squared_cross_mark: | [parsesql](https://nim-lang.org/docs/parsesql.html) |
| Cores no terminal | :negative_squared_cross_mark: | [terminal](https://nim-lang.org/docs/terminal.html) |
| Detecção de distribuição Linux | :negative_squared_cross_mark: | [distros](https://nim-lang.org/docs/distros.html) |
| Gerador de HTML | :negative_squared_cross_mark: | [htmlgen](https://nim-lang.org/docs/htmlgen.html) |
| Funções de seta (arrow) | :negative_squared_cross_mark: | [sugar](https://nim-lang.org/docs/sugar.html#%3D%3E.m%2Cuntyped%2Cuntyped) |
| In-Place para Work-on-Copy | :negative_squared_cross_mark: | [sugar.dup](https://nim-lang.org/docs/sugar.html#dup.m%2CT%2Cvarargs%5Buntyped%5D) |
| Sintaxe Sugar | :negative_squared_cross_mark: | [sugar](https://nim-lang.org/docs/sugar.html) |
| JavaScript e frontend | :negative_squared_cross_mark: | [dom](https://nim-lang.org/docs/dom.html), [asyncjs](https://nim-lang.org/docs/asyncjs.html),
[jscore](https://nim-lang.org/docs/jscore.html), [jsffi](https://nim-lang.org/docs/jsffi.html),
[dom_extensions](https://nim-lang.github.io/Nim/dom_extensions.html), [jsre](https://nim-lang.github.io/Nim/jsre.html) |

- Isso não está completo, mas apenas uma visão geral rápida. Para obter mais
informações, consulte https://nim-lang.org/docs/lib.html

## Tuplas

As tuplas têm tamanho fixo, começam no índice `0`, podem conter tipos mistos e
podem ser anônimas ou nomeadas. Tuplas nomeadas não têm nenhuma sobrecarga extra
sobre tuplas anônimas.

#### Tupla anônima

```python
(1, 2, 3)
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
(1, 2, 3)
```

#### Tuple Nomeada

- O Nim permite que os campos sejam nomeados, sem exigir que a própria tupla
seja nomeada. O Python NamedTuple requer `import collections`, e precisamos dar
a ele um nome fictício de sublinhado:

```python
collections.namedtuple("_", "key0 key1")("foo", 42)
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
(key0: "foo", key1: 42)
```

#### Tuple Nomeada

- Também podemos nomear os campos e a tupla:

```python
collections.namedtuple("NameHere", "key0 key1")("foo", 42)
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
type NameHere = tuple[key0: string, key1: int]
var variable: NameHere = (key0: "foo", key1: 42)
```

`tuple [key0: string, key1: int] `é o `typedesc` para Declarações.
`(key0: “foo”, key1:42)` é o literal para atribuições.

As tuplas do Nim são muito parecidas com Python NamedTuple, pois os membros da
tupla têm nomes.

NÃO use tuplas nomeadas para “imitar” objetos apropriados (o compilador
reutiliza instanciações genéricas para tuplas “idênticas”).

Veja [manual](http://nim-lang.org/docs/manual.html#types-tuples-and-object-types)
para uma análise mais aprofundada das tuplas.

## Listas

[Nim sequences](http://nim-lang.org/docs/tut1.html#advanced-types-sequences) *não*
são de tamanho fixo. Eles podem crescer e encolher, começar no índice `0` e
devem conter elementos do mesmo tipo.

```python
["foo", "bar", "baz"]
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
@["foo", "bar", "baz"]
```

[@](https://nim-lang.github.io/Nim/system.html#%40%2CopenArray%5BT%5D) é uma
função que converte de `array` para `seq`.

## List Comprehensions

```python
variable = [item for item in (-9, 1, 42, 0, -1, 9)]
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
let variable = collect(newSeq):
  for item in @[-9, 1, 42, 0, -1, 9]: item
```

Uma comprehension também pode ser atribuída a `const` e será executada em tempo
de compilação.

A comprehension é implementada como uma `macro` que é expandida em tempo de
compilação. Você pode ver o código expandido usando a opção de compilador
`—expandMacro`:

```nim
let variable = 
  var collectResult = newSeq(Natural(0))
  for item in items(@[-9, 1, 42, 0, -1, 9]):
    add(collectResult, item)
  collectResult
```

As comprehension podem ser aninhadas, com várias linhas e com várias expressões,
tudo sem sobrecarga:

```nim
import std/sugar

let values = collect(newSeq):
  for val in [1, 2]:
    collect(newSeq):
      for val2 in [3, 4]:
        if (val, val2) != (1, 2):
          (val, val2)
        
assert values == @[@[(1, 3), (1, 4)], @[(2, 3), (2, 4)]]
```

Exemplo de linha única:

```python
print([i for i in range(0, 9)])
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
echo(block: collect newSeq: (for i in 0..9: i))
```

As comprehension de Python convertem o código em um gerador, mas as compreensões
de Nim não convertem o código em um iterador:

```nim
import std/sugar

func example() =
  discard collect(newSeq):
    for item in @[-9, 1, 42, 0, -1, 9]: 
      if item == 0: return
      item

example()
```

:arrow_up: Nim :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Python :arrow_down:

```python
def example():
  [item for item in [-9, 1, 42, 0, -1, 9] if item == 0: return]
      
example()
```

Python reclama:

```
SyntaxError: invalid syntax.
```

Algumas coisas que em Python são sintaticamente proibidas dentro de compreensões
(como `return`) são permitidas no Nim. Isso ocorre porque as compreensões do Nim
são apenas macros que se expandem para o código normal.

- O que é `collect () `?.

[collect](https://nim-lang.github.io/Nim/sugar.html#collect.m%2Cuntyped%2Cuntyped)
takes as argument whatever your returning type uses as the constructor.

## Dict Comprehensions

```python
variable = {key: value for key, value in enumerate((-9, 1, 42, 0, -1, 9))}
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
let variable = collect(initTable(4)):
  for key, value in @[-9, 1, 42, 0, -1, 9]: {key: value}
```

- `collect () `requer [`import std/sugar`.](https://nim-lang.github.io/Nim/sugar.html#collect.m%2Cuntyped%2Cuntyped)

## Set Comprehensions

```python
variable = {item for item in (-9, 1, 42, 0, -1, 9)}
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
let variable = collect(initHashSet):
  for item in @[-9, 1, 42, 0, -1, 9]: {item}
```

- `collect () `requer [`import std/sugar`.](https://nim-lang.github.io/Nim/sugar.html#collect.m%2Cuntyped%2Cuntyped)

## Conjuntos (sets)

| Lang | Conjunto (set) | Set ordenado | Bitset | [Bit Fields](https://en.wikipedia.org/wiki/Bit_field) | Importações |
| --- | --- | --- | --- | --- | --- |
| :snake: Python | `set()` | :negative_squared_cross_mark: | :negative_squared_cross_mark: | :negative_squared_cross_mark: |  |
| :crown: Nim | [`HashSet()`](https://nim-lang.github.io/Nim/sets.html#HashSet) | [`OrderedSet()`](https://nim-lang.github.io/Nim/sets.html#OrderedSet) | [`set`](http://nim-lang.org/docs/manual.html#types-set-type) | [Bit Fields](https://nim-lang.org/docs/manual.html#set-type-bit-fields) | `import std/sets` |

- **O Python set pode ser substituído por [HashSet](http://nim-lang.org/docs/sets.html)
.**

Os conjuntos Python não são como o [tipo de conjunto Nim](http://nim-lang.org/docs/manual.html#types-set-type).
O conjunto “padrão” é um [bitset](https://en.wikipedia.org/wiki/Bitset). Para
cada valor possível do tipo contido, ele armazena 1 bit indicando se ele está
presente no conjunto. Isso significa que você deve usá-lo se o tipo tiver uma
faixa finita e limitada de valores possíveis. Se todos os valores possíveis
também forem conhecidos em tempo de compilação, você poderá criar um `Enum` para
eles.

O maior número inteiro que você pode caber em um conjunto normalmente é `65535`
igual a `high (uint16) `.

Você pode ajustar números inteiros maiores usando um Subrange inteiro, se não
precisar de números inteiros pequenos. Um exemplo realmente estressante de
definir para caber `2_147_483_647` é igual a `high (int32) `em um conjunto em
tempo de compilação:

```nim
const x = {range[2147483640..2147483647](2147483647)}
assert x is set  # Equals to {2147483647}
```

O tipo de conjunto (set) básico do Nim é rápido e economiza memória, em
comparação com o [HashSet](http://nim-lang.org/docs/sets.html), que é
implementado como um dicionário. Para tipos de flags simples e pequenos
conjuntos matemáticos, use set. Para coleções maiores, ou se você está apenas
aprendendo, use o HashSet.

## Dicionários

Use [tables](http://nim-lang.org/docs/tables.html) para dicionários semelhantes
ao Python.

| Lang | Dicionário | Dicionário ordenado | Counter | Importações |
| --- | --- | --- | --- | --- |
| :snake: Python | `dict()` | `OrderedDict()` | `Counter()` | `import std/collections` |
| :crown: Nim | [`Table()`](https://nim-lang.org/docs/tables.html#basic-usage-table) | [`OrderedTable()`](https://nim-lang.org/docs/tables.html#basic-usage-orderedtable) | [`CountTable()`](https://nim-lang.org/docs/tables.html#basic-usage-counttable) | `import std/tables` |

#### Construtores de tabela

```python
dict(key="value", other="things")
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
to_table({"key": "value", "other": "things"})
```

#### Dicionário ordenado

```python
collections.OrderedDict([(8, "hp"), (4, "laser"), (9, "engine")])
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
to_ordered_table({8: "hp", 4: "laser", 9: "engine"})
```

#### Contadores

```python
collections.Counter(["a", "b", "c", "a", "b", "b"])
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
to_count_table("abcabb")
```

**Exemplos: **

```Nim
import std/tables

var dictionary = to_table({"hi": 1, "there": 2})

assert dictionary["hi"] == 1
dictionary["hi"] = 42
assert dictionary["hi"] == 42

assert len(dictionary) == 2
assert dictionary.has_key("hi")

for key, value in dictionary:
  echo key, value
```

As tabelas são apenas açúcar de sintaxe para uma matriz de tuplas:

```nim
assert {"key": "value", "k": "v"} == [("key", "value"), ("k", "v")]
assert {"key": true, "k": false} == @[("key", true),  ("k", false)]
```

#### Tabelas Árvores-B

[Tabelas ordenadas genéricas baseadas em Árvore-B](https://nim-lang.github.io/Nim/btreetables.html)
usando a mesma API.

Veja também:

- [O que é B-Tree? (Wikipédia).](https://en.wikipedia.org/wiki/B-tree)
- [O que é B-Tree? (Vídeo animado de 1 minuto).](https://youtu.be/coRJrcIYbF4)

### Operadores ternários

```python
"result0" if conditional else "result1"
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
if conditional: "result0" else: "result1"
```

Em Nim, o “operador ternário” é simplesmente um `if.. else` em linha. Ao
contrário do Python, o `if.. else` comum é uma expressão, portanto, ele pode ser
atribuído a uma variável. Esses trechos são equivalentes:

```nim
var foo = if 3 < 10:
  50
  else: 100
```

```nim
var foo = if 3 < 10: 50 else: 100
```

## Lendo e escrevendo arquivos

**Lendo arquivos linha por linha**

```python
with open("yourfile.txt", "r") as f:
    for line in f:
        print(line)
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
for line in lines("yourfile.txt"):
  echo line
```

- `lines()` Documentação https://nim-lang.org/docs/io.html#lines.i%2Cstring

**Lendo e gravando arquivos: **

```nim
write_file("yourfile.txt", "this string simulates data")
assert read_file("yourfile.txt") == "this string simulates data"
```

**Lendo arquivos em tempo de compilação: **

```nim
const constant = static_read("yourfile.txt")  # Returns a string at compile-time
```

## Alterar permissões de arquivo

```python
import std/os
os.chmod("file.txt", 0o777)
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
import fusion/filepermissions
chmod "file.txt", 0o777
```

Esses exemplos assumem que existe um arquivo `” file.txt “`. [Ambos usam as
permissões octais de arquivo Unix.](https://en.wikipedia.org/wiki/File-system_permissions#Notation_of_traditional_Unix_permissions)
[Além disso, uma API de nível inferior está disponível no módulo `os`.](https://nim-lang.github.io/Nim/os.html#setFilePermissions%2Cstring%2Cset%5BFilePermission%5D)

Veja https://nim-lang.github.io/fusion/src/fusion/filepermissions.html

## Alterar pasta temporariamente

```python
import std/os

class withDir:
    # Unsafe without a __del__()

    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


with withDir("subfolder"):
  print("Inside subfolder")
print("Go back outside subfolder")
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
import fusion/scripting

withDir "subfolder":
  echo "Inside subfolder"
echo "Go back outside subfolder"
```

Esses exemplos assumem que existe uma pasta `"subfolder"`. Opcionalmente, o
Python tem dependências de terceiros que fazem a mesma coisa; os exemplos usam a
biblioteca padrão. Algumas dependências de terceiros do Python podem converter o
código dentro de `withDir` em um gerador, forçando você a alterar o código (como
`return` para `yield` etc), exemplos usam biblioteca padrão.

Veja https://nim-lang.github.io/fusion/src/fusion/scripting.html

## Map e filter

```python
def isPositive(arg: int) -> bool: 
  return arg > 0

map(isPositive, [1, 2,-3, 5, -9])
filter(isPositive, [1, 2,-3, 5, -9])
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
proc isPositive(arg: int): bool = 
  return arg > 0 

echo map([1, 2,-3, 5, -9], isPositive)
echo filter([1, 2,-3, 5, -9], isPositive)
```

- operações de map e filter requerem [`import std/sequtils`.](https://nim-lang.org/docs/sequtils.html)

## Lambdas

```python
variable: typing.Callable[[int, int], int] = lambda var1, var2: var1 + var2
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
var variable = proc (var1, var2: int): int = var1 + var2
```

Exemplo em várias linhas:

```nim
var anon = func (x: int): bool =
             if x > 0:
               result = true
             else: 
               result = false

assert anon(9)
```

As funções anônimas do Python não podem usar `return`, mas podem no Nim:

```python
example = lambda: return 42
assert example() == 42
```

Reclamações `SyntaxError: sintaxe inválida`.

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
let example = func: int = return 42
assert example() == 42
```

As funções anônimas do Python não podem usar `yield`, mas podem no Nim:

```python
example = lambda: for i in range(0, 9): yield i

for _ in example(): pass
```

Reclamações `SyntaxError: sintaxe inválida`.

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
let example = iterator: int = 
  for i in 0..9: yield i

for _ in example(): discard
```

[Processos anônimos em Nim](https://nim-lang.org/docs/manual.html#procedures-anonymous-procs)
são basicamente funções sem nome.

## Decoradores

- Modelos e macros podem ser usados de forma semelhante aos decoradores do
Python.

```python
def decorator(argument):
  print("This is a Decorator") 
  return argument

@decorator
def function_with_decorator() -> int:
  return 42

print(function_with_decorator())
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
template decorator(argument: untyped) =
  echo "This mimics a Decorator"
  argument

func function_with_decorator(): int {.decorator.} =
  return 42

echo function_with_decorator()
```

- Por que o Nim não usa a sintaxe `@decorator`?.

Nim usa `{.` e`.} `porque pode ter vários decoradores juntos.

Também no Nim, trabalha-se com variáveis e tipos:

```nim
func function_with_decorator(): int {.discardable, inline, compiletime.} =
  return 42

let variable {.compiletime.} = 1000 / 2

type Colors {.pure.} = enum Red, Green, Blue
```

[@](https://nim-lang.github.io/Nim/system.html#%40%2CopenArray%5BT%5D) é uma
função que converte de `array` para `seq`.

## JSON

Python usa strings de várias linhas com JSON interno, Nim usa JSON literal
diretamente no código.

```python
import std/json

variable = """{
    "key": "value",
    "other": true
}"""
variable = json.loads(variable)
print(variable)
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
import json

var variable = %*{
  "key": "value",
  "other": true
}
echo variable
```

- `%*` converte tudo dentro dos colchetes em JSON, o JSON tem um tipo `JsonNode`.
- `%*` pode ter variáveis e literais dentro dos colchetes.
- O JSON pode ter comentários de Nim entre colchetes de `%*`.
- Se o JSON não for um JSON válido, o código não será compilado.
- `JsonNode` pode ser útil no Nim porque é um tipo que pode ter [tipos
mistos](https://nim-lang.github.io/Nim/manual.html#types-object-variants) e pode
crescer/encolher.
- Você pode ler o JSON em tempo de compilação e armazená-lo em uma constante
como uma string.
- Para analisar o JSON a partir de uma string, você pode usar `parseJSON(“{}”) `.
- Para analisar o JSON de um arquivo, use `parseFile(“file.json”) `.
- [Documentação JSON](https://nim-lang.org/docs/json.html)

## Auto-execução do módulo principal

```python
if __name__ == "__main__":
  main()
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
when is_main_module:
  main()
```

## Testes unitários

```python
import std/unittest


def setUpModule():
    """Setup: Run once before all tests in this module."""
    pass

def tearDownModule():
    """Teardown: Run once after all tests in this module."""
    pass


class TestName(unittest.TestCase):
    """Test case description"""

    def setUp(self):
        """Setup: Run once before each tests."""
        pass

    def tearDown(self):
        """Teardown: Run once after each test."""
        pass

    def test_example(self):
        self.assertEqual(42, 42)


if __name__ == "__main__":
    unittest.main()
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
import std/unittest

suite "Test Name":

  echo "Setup: Run once before all tests in this suite."

  setup:
    echo "Setup: Run once before each test."

  teardown:
    echo "Teardown: Run once after each test."

  test "example":
    assert 42 == 42

  echo "Teardown: Run once after all tests in this suite."
```

- [Documentação do Unittest.](https://nim-lang.org/docs/unittest.html)
- [O gerenciador de pacotes Nimble também pode executar Unittests.](https://github.com/nim-lang/nimble#nimble-tasks)
- [O NIMScript também pode executar Unittests.](https://nim-lang.org/docs/nims.html)
- [Você pode executar a documentação como Unittests com `runnableExamples`](https://nim-lang.org/docs/system.html#runnableExamples%2Cuntyped).

#### Assert com mensagens personalizadas

- `assert` pode ter um `block`. Você pode personalizar a mensagem para melhorar
a experiência do usuário:

```nim
let a = 42
let b = 666
doAssert a == b, block:
  ("\nCustom Error Message!:" &
   "\n  a equals to " & $a &
   "\n  b equals to " & $b)
```

### Testamento

Uma alternativa ao `unittest`. Está preparado para grandes projetos e tem mais
funcionalidades.

- https://nim-lang.github.io/Nim/testament.html ** (Recomendado) **

## Docstrings

Docstrings em Nim são comentários reStructuredText *e* MarkDown começando com
`##`. ReStructuredText e MarkDown podem ser misturados, se você quiser.

Gere documentação HTML, Latex (PDF) e JSON a partir do código-fonte com
`nim doc file.nim`.

O Nim pode gerar um gráfico de dependência DOT `.dot` com
`nim genDepend file.nim`.

[Você pode executar a documentação como Unittests com `runnableExamples`](https://nim-lang.org/docs/system.html#runnableExamples%2Cuntyped).

```python
"""Documentation of module"""

class Kitten(object):
    """Documentation of class"""

    def purr(self):
        """Documentation of method"""
        print("Purr Purr")
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
## Documentation of Module *ReSTructuredText* and **MarkDown**

type Kitten = object ## Documentation of type
  age: int  ## Documentation of field

proc purr(self: Kitten) =
  ## Documentation of function
  echo "Purr Purr"
```

## Indentação opcional

Você pode escrever construções como `if.. then` e `try.. except.. finally` em
uma única linha sem erros ou avisos; a indentação é opcional. Obviamente, isso
só é uma boa ideia se o trecho for curto e simples.

```nim
let a = try: 1 + 2 except: 42 finally: echo "Inline try"

let b = if true: 2 / 4 elif false: 4 * 2 else: 0

for i in 0 .. 9: echo i

proc foo() = echo "Function"

(proc   () = echo "Anonymous function")()

template bar() = echo "Template"

macro baz() = echo "Macro"

var i = 0
while i < 9: i += 1

when is_main_module: echo 42
```

## CamelCase

- Por que Nim CamelCase em vez de snake_case?

Realmente não é, Nim é independente de estilo!

```nim
let camelCase = 42      # Declaring as camelCase 
assert camel_case == 42 # Using as snake_case

let snake_case = 1      # Declaring as snake_case
assert snakeCase == 1   # Using as camelCase

let `free style` = 9000
assert free_style == 9000
```

**Esse recurso permite que o Nim interopere perfeitamente com várias linguagens
de programação com diferentes estilos de nomeação. **

Para obter um código mais homogêneo, você pode aplicar um estilo de caixa padrão
usando o comando do compilador `—styleCheck:hint`. Nim *verificará o estilo* do
seu código antes da compilação, semelhante ao `pycodestyle` em Python. Se você
quiser um estilo ainda mais rígido, você pode usar `—styleCheck:error`.

O Nim vem com um formatador automático de código embutido chamado Nimpretty.

Muitas linguagens de programação não diferenciam maiúsculas e minúsculas, como:
PowerShell, SQL, PHP, Lisp, Assembly, Batch, ABAP, Ada, Visual Basic, VB.NET,
Fortran, Pascal, Forth, Cobol, Scheme, Red, Rebol.

Se você está começando do zero, pode usar nomes semelhantes aos do Python
enquanto aprende. Isso não produzirá um erro, a menos que você diga ao
compilador que deseja isso.

## def x proc/func

- Por que Nim não usa `def` em vez de `proc`?.

Nim usa `proc` para funções normais, que é a abreviação de “procedimento”.

Use `func` para quando sua rotina não puder e não deve acessar variáveis globais
ou locais de thread (veja também: [funções puras](https://en.wikipedia.org/wiki/Pure_function)).

[Nim tem rastreamento de efeitos colaterais.](https://nim-lang.github.io/Nim/manual.html#procedures-func)

Você não pode usar `echo` dentro de `func`, porque `echo` muda `stdout`, o que é
um efeito colateral. Em vez disso, use `debugEcho`.

Veja também:

- [Func restrito](https://nim-lang.github.io/Nim/manual_experimental.html#strict-funcs)
- [Rastreamento de gravação para Nim](https://nim-lang.org/araq/writetracking_2.html)

Se você está começando do zero, você pode usar `proc` para todas as funções
enquanto aprende. Isso não dará um erro.

# Assíncrono

O Nim tem a assíncrona embutida há muito tempo. Funciona como você pode esperar
com `async`, `await`, `Future`, etc.

[asyncdispatch](https://nim-lang.org/docs/asyncdispatch.html) é um módulo para
escrever código simultâneo usando a sintaxe `async`/`await`.

`Future` é um tipo (como uma Future em Python ou uma Promise em JavaScript).

`{.async.}` é um pragma que converte funções em assíncronas (como `async def` em
Python).

Vamos converter o asyncio oficial do Python *Hello World* para Nim:

```python
async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")

asyncio.run(main())
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
proc main() {.async.} =
  echo("Hello ...")
  await sleep_async(1)
  echo("... World!")

wait_for main()
```

A assíncrona interna é implementada usando metaprogramação (macros, modelos,
pragmas, etc.).

| Descrição | [AsyncCheck](https://nim-lang.org/docs/asyncfutures.html#asyncCheck%2CFuture%5BT%5D) | [waitFor](https://nim-lang.org/docs/asyncdispatch.html#waitFor%2CFuture%5BT%5D) | [await](https://nim-lang.org/docs/asyncdispatch.html#await%2CT) |
| --- | --- | --- | --- |
| Espera que a Future seja concluída | :negative_squared_cross_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Ignora a Future | :heavy_check_mark: | :negative_squared_cross_mark: | :negative_squared_cross_mark: |
| Retorna o resultado da Future | :negative_squared_cross_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Disponível apenas dentro do async | :negative_squared_cross_mark: | :negative_squared_cross_mark: | :heavy_check_mark: |

- Por que Nim não usa `async def`?.

Async é apenas uma `macro` em Nim, sem necessidade de alterar a sintaxe da
linguagem. É como um decorador em Python, só que mais poderoso.

Também no Nim, a mesma função pode ser assíncrona *e* síncrona ao mesmo tempo,
com o mesmo código, com o mesmo nome.

Em Python, quando você tem uma biblioteca *"foo"*, você pode precisar de `foo`
(sync) e `aiofoo` (async), que geralmente estão em projetos, repositórios,
desenvolvedores e APIs completamente diferentes. Isso não é necessário no Nim,
ou raramente visto, graças a esse recurso.

[Como o async é apenas uma `macro` no Nim, você também pode criar seu
próprio assíncrono do seu jeito.](https://github.com/disruptek/cps#why)

Veja também [asyncfile](https://nim-lang.org/docs/asyncfile.html), [asyncnet](https://nim-lang.org/docs/asyncnet.html),
[asyncstreams](https://nim-lang.org/docs/asyncstreams.html), [asyncftpclient](https://nim-lang.org/docs/asyncftpclient.html),
[asyncfutures](https://nim-lang.org/docs/asyncfutures.html).

# Eu tenho que saber C?

Você nunca precisa realmente editar manualmente o C, da mesma forma que no
Python você nunca edita manualmente os arquivos .pyc.

No Nim, você codifica escrevendo Nim, da mesma forma que em Python você codifica
escrevendo Python.

## Modelos (Templates)

Um modelo substitui sua invocação pelo corpo do modelo em tempo de compilação.

Essencialmente, **o compilador copiará e colará um pedaço de código para você**.

Um modelo nos permite ter construções semelhantes a uma função sem qualquer
sobrecarga ou dividir funções enormes em partes menores.

Muitos nomes de funções e variáveis podem poluir o namespace local. As variáveis
dentro dos modelos não existem fora do modelo. Os modelos não existem no
namespace em tempo de execução (se você não os exportar). Os modelos podem
otimizar determinados valores se forem conhecidos em tempo de compilação.

Os templates *não* podem `importar` nem `exportar` de bibliotecas
automaticamente implicitamente. Os modelos *não* “importam automaticamente”
símbolos usados dentro de si mesmos. Se você usar qualquer biblioteca importada
no corpo de um modelo, deverá importar essa biblioteca ao invocar esse modelo.

Dentro dos modelos, você não pode usar `return` porque um modelo não é uma
função.

Os modelos permitem que você implemente APIs bonitas e de alto nível para o uso
diário, mantendo os detalhes otimizados de baixo nível fora de sua cabeça e
[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

Python `with open (” file.txt “, mode = “r”) as file:` implementado usando um
modelo:

[![Animação explicativa do
modelo](https://raw.githubusercontent.com/juancarlospaco/nim-presentation-slides/master/templates.gif
“Animação explicativa do modelo”)](https://github.com/juancarlospaco/nim-presentation-slides/blob/master/templates.xcf)

O GIF não é perfeito, mas uma aproximação preguiçosa e simplificada!

Essa não é a maneira de ler arquivos no Nim, apenas um exercício.

Este modelo não é perfeito, mas uma aproximação preguiçosa. É um exercício para
o leitor tentar melhorá-lo ;P

```nim
template withOpen(name: string, mode: char, body: untyped) =
  let flag = if mode == 'w': fmWrite else: fmRead  # "flag" doen't exist outside of this template
  let file {.inject.} = open(name, flag)   # Create and inject `file` variable, `file` exists outside of this template because of {.inject.}
  try:
    body                                   # `body` is the code passed as argument
  finally:
    file.close()                           # Code after the code passed as argument

withOpen("testing.nim", 'r'): # Mimic Python with `open("file", mode='r') as file`
  echo "Hello Templates"      # Code inside the template, this 2 lines are "body" argument on the template
  echo file.read_all()        # This line uses "file" variable
```

Se você está começando do zero, não se preocupe, você pode usar funções para
tudo enquanto aprende.

## Como compartilhar variáveis entre funções?

O compartilhamento de variáveis entre funções é semelhante ao Python.

**Variável global: **

```python
global_variable = ""

def function0():
    global global_variable
    global_variable = "cat"

def function1():
    global global_variable
    global_variable = "dog"

function0()
assert global_variable == "cat"
function1()
assert global_variable == "dog"
function0()
assert global_variable == "cat"
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
var global_variable = ""

proc function0() =
  global_variable = "cat"

proc function1() =
  global_variable = "dog"

function0()
assert global_variable == "cat"
function1()
assert global_variable == "dog"
function0()
assert global_variable == "cat"
```

**Atributo do objeto: **

```python
class IceCream:

  def __init__(self):
    self.object_attribute = None

def function_a(food):
    food.object_attribute = 9

def function_b(food):
    food.object_attribute = 5

food = IceCream()
function_a(food)
assert food.object_attribute == 9
function_b(food)
assert food.object_attribute == 5
function_a(food)
assert food.object_attribute == 9
```

:arrow_up: Python :arrow_up: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
:arrow_down: Nim :arrow_down:

```nim
type IceCream = object
  object_attribute: int

proc functiona(food: var IceCream) =
  food.object_attribute = 9

proc functionb(food: var IceCream) =
  food.object_attribute = 5

var food = IceCream()
functiona(food)
assert food.object_attribute == 9
functionb(food)
assert food.object_attribute == 5
functiona(food)
assert food.object_attribute == 9
```

Você pode passar funções como argumentos para outras funções, como em Python.
Funções (procs) são objetos de primeira classe.

### In-Place x Out-Place

Se você estiver migrando de uma linguagem interpretada, como Python ou
JavaScript, você pode encontrar menções estranhas de “In-Place” e “Out-Place” em
algum lugar de Nim. Se você não sabe o que isso significa, parece que o Nim tem
funções duplicadas.

O Python aloca uma nova string ou objeto quando algo nele muda de alguma forma.
Digamos que você tenha uma sequência enorme em uma variável e queira alterar um
único caractere. Como as cadeias de caracteres do Python são imutáveis, a única
solução é duplicar a string na memória, mas com a nova cópia tendo esse
caractere alterado. Devolver uma nova cópia é uma operação “Out-Place”. A maior
parte do Python funciona assim.

Por outro lado, as strings de Nim são mutáveis. No Nim, você pode alterar apenas
o caractere que deseja alterar, em vez de copiar a string na memória. Algumas
funções funcionam no local, outras funcionam em uma nova cópia. A documentação
(geralmente) será qual.

[usando `macro`, o Nim pode passar de uma função in-place para uma
out-place.](https://nim-lang.github.io/Nim/sugar.html#dup.m%2CT%2Cvarargs%5Buntyped%5D)

Os módulos Nim stdlib projetados para o destino JavaScript geralmente funcionam
em uma nova cópia. É assim que o destino do JavaScript é; não há API local nem
benefícios em usá-la.

Alguns módulos Nim stdlib que funcionam em uma nova cópia podem ou não ser
alterados para funcionar no local no futuro.

Exemplos:

```nim
import std/sugar  # sugar.dup

func inplace_function(s: var string) =  # Does not use "string" but "var string"
  s = "CHANGED"

# In-Place algo.
var bar = "in-place"
inplace_function(bar)  ## Variable mutated in-place.
assert bar == "CHANGED"

# Out-Place algo.
assert "out-place".dup(inplace_function) == "CHANGED"  ## Variable mutated on a new copy.
```

## Importar arquivos Nim em Python

- https://github.com/Pebaz/nimporter#nimporter

## Sintaxe Python para Nim

- https://github.com/Yardanico/nimpylib#nimpylib

## Publicar no PYPI

- https://github.com/yglukhov/nimpy/wiki#publish-to-pypi
- https://github.com/sstadick/ponim/blob/master/README.md#nim--python--poetry —
- https://github.com/sstadick/nython#nython

## Compilação silenciosa

Se você quiser que a compilação fique completamente silenciosa (você pode perder
avisos e dicas importantes), você pode adicionar ao comando de compilação
`—hints:off —verbosity:0`.

## Ajuda do compilador

A ajuda do compilador é longa. Para torná-lo mais fácil de usar, apenas os
comandos mais frequentes são mostrados com `—help`. Se você quiser ver a ajuda
completa, você pode usar `—fullhelp`.

## Modos de construção

Quando seu código estiver pronto para produção, você deve usar uma compilação
Release, você pode adicionar ao comando de compilação `-d:release`.

| Característica | Versão de compilação | Compilação de depuração |
| --- | --- | --- |
| Rapidez | Rápido | Lento |
| Tamanho do arquivo | Pequeno | Grande |
| Otimizado | :heavy_check_mark: | :negative_squared_cross_mark: |
| Tracebacks (Pilhas de Rastreamento) | :negative_squared_cross_mark: | :heavy_check_mark: |
| Verificações em tempo de execução | :heavy_check_mark: | :heavy_check_mark: |
| Verificações em tempo de compilação | :heavy_check_mark: | :heavy_check_mark: |
| `assert` | :negative_squared_cross_mark: | :heavy_check_mark: |
| [`doAssert`](https://nim-lang.org/docs/assertions.html#doAssert.t%2Cuntyped%2Cstring) | :heavy_check_mark: | :heavy_check_mark: |

# MicroPython

O Nim compila em C, para que possa ser executado no Arduino e em hardware
similar.

Tem várias estratégias de gerenciamento de memória para atender às suas
necessidades, incluindo gerenciamento manual completo da memória. Os binários
Nim são pequenos quando construídos para o Release e podem caber no pequeno
armazenamento do hardware.

- https://github.com/zevv/nim-arduino
- https://github.com/elcritch/nesper#example-code
- https://gitlab.com/endes123321/nimcdl/tree/master#nimcdl-nim-circuit-design-language
- https://github.com/cfvescovo/Arduino-Nim#arduino-nim
- https://gitlab.com/nimbed/nimbed#nimbed
- https://gitlab.com/endes123321/led-controller-frontend#led-controller-frontend
- https://gitlab.com/jalexander8717/msp430f5510-nim
- https://github.com/mwbrown/nim_stm32f3
- https://github.com/gokr/ardunimo
- https://gitlab.com/NetaLabTek/Arduimesp
- https://ftp.heanet.ie/mirrors/fosdem-video/2020/AW1.125/nimoneverything.webm

# SuperCollider

O SuperCollider é C++, então ele pode ser reutilizado usando o Nim.

Teoricamente, os plug-ins do Nim SuperCollider devem ser tão rápidos quanto o
código C. A metaprogramação de Nim nos permite criar DSLs compatíveis com
LiveCoding.

Alguns projetos para o Nim LiveCoding:

- https://github.com/vitreo12/omni#omni
- https://github.com/capocasa/scnim#scnim---writing-supercollider-ugens-using-nim

#### ABC

Veja [isso](http://rosettacode.org/wiki/Abstract_type#Nim)

## Filosofia

A chave para entender o Nim é que o Nim foi projetado para ser tão rápido quanto
C, mas para ser muito mais seguro. Muitas das decisões de design são baseadas em
tornar mais difícil dar um tiro no próprio pé. Em Python, não há ponteiros (tudo
é tratado como referência). Enquanto o Nim fornece dicas, o Nim oferece outras
ferramentas mais seguras para suas necessidades diárias, enquanto os ponteiros
são principalmente reservados para a interface com C e a programação de sistemas
de baixo nível.

Ao contrário do Python, a maior parte do código Nim pode ser executada em tempo
de compilação para realizar metaprogramação. Você pode fazer muitas das DSLs
possíveis com decoradores/metaprogramação Python com macros e pragmas Nim. (E
algumas coisas que você não pode!). Obviamente, isso requer alguns padrões
diferentes e mais segurança de tipos.

[ :arrow_up: :arrow_up: :arrow_up: :arrow_up: ](#table-of-contents "Ir para o topo")
