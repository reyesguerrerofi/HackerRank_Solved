
/*Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to 
buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power 
of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same 
power, sort the result in order of descending age.


Input Format

The following tables contain data on the wands in Ollivander's inventory:

Wands: The id is the id of the wand, code is the code of the wand, 
coins_needed is the total number of gold galleons needed to buy the wand, 
and power denotes the quality of the wand (the higher the power, the better the wand is). 

Wands_Property: The code is the code of the wand, age is the age of the wand, and is_evil 
denotes whether the wand is good for the dark arts. If the value of is_evil is 0, it means that 
the wand is not evil. The mapping between code and age is one-one, meaning that if there are two pairs
*/

SELECT A.ID,B.AGE,A.COINS_NEEDED,A.POWER FROM WANDS A
INNER JOIN WANDS_PROPERTY B 
ON A.CODE = B.CODE
WHERE B.IS_EVIL = 0 AND A.COINS_NEEDED = (SELECT MIN(COINS_NEEDED) FROM WANDS C 
INNER JOIN WANDS_PROPERTY D 
ON C.CODE = D.CODE
WHERE C.POWER = A.POWER AND D.AGE = B.AGE )
ORDER BY A.POWER DESC, B.AGE DESC

/*Explicación
La varita debe ser buena B.is_evil = 0
La cantidad de monedas necesarias debe ser el minimo de las varitas con el mismo poder y la misma edad
A.coind_needed = (select min(coins_needed) from wands C join wands_property D 
on c.code = d.code
where c.powe = a.powe and d.age = b.age) en este caso las varitas de este select interno deben ser iguales 
a las varitas buenas del select principal */