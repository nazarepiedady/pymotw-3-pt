=======
 Texto
=======

A classe ``str`` é a ferramenta de processamento de texto mais óbvia disponível aos programadores da Python, mas existem muitas outras ferramentas na biblioteca padrão para tornar a manipulação de texto avançada simples.

Os programas podem usar ``string.Template`` como uma maneira simples de parametrizar sequências de caracteres para além das funcionalidades dos objetos da ``str``. Apesar de não ser tão rico em funcionalidades quanto os modelos definidos por muitas das abstrações da Web ou módulos de extensão disponíveis a partir do Índice de Pacote de Python, ``string.Template`` é um bom meio-termo para os modelos modificáveis pelo utilizador, nos quais os valores dinâmicos precisam ser inseridos de outra maneira seriam texto estático.

O módulo :mod:`textwrap` inclui ferramentas para formatar texto de parágrafos, limitando a largura da saída, adicionando indentação, e inserindo quebras de linha para envolver as linhas de maneira consistente.

A biblioteca padrão inclui dois módulos para comparação de valores de texto que vão além da comparação de igualdade e ordenação embutida suportada por objetos de sequência de caracteres. :mod:`re` fornece uma biblioteca de expressão regular completa, implementada em C para maior velocidade.  As expressões regulares são adequadas para encontrar subsequências de caracteres dentro dum conjunto de dados maior, comparar sequências de caracteres contra um padrão mais complexo do que outra sequência de caracteres fixa e análise sintática suave.

:mod:`difflib`, em contraste, calcula as diferenças reais entre sequências de texto em termos das partes adicionadas, removidas, ou alteradas. A saída das funções de comparação em :mod:`difflib` pode ser usada para fornecer uma resposta mais detalhada ao utilizador sobre onde ocorrem as alterações em duas entradas, como um documento foi alterado ao longo do tempo, e assim por diante.

.. toctree::
   :maxdepth: 1

   string/index
   textwrap/index
   re/index
   difflib/index
