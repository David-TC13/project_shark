# 1. Project_shark_attacks:

## Context:

In 1946 the UN created the office of the [World Tourism Organization](https://www.unwto.org) with the idea of "seeking to position tourism as a policy priority, lead in knowledge creation, enhance the Organization’s capacity through building new and stronger partnerships, and offer better value for existing Members while also expanding membership."

With this idea, they were developed 5 pilars, the no. 5 would be concerning: "harnessing tourism’s unique potential to protect cultural and natural heritage and to support communities both economically and socially".

Relating this pilar with the dataframe, we wanted to analyse if the tourism is related with the shark attack as way to analyse if there's an invasion of their environment due to the tourism.

According to it, we highlighted summer as peak season of both hemispheres for tourism; in this case, for the northern countries we describe summer as months from June to August, meanwhile, in the southern hemisphere, goes from December to February.

Also, from the data reported, we focused our attention since 1946, when UNWTO was created, as context to see if their values can affect the natural heritage.

[summer as peak season](https://www.utmsjoe.mk/files/Vol.%207%20No.%201/UTMSJOE-2016-0701-07-Corluka-Mikinac-Milenkovska.pdf)



## Methods:

As described before, we remove all the data which is not useful for our analysis; to do so, we used function like .drop to remove the columns by their label, .dropna for data with empty values( in this case we adjust to  rows with all empty values), and those ones were duplicated by its function (.duplicate).
Also, removed those rows with year before 1946, due to our hypothesis, keeping in total the columns: Date, Year, Country.

After this first step, it was also used another dataframe(from a .csv file) which included the latitude, longitude of each country with the objetive to determine to which hemisphere belonged each country listed in the original dataframe, for, ultimately, determine in which season happened each incident analyzed.

For checking the season we create two functions with dictionaries with the months as keys and the season as values; creating two subsets (one per hemisphere) applying those functions according to the hemisphere they belonged.

Finally, the last step of the analysis was checking in a barplot the different seasons (per hemisphere and in total) to determine if the criteria was met or not.

## Results:

We can determine that there's a bigger amount of shark attacks during the summer in both hemispheres than during the rest of the seasons. 

We noticed as well, a bigger amount of attacks happens in the North hemisphere than the South, which contradicts the traditional view.

Eventhough, our Hypothesis confirms the fact that sharks attacks occured more during the summer season, we can't confirm if this is due to tourism.
![South](https://user-images.githubusercontent.com/115069379/215608801-5b5df5f8-1a4c-4b69-9292-54e3950673d7.jpg) Southern countries

![North](https://user-images.githubusercontent.com/115069379/215608708-2f5420f3-c8df-4d49-b624-f258cad143af.jpg) Northern countries

