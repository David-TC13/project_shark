# 1. Project_shark_attacks:

## Context:

In 1946 the UN created the office of the [World Tourism Organization](https://www.unwto.org) with the idea of "seeking to position tourism as a policy priority, lead in knowledge creation, enhance the Organization’s capacity through building new and stronger partnerships, and offer better value for existing Members while also expanding membership."

With this idea, it was developed 5 pilars, which one concerning would be no. 5: "harnessing tourism’s unique potential to protect cultural and natural heritage and to support communities both economically and socially.

Relating this pilar with the dataframe we wanted to analyse if the tourism is related with the shark attack as way to analyse if there's an invasion of their environment due to the tourism.

According to it, we analyze summer as peak season of both hemispheres for tourism; in this case, for the northern countries we describe summer as months between June to August, meanwhile, in the southern hemisphere, goes in between December to February.

Also, from the data reported, we focus our attention since 1946, when UNWTO was created, as context to see if their values can be that affected to it.

[summer as peak season](https://www.utmsjoe.mk/files/Vol.%207%20No.%201/UTMSJOE-2016-0701-07-Corluka-Mikinac-Milenkovska.pdf)



## Methods:

As described before we remove all duplicates, data with empty values and those ones collected before 1946. After this first 'clearance', we removed all the columns which were not necessary for our analysis, keeping just the dates, years and Country.

On the other side, to determine if a country of the ones of the dataframe was from the northern or southern hemisphere, we got another .csv file which describes their coordinates so, with a loop filter which one belongs to the southern hemisphere and which one from the north.

Once, we got this, we decribe in which season happened every incident according to the country and the month when happened for, then, compare summer season with the other seasons, by hemisphere, and, together.

## Results:

We can check byt the results obtained, summer is by far, the season with more attacks comparing the others, so, we can expeculate that tourism has a strong influence on those attacks (pending further investigations).
