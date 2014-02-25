
  def countChange(money: Int, coins: List[Int]): Int = {
    def count(m: Int, cs: List[Int]): Int =
      if (cs.isEmpty || m < 0) 0
      else if (m == 0) 1
      else count(m, cs.tail) + count(m - cs.head, cs)
    if (money == 0) 1
    else count(money, coins.sortWith(_ > _))
  }
  countChange(200,List(1,2,5,10,20,50,100,200))