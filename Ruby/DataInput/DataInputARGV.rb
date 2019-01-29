class DataInputARGV
    def initialize()
    end
    def WhitoutChomp()
        name = ARGV[0]
        puts "Hola " + name
    end
end

object = DataInputARGV.new()
object.WhitoutChomp()