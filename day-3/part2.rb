def count_amount(str)
    return str.scan(/mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)/) 
end  

f = File.open("day-3/input.txt")
array = count_amount(f.read)
total = 0
doing = true
for equation in array
    if (equation == "do()")
        doing = true
    elsif (equation == "don't()")
        doing = false
    else
        if (!doing)
            next
        end
        equation = equation.gsub("mul(", "").gsub(")", "")
        equation = equation.split(",")
        total += equation[0].to_i * equation[1].to_i
    end 
end
puts total