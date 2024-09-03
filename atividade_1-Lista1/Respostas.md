# Lista de Exercícios 1 – Processamento Gráfico

Nome: Bruno da Siqueira Hoffmann

Professora: Rossana Baptista Queiroz

## Questão 1

**Questão:** O que é a GLSL? Quais os dois tipos de shaders são obrigatórios no pipeline programável da versão atual que trabalhamos em aula e o que eles processam? 

**Resposta:** A GLSL é uma linguagem de programação para escrever shaders, de modo que ela é semelhante ao `C-Style`, possibilitando uso de diferentes estruturas de controle. Além disso, os programas escritos em GLSL serão executados diretamente na GPU, a medida que otimiza o processo e tira a carga da CPU para fazer o processamento do mesmo.

Com relação aos tipos de Shaders que são obrigatórios no pipeline programável e que trabalhamos em aula, temos o Vertex shading e o Fragment shading. O Vertex shading será responsável por manipular as coordenadas em um espaço 3D, identificando onde cada elemento está no espaço. Como entrada esse processo de shading recebe as informações dos vértices, e como saída os dados processados, contendo a posição do vértice. Ele vai ser responsável por dar um valor a variável `gl_Position`.

O outro shader obrigatório visto em aula foi o Fragment shading, sendo ele responsável por definir as cores de cada um dos fragmentos. Sua entrada consiste nos dados passados de outros shaders (podendo ou não ser o Vertex Shader), e sua saída consiste na cor final do fragmento. Ele vai ser responsável por dar um valor a variável `gl_FragColor`.

Referência: 
- https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)

- https://developer.mozilla.org/en-US/docs/Games/Techniques/3D_on_the_web/GLSL_Shaders

## Questão 2

**Pergunta:** O que são primitivas gráficas? Como fazemos o armazenamento dos vértices na OpenGL?

**Resposta:**