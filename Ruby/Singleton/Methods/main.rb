require_relative 'Dog.rb'

newDog = Dog.new "GG", "chichi"
newDog2 = Dog.new "Boby", "Ukulele"

def newDog.speak
    return 'Hello human'
end

puts newDog.speak