class DataInputChomp
    def initialize()
    end
    def WhithChomp()
        puts "Give me your name: "
        name2 = gets.chomp
        puts "Hola " + name2
    end
end

object = DataInputChomp.new()
object.WhithChomp()
gets()