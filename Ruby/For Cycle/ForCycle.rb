class ForCycle
    def initialize()
    end
    def forcycle()
        ##############################
        #First case
        for i in(0..10)
            print i
            print "\n"
        end
        ##############################
        #Second case
        print "\n" * 2
        for i in(0..10)
            if i == 2
                break   #Break the cycle
            end
            print i
            print "\n"
        end
        ##############################
        #Third case
        print "\n" * 2
        for i in(0..10)
            if i == 2
                next # Is as a continue
            end
            print i
            print "\n"
        end
        ##############################
        #Fourth case
        counter = 0
        print "\n" * 2
        for i in(0..10)
            counter = counter + 1
            print i
            print "\n"
            if i == 2
                if counter == 10
                    break
                end
                redo # Repeat the cycle
            end
        end
    end
end

object = ForCycle.new()
object.forcycle()
gets()