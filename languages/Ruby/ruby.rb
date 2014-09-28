#!/usr/bin/env ruby

say = "I love Ruby"
puts say
say['love'] = "*love*"
puts say.upcase
5.times { puts say }
def h
puts "Hello World!"
end
h
def h(name = "World")
puts "Hello #{name.capitalize}!"
end
h "chris"
h
class Greeter
    attr_accessor :name
    def initialize(name = "World")
        @name = name
    end
    def say_hi
        puts "Hi #{@name}!"
    end
    def say_bye
        puts "Bye #{@name}, come back!"
    end
end
g = Greeter.new("Pat")
g.say_hi
g.say_bye
g.name = "Betty"
g.say_hi
# puts Greeter.instance_methods
class MegaGreeter
    attr_accessor :names

    # Create the object
    def initialize(names = "World")
        @names = names
    end

    # Say hi to everybody
    def say_hi
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("each")
            @names.each do |name|
                puts "Hello #{name}!"
            end
        else
            puts "Hello #{@names}!"
        end
    end

    # Say bye to everybody
    def say_bye
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("join")
            # Join the list elements with commas
            puts "Goodbye #{@names.join(", ")}. Come back soon!"
        else
            puts "Goodbye #{@names}. Come back soon!"
        end
    end

end


if __FILE__ == $0
    mg = MegaGreeter.new
    mg.say_hi
    mg.say_bye

    mg.names = "Zeke"
    mg.say_hi
    mg.say_bye

    mg.names = ["Albert", "Brenda", "Charles", "Dave", "Engelbert"]
    mg.say_hi
    mg.say_bye

    mg.names = nil
    mg.say_hi
    mg.say_bye
end
