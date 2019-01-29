class IfSentence
    def intitialize()
    end
    def ifSentence()
        hour = 23
        if hour < 12 
            puts "Good Morning" 
        end
        if  hour >= 12 && hour < 18
            puts "Good afternoon"
        else hour >= 18 && hour <= 24
            puts "Good night"
        end
        ####################################
        puts "\n"
        number = 3
        number2 = 1
        if number == 177
            puts "The number is one hundred seventy seven.\n:D\n"
        else
            puts "The number is not one hundred seventy seven.\n"
        end

        if not number2 == 2 
            puts "The variable is incorrect"
        end

        if number == 3 and number2 > 0 or not number2 == 2
            puts "correct"
        else
            puts "incorrect"
        end
    end
end

object = IfSentence.new()
object.ifSentence()
gets()