class Strings 
    def initialize()
    end
    def strings()
        sum = 3 + 5
        result = "The result between 3 and 5 is: #{sum}.\n"
        #######################################
        chain = "Hello "
        chain << "world"
        chain.concat(33) #This is in ASCII
        #######################################
        chain2 = "ja" * 4
        #######################################
        # If is equals return 0, if is  more bigger return 1 else return -1
        chain3 = "HelloWorld"
        chain4 = "helloWorld"
        result2 = chain3 <=> chain4
        #######################################
        # If is equals return 0, if is  more bigger return 1 else return -1 without mayus
        chain5 = "HelloWorld"
        chain6 = "helloWorld"
        result3 = chain5.casecmp(chain6)
        #######################################
        name = "juan"
        name = name.capitalize
        #######################################
        chain7 = "Welcome"
        chain7.each_char{|c| print c 
            print "\n"}
        #######################################
        chain8 = "Youngermaster"
        chain8 = chain8.center(100, "--")
        #######################################
        print result
        print chain + "\n"
        print chain2 + "\n"
        print chain.length
        print "\n"
        print result2
        print "\n"
        print result3
        print "\n"
        print name
        print "\n"
        print chain8
    end
end

object = Strings.new()
object.strings()
gets()