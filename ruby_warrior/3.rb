class Player
  def play_turn(warrior)
    @warrior = warrior
    warrior.feel.empty? ? walk_or_rest : warrior.attack!
  end
  
  def walk_or_rest
    if @warrior.health < 20
      @warrior.rest!
    else
      @warrior.walk!
    end
  end
end