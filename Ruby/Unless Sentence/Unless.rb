class Unless
    def initialize()
    end
    def unless()
        age = 29
        unless age < 18
            print "You are not a boy"
        end
        blocked = "Código facilito"
        unless blocked == "Juan"
            print "\nWelcome to the party"
        end
    end
end

object = Unless.new()
object.unless()
gets()