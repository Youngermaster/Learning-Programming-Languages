=begin
    to_i convert to integer
    to_f convert to float
    to_s convert to string
=end
class ConvertVariables
    def initialize()
    end
    def convert()
        example_int = 1
        example_float = 117.177
        example_string = "13"
        example_string = example_string.to_f
        example_int = example_int.to_f
        puts example_string + example_float
        puts example_int + example_float
    end
end

object = ConvertVariables.new()
object.convert
gets()