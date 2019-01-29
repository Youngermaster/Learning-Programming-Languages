class AnotherCycles
    def initialize()
    end
    def Each()
        print "Each Cycle.\n"
        (1..10).each { |i| 
        print i 
        print "\n"}
    end
    def UpTo()
        print "\nUp To Cycle.\n"
        10.upto(20) { |i|
        print i 
        print "\n"}
    end
    def DownTo()
        print "\nDown To.\n"
        20.downto(10) { |i|
        print i 
        print "\n"}
    end
    def Times()
        print "\nTimes.\n"
        10.times { |i| 
        print i + 1
        print "\n"}
    end
end

object = AnotherCycles.new()
object.Each()
object.UpTo()
object.DownTo()
object.Times()
gets()