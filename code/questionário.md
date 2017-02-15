Respostas às questões:

1- Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?

Você poderia usar diferentes máquinas executando o mesmo código, cada uma com um subconjunto dos 100 sites ou poderia programar de maneira a criar diferentes processos dentro da mesma máquina, cada processo acessaria um subconjunto dos 100 sites.

2- Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.

Você poderia tentar buscar a url do serviço de onde vem os preços, assumindo que essa url está na página HTML, ou se você tiver acesso às requisições que esse site faz. Assim você poderia seguir as URLs.

3- Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?

Descobriria os limites de tempo de acesso impostos por cada site e colocaria um timer para que, sempre que chegar perto do limite, parar o processo e aguardar o tempo estipulado para recomeçar o processo. Mas isso certamente tornaria o processo total mais lento, então outra solução seria trocar o ip da máquina (ou trocar de máquina) que está fazendo os acessos, dado que o mecanismo de segurança provavelmente bloquearia o IP que está acessando.

4- Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?

O primeiro passo é identificar se há algum problema com o crawler, por exemplo, se ele está comprimindo os dados que pega ou se os está pegando no tamanho natural, e corrigir esses problemas. Depois combinaria com o cliente ou com o prestador de serviços de infraestrutura algumas políticas para o crawler funcionar, por exemplo a periodicidade de acesso, que poderia ser reduzida (rodar o crawler 1 vez por semana ou por mês, por exemplo), executar o crawler em horários que o site possui menos acessos, por exemplo, de madrugada. E sempre explicar que existe um custo de resgatar esses dados via crawler e que os dados obtidos e o poder deles para o negócio ultrapassa os custos com a infra que o crawler pode gerar. 
