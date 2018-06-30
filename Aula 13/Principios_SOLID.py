# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:49:51 2018

@author: Lourenço Neto
"""

"""
Este arquivo Py somente será de comentário, falando a respeito do Projeto de CES-22 deste que vos fala, o NewsCrawler,
E verificar o encaixe do Projeto nos Príncipios SOLID de Design Pattern

Single Responsability: As etapas desenvolvidas realmente possuem uma única "razão de existir"

    Web Scrapper: Ele é o único que mexe nas páginas da web para captação de informações relativas a notícias
    Classificadores: Neste caso, os classificadores foram desenvolvidos na linguagem Julia. Se os mesmos fossem importados para Python, cada um seria responsável pela classificação conforme o modelo que o mesmo se baseiou.
                     Ou seja, seria uma classe para o Unigrama, outro para o Bigrama e um para o Trigrama. Sendo assim, para cada modelo, existe um único classificador responsável
    Aplicação Flask: O arquivo app.py é responsável por fazer o programa funcionar, permitindo que o usuário consiga interagir com as interfaces desenvolvidas
                     O arquivo home.py é responsável por gerenciar o roteamento de urls, que criará interfaces com o qual o usuário realmente quer interagir baseado na interação anterior com a última interface.
                     Os templates são responsáveis por definir como a interface irá aparecer para o usuário.
                     
Open Closed Design: O projeto atende razoavelmente esse quesito, visto que existe uma classe específica para dar o "run" no programa, mas ela só importa as classes do programa home.py para funcionar.
                    No entanto, é bem fácil fazer as modificações no último arquivo, uma vez que se tenha acesso ao arquivo do mesmo. Logo, ele é aberto ao uso, mas não é exatamente fechado para modificações.
                    
Linskov Substitution: Os programas não foram desenvolvidos com a interface de classe especificamente. Então, não tem a relação entre subclasse e classe.
                      Caso todo o programa fosse convertido para classe e ter uma main usando todas elas, a única que geraria subclasses seria a aplicação Flask que, à medida que mais databases fossem usadas e roteamento, maior seria a funcionalidade da classe pai.
                      Logo, esse ponto não foi levado em conta, mas sua essência se mantém no projeto.
                      
Interface Segretation: Novamente, como a criação do projeto não foi dividido exatamente com o uso de classes, essa análise não será feito ao pé da letra:
                       As interfaces geradas por cada etapa do projeto realmente são únicas e essenciais para atender a responsabilidade de cada uma delas.
                       No entanto, o programa home.py seria uma classe muito poderosa, pois ela determina todo o processo de interação do usuário com o site. Logo, esse quesito não foi atendido.

Dependency Injection: Os detalhes de cada etapa do projeto eram altamente dependentes da abstração necessárias para sua funcionalidade:
    
    Web Scrapper: Os detalhes necessários para sua implementação dependiam de como os dados estavam dispostos e como eles precisavam ser armazenados
    Classificadores: Os detalhes de cada classificador dependem de como aquele classificador precisaria retornar o resultado baseado no seu modelo
    Aplicação Flask: Os detalhes da aplicação dependiam de como as informações iam ser dispostas. Isso inclui os dados necessários e sua forma de exposição
    
"""