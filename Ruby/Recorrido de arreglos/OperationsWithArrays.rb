class OperationsWithArrays
def initialize()
end
def operations
    example = [1, 2, 3, 4, 5, 6]
    #######################################
    # First way
    puts  "First way"
    for y in example
        puts y
    end
    #######################################
    # Second way
    puts  "Second way"
    example.each do |y|
        puts y
    end
    #######################################
    # Third way
    puts  "Third way"
    map = example.map { |y| y+1}
    for y in map
        puts y
    end
    #######################################
    # Fourth way
    puts  "Fourth way"
    select = example.select { |number| number > 3}
    for y in select
        puts y
    end
    #######################################
    # Fifth way
    puts  "Fifth way"
    delete = example.delete_if { |number| number > 3}
    for y in delete
        puts y
    end
end
end

object = OperationsWithArrays.new()
object.operations()
gets()