class Player
  def play_turn(warrior)
    cur_h = warrior.health
    if warrior.feel.empty?
      if cur_h < 20 and not cur_h < @health
        warrior.rest!
      else
        warrior.walk!
      end
    else
      if warrior.feel.captive?
        warrior.rescue!
      else
        warrior.attack!
      end
    end
    @health = warrior.health
  end
end