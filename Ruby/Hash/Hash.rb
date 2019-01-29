class Hash
def initialize()
end
def dictionary
    courses = {'Age' => 17, 'name' => "Juan Manuel Young"}
    courses['Sex'] = "Male"
    keys = courses.keys
    values = courses.values
    courses.each do |key, value|
        puts "#{key} have this value: #{value}"
    end
    for y in keys
        puts y
    end
    for z in values
        puts z
    end
end
end

object = Hash.new
object.dictionary
gets