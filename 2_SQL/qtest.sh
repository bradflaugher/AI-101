q -H -d "," "SELECT COUNT(DISTINCT(CountryName)) FROM ./gdp.csv"

q -d "," "SELECT p.c1,g.c2,p.c3,g.c2/p.c3 FROM gdp.csv g LEFT JOIN pop.csv p ON (g.c1 = p.c2) ORDER BY c3 desc"