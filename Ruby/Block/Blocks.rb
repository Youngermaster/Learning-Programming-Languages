class Array
    def iterar
        self.each_with_index do |n,y|
            self[y] = yield(n)
        end
    end
end

array = [1, 2, 3, 4, 5]

array.iterar do |n|
    n**2
end

for i in array
    puts i
end