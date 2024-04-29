Feature: Procura em grafo utiliza A*

Scenario Outline: Encontrar um caminho em um grafo do arquivo "mini_map.txt" 
Given a descrição de um grafo a partir do arquivo "mini_map.txt"
    And vértice inicial é <start>
    And vértice final é <goal>
When eu procuro o menor caminho com o algoritmo A*
Then o número de vértices analisados é <count>
    And o caminho encontrado é <path>
Examples:
    | start | goal | count | path            |
    |   0   |  7   |   5   | [0, 2, 5, 7] |
    |   0   |  9   |   2   | [0, 9] |
    |   3   |  7   |   3   | [3, 5, 7] |
    |   0   |  6   |   5   | [0, 2, 5, 6] |
    |   6   |  0   |   4   | [6, 5, 2, 0] |

Scenario Outline: Encontrar um caminho em um grafo do arquivo "small_map.txt" 
Given a descrição de um grafo a partir do arquivo "small_map.txt"
    And vértice inicial é <start>
    And vértice final é <goal>
When eu procuro o menor caminho com o algoritmo A*
Then o número de vértices analisados é <count>
    And o caminho encontrado é <path>
Examples:
    | start | goal | count | path            |
    |   0   | 764  |  148  | [0, 709, 710, 712, 714, 716, 718, 722, 727, 730, 734, 738, 743, 744, 748, 751, 752, 755, 758, 762, 763, 764] |
    |   230 | 850  |  133  | [230, 229, 228, 227, 226, 225, 218, 217, 216, 215, 214, 213, 895, 887, 884, 883, 873, 872, 871, 870, 852, 851, 850] |
    |   0   |  20  |   7   | [0, 16, 17, 18, 19, 20] |
    |   0   |   6  |   5   | [0, 2, 5, 6] |
