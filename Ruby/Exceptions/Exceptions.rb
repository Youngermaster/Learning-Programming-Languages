def filegg value
    archive = File.open "claseperro.rb"
    raise
rescue => error
    puts error.message
ensure
    archive.close
    puts "Me aseguro de que se cierre :D"
end

filegg false

def verdadero value
    raise TypeError, 'Tienes que mandar una error verdadero' if value == false
    rescue => error
        puts error.message
end


verdadero false

puts "\n" * 2
begin
    1/0
rescue => error
    puts error.message
end

puts "hello world"