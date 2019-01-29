class Array 
    def iterar block
        self.each_with_index do |n,y|
            self[y] = block.call n
        end
    end
end

array = [1, 2, 3, 4, 5]

pow = Proc.new do |n|
    n**2
end

plus_1 = Proc.new do |number|
    number + 1
end

array.iterar plus_1
array.iterar pow

for i in array
    puts i
end