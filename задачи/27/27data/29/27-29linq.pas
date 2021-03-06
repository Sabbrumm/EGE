// На основе решения А. Богданова
const B = 5;
const D = 0;
begin
  var data := Readlines('27-29b.txt').Select(s->s.ToIntegers).ToArray;
  var n := data[0].First;
  var triples := data.Skip(1).Take(n).Select(x->|x[0]+x[1], x[0]+x[2], x[1]+x[2]|); 
  var sum := triples.Sum(x->x.Max);
  triples.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на B
               .Select(x->x.Max)    // из каждой группы выбрать максимальное
               .ToArray)
    .Where(x->x mod B <> D)
    .Max
    .Print;      
end.


