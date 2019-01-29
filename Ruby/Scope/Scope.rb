$example = "This is a global variable"
class Scope
    def intialize()
        @example = "This is a instance variable"
        $example = "I was modified"
    end
    def scopeProof()
        example = "This is a local variable"
        puts example
        puts @example
        puts $example
    end
end

object = Scope.new()
object.scopeProof()
gets()