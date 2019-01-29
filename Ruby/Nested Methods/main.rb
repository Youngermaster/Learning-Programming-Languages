class Main
    def initialize
    end
    def x
        puts "This is a x"
        def y
            puts "This is a y"
            def z
                puts "This is a z"
            end
        end
    end
end

object = Main.new
object.x
object.y
object.z