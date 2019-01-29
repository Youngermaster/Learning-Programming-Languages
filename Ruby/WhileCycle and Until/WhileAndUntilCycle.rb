class WhileAndUntilCycle
    def initialize()
    end
    def While()
        print "While cycle.\n"
        y = 0
        while y < 5 do
            print y
            y += 1
        end
    end
    def DoWhile()
        print "\nDo while.\n"
        y = 0
        begin
            print y
            y += 1
        end while y < 5
    end
    def Until()
        print "\nUntil Condition.\n"
        y = 0
        until y > 5 do
            print y
            y += 1
        end
    end
    def Until2()
        print "\nUntil Condition 2.\n"
        y = 0
        begin
            print y
            y += 1
        end until y > 5
    end
end

object = WhileAndUntilCycle.new()
object.While()
object.DoWhile()
object.Until()
object.Until2()
gets()
