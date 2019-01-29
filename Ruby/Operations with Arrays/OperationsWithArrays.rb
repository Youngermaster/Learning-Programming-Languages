class OperationWithArrays
    def initialize()
    end
    def opWithArrays()
        example = [0,1,2,3,4,5,6,7,8,9]

        ######################
        #Firts way
        for y in example
            puts example[y]
        end
        ######################
        #Second way
        puts "Second way"
        example.each do |y|
            puts y
        end

        ######################
        #Third way
        puts "Third way"
        example.map { |y| y + 1}
    end
end

object = OperationWithArrays.new()
object.opWithArrays()
gets()