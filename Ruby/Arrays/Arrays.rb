class Arrays
    def initialize()
    end
    def Arrays()
        ########################
        #First option
        array = [1,2,3]
        
        for i in(0..2)
            puts array[i]
        end
        ########################
        #Second option
        array<<"Nuevo valor"
        puts array[-1]
        ########################
        #Third option
        array.push("Last value")
        puts array[-1]
        puts array[-5]
    end
end

object = Arrays.new()
object.Arrays()
gets()