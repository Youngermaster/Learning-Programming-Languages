class Lambdas
    def initialize
    end
    def lambdas
        #########################################
        # First example
        firstLambda = lambda {"Hello Lambda"}
        puts "\nFirst example\n" + firstLambda.call
        #########################################
        # Second example
        puts "\nSecond example\n"
        secondLambda = lambda { |number| number + 3}
        puts secondLambda.call 5
        #########################################
        # Third example
        # do when is more than one line
        puts "\nThird example\n"
        thirdLambda = lambda do |name|
            if name == "Juan"
                return "Excelente"
            else 
                return "Mmm... ok"
            end
        end
        puts thirdLambda.call "Juan"
    end
end

object = Lambdas.new
object.lambdas