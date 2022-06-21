Factory Method
O padrão Factory Method possui a seguinte intenção:
“Definir uma interface para criar um objeto, mas deixar as subclasses decidirem que classe instanciar. O Factory Method permite adiar a instanciação para subclasses.” 
Ou seja, ao invés de criar objetos diretamente em uma classe concreta, nós definimos uma interface de criação de objetos e cada subclasse fica responsável por criar seus objetos. Seria como se, ao invés de ter uma fábrica de carros, nós tivéssemos uma fábrica da Fiat, que cria o carro da Fiat, uma fábrica da Ford, que cria o carro da Ford e etc.

A principal vantagem em utilizar o padrão Factory Method é a extrema facilidade que temos para incluir novos produtos. Não é necessário alterar NENHUM código, apenas precisamos criar o produto e a sua fábrica. Todo o código já escrito não será alterado.
No entanto isto tem um custo. Perceba que criamos uma estrutura relativamente grande para resolver o pequeno problema, temos um conjunto grande de pequenas classes, cada uma realizando uma operação simples. Apesar de seguir o princípio da responsabilidade única, para cada novo produto precisamos sempre criar duas classes, uma produto e uma fábrica.
Na primeira sugestão de implementação nós definimos o Factory Method em uma classe concreta, isso evita a criação de várias classes pequenas de fábrica, no entanto acaba criando um código gigante para criação de objetos. Durante a implementação é necessário escolher qual tipo de implementação resolve melhor o seu problema.

Aplicabilidade
O Factory Method separa o código de construção do produto do código que realmente usa o produto. Portanto, é mais fácil estender o código de construção do produto independentemente do restante do código.

Por exemplo, para adicionar um novo tipo de produto à aplicação, só será necessário criar uma nova subclasse criadora e substituir o método fábrica nela.


Economizar recursos
Use o Factory Method quando deseja economizar recursos do sistema reutilizando objetos existentes em vez de recriá-los sempre.

Você irá enfrentar essa necessidade ao lidar com objetos grandes e pesados, como conexões com bancos de dados, sistemas de arquivos e recursos de rede.

Vamos pensar no que deve ser feito para reutilizar um objeto existente:

Primeiro, você precisa criar algum armazenamento para manter o controle de todos os objetos criados.
Quando alguém solicita um objeto, o programa deve procurar um objeto livre dentro desse conjunto.
...e retorná-lo ao código cliente.
Se não houver objetos livres, o programa deve criar um novo (e adicioná-lo ao conjunto de objetos).
Isso é muito código! E tudo deve ser colocado em um único local para que você não polua o programa com código duplicado.

Provavelmente, o lugar mais óbvio e conveniente onde esse código deve ficar é no construtor da classe cujos objetos estamos tentando reutilizar. No entanto, um construtor deve sempre retornar novos objetos por definição. Não pode retornar instâncias existentes.

Portanto, você precisa ter um método regular capaz de criar novos objetos e reutilizar os existentes. Isso parece muito com um método fábrica.



Prós 
Você evita acoplamentos firmes entre o criador e os produtos concretos.

Princípio de responsabilidade única. Você pode mover o código de criação do produto para um único local do programa, facilitando a manutenção do código.

Princípio aberto/fechado. Você pode introduzir novos tipos de produtos no programa sem quebrar o código cliente existente.

Contras
O código pode se tornar mais complicado, pois você precisa introduzir muitas subclasses novas para implementar o padrão. O melhor cenário é quando você está introduzindo o padrão em uma hierarquia existente de classes criadoras.


Relações com outros padrões
Muitos projetos começam usando o Factory Method (menos complicado e mais customizável através de subclasses) e evoluem para o Abstract Factory, Prototype, ou Builder (mais flexíveis, mas mais complicados).

Classes Abstract Factory são quase sempre baseadas em um conjunto de métodos fábrica, mas você também pode usar o Prototype para compor métodos dessas classes.

Você pode usar o Factory Method junto com o Iterator para permitir que uma coleção de subclasses retornem diferentes tipos de iteradores que são compatíveis com as coleções.

O Prototype não é baseado em heranças, então ele não tem os inconvenientes dela. Por outro lado, o Prototype precisa de uma inicialização complicada do objeto clonado. O Factory Method é baseado em herança mas não precisa de uma etapa de inicialização.

O Factory Method é uma especialização do Template Method. Ao mesmo tempo, o Factory Method pode servir como uma etapa em um Template Method grande.