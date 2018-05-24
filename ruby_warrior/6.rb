class Player
  def play_turn(warrior)
    cur_h = warrior.health
    if not @resc_captive
      if warrior.feel(:backward).empty?
        warrior.walk! :backward
      else
        warrior.rescue! :backward
        @resc_captive = true
      end
    else
      if warrior.feel.empty?
        warrior.walk!
      else
        warrior.attack!
      end
      @health = warrior.health
    end
    
    
  end
end