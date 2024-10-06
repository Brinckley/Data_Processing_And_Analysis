# Grabfi

## Team:
- Мария Лагуткина, группа М8О-209М-23 (168420440)
- Савин Александр, группа М8О-214М-23 (220523027)
- Свинаренко Владисла, группа М8О-209М-23 (50933461)
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
User name 168420440 with value 0.0001198045257558153
User name 198216820 with value 2.405864785156243e-06
User name 220523027 with value 2.281481752383861e-07
User name 50933461 with value 5.119506057853398e-08

Calculating closeness centrality of graph
User name 168420440 with value 0.0001198045257558153
User name 198216820 with value 2.405864785156243e-06
User name 220523027 with value 2.281481752383861e-07
User name 50933461 with value 5.119506057853398e-08

Calculating betweenness centrality of graph
User name 168420440 with value 0.0001198045257558153
User name 198216820 with value 2.405864785156243e-06
User name 220523027 with value 2.281481752383861e-07
User name 50933461 with value 5.119506057853398e-08

```
