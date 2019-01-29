class Case
    def initialize()
    end
    def case()
        age = 17
        name = "Juan"
        case age
            when 0..11 then print "Is a boy"
            when 12..17 then print "Is a teen"
            when 18..29 then print "Is an young"
            when 30..59 then print "Is an adult"
            when 60..150 then print "Is too older"
            else print "Error"
        end

        #############################################
        #Another way to do it.
        answer = case age
            when 0..11 then "Is a boy"
            when 12..17 then "Is a teen"
            when 18..29 then "Is an young"
            when 30..59 then "Is an adult"
            when 60..150 then "Is too older"
            else "Error"
        end
        print "\n" + answer

        #############################################
        #Another way to do it.
        answer = case name
            when "Juan", "Manuel", "Young", "Hoyos" then "Papasote"
            else "Na too ugly"
        end
        print "\n" + answer
    end
end

object = Case.new()
object.case()
gets()