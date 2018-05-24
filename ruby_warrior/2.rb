class Player
  def play_turn(warrior)
    warrior.feel.empty? ? warrior.walk! : warrior.attack!
  end
end