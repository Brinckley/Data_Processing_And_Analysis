# Grabfi

## Team:
- Мария Лагуткина, группа М8О-209М-23
- Савин Александр, группа М8О-214М-23
- Свинаренко Владисла, группа М8О-209М-23
- Хренникова Ангелина, группа М8О-209М-23

## Graph:

![img](https://github.com/Brinckley/Data_Processing_And_Analysis/blob/main/Grabfri/AllPhotos/BaseGraph/image_2024-09-30_19-45-33.png)

## Parsing friends of friends ids and building graph

First of all you need to get Auth token. You can go [here](https://vkhost.github.io/) and select **Kate Mobile** option. Check the URL for the *access_token=* field.

Create the *token.txt* file in the *Grabfri* project and paste the token there.

Put all wanted ids in the *user_ids.txt* file. You should use only numeric ids!
Install the requirements and start the program.

```
Calculating closeness eigenvector of graph
User name 268235974 Руся Яминов with value 0.5315008023247143
User name 207227130 Матвей Волков with value 0.13127455250525
User name 168420440 Мария Лагуткина with value 0.10711856944502657
User name 150078285 Семён Бугреев with value 0.08712075450705842
User name 7894249 Денис Махачев with value 0.08088789838178014
 
Calculating closeness centrality of graph
User name Руся Яминов 
User name Мария Лагуткина
User name Матвей Волков
User name Ангелина Хренникова
User name Ирфан Алимов

Calculating betweenness centrality of graph
User name Руся Яминов 
User name Мария Лагуткина
User name Ангелина Хренникова
User name Матвей Волков
User name Ирфан Алимов
```
