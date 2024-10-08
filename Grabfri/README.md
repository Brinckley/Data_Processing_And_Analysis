# Grabfi

## Team:
- Мария Лагуткина, группа М8О-209М-23 (168420440)
- Савин Александр, группа М8О-214М-23 (220523027)
- Свинаренко Владислав, группа М8О-209М-23 (50933461)
- Хренникова Ангелина, группа М8О-209М-23 (198216820)

## Graph:

![img](https://github.com/Brinckley/Data_Processing_And_Analysis/blob/main/Grabfri/full_graph_img.png)

## Parsing friends of friends ids and building graph

First of all you need to get Auth token. You can go [here](https://vkhost.github.io/) and select **Kate Mobile** option. Check the URL for the *access_token=* field.

Create the *token.txt* file in the *Grabfri* project and paste the token there.

Put all wanted ids in the *user_ids.txt* file. You should use only numeric ids!
Install the requirements and start the program.

```
Calculating closeness eigenvector of graph
User name 168420440 with value 0.0001696388076520314
User name 1931147 with value 8.862445238078442e-06
User name 290530655 with value 7.3205986483760225e-06
User name 711398942 with value 2.775535324668156e-06
User name 198216820 with value 2.7011192399565775e-06
User name 207227130 with value 5.432620061853274e-07
User name 220523027 with value 3.120922571567494e-07
User name 172244589 with value 2.5348264073660236e-07
User name 50933461 with value 6.268539046451648e-08
User name 24435047 with value 3.007728155439675e-08
User name 176183602 with value 2.787633158855468e-08
User name 268235974 with value 1.7605222469915988e-08
User name 65657314 with value 1.5365275836726827e-08

Calculating closeness centrality of graph
User name 290530655 with value 0.28206211595020975 
User name 1931147 with value 0.25398657547586184 
User name 207227130 with value 0.2559194607779892 
User name 24435047 with value 0.23501129248920674 
User name 172244589 with value 0.22603612553741215 
User name 168420440 with value 0.28148570611968426 
User name 711398942 with value 0.28851918463211657 
User name 50933461 with value 0.24419692864951206 
User name 198216820 with value 0.28461959980663787 
User name 268235974 with value 0.24005085848329685 
User name 220523027 with value 0.2559580362495971


Calculating betweenness centrality of graph
User name 290530655 with value 0.00035339276655577123
User name 1931147 with value 4.341531166573986e-06
User name 207227130 with value 1.6048417819547467e-05
User name 24435047 with value 1.0923818081209902e-06
User name 172244589 with value 1.2178063002465933e-08
User name 168420440 with value 0.0006250250735320151
User name 711398942 with value 0.0009039243450388312
User name 50933461 with value 8.042872650548816e-06
User name 198216820 with value 0.0004964881227351725
User name 268235974 with value 1.241450536326738e-05
User name 220523027 with value 1.965944466064684e-05


```
