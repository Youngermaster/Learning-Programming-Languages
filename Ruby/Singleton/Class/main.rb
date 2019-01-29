require_relative 'Dog.rb'

newDog = Dog.new "GG", "chichi"
newDog2 = Dog.new "Boby", "Ukulele"
differentDog = Dog.new "Young", "Juan"

class << differentDog
    def speak
        return "I'm different, hello human"
    end
end

puts differentDog.speak

if newDog.respond_to?(:speak) then 
    puts differentDog.speak
else
    puts "This dog does'nt know how to speak"
end