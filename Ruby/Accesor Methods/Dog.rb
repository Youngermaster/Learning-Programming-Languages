class Dog
    def initialize name = 'With out name', race = 'With out race'
        @name = name
        @race = race
    end
    def bark greet
        return "Guau" * 5
    end
    def my_name
        return @name
    end
    def my_race
        return @race
    end
    #def name
    #    return @name
    #end
    #def name=newName
    #    @name = newName
    #end
    attr_accessor :name
end