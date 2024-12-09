local function readFileLines(filename)
    local lines = {}
    local file = io.open(filename, "r")
    if file then
        for line in file:lines() do
            table.insert(lines, line)
        end
        file:close()
    else
        error("Could not open file: " .. filename)
    end
    return lines
end

function split(inputstr, sep)
    if sep == nil then
      sep = "%s"
    end
    local t = {}
    for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
      table.insert(t, str)
    end
    return t
end
function indexOf(array, value)
    for i, v in ipairs(array) do
        if v == value then
            return i
        end
    end
    return -1
end


-- Example usage:
local lines = readFileLines("day-5/testcase.txt")
local rules = {}
local pages = {}
local hit_split = false

for i, line in ipairs(lines) do
    if (line == "") then
        hit_split = true
    elseif (not hit_split) then
        rules[#rules+1] = line
    elseif (hit_split) then
        pages[#pages+1] = line
    end
end

for i, page in ipairs(pages) do
    local page_split = {}
    page_split = split(page, ",")
    -- okay so i iterate through the page array
    for j = 1, #page_split, 1 do
        -- for each page, check if it follows the rules
        local found_violation = false;
        local found_correct = true;
        for k = 1, #rules, 1 do
            local rule_split = split(rules[k],"|")
            -- check if the rule applies
            if (rule_split[1] == page_split[j]) then
                -- check if it follows rules
                local pageIndex = indexOf(page_split,rule_split[2])
                if (pageIndex < j and not pageIndex == -1 ) then
                    found_violation = true
                else 
                    found_correct = true
                end
            elseif (rule_split[2] == page_split) then
                local pageIndex = indexOf(page_split,rule_split[2])
                if (pageIndex >= j and not pageIndex == -1  ) then
                    found_violation = true
                else 
                    found_correct = true
                end
            end
        end
        if (found_violation or not found_correct) then
            print("page " .. i .. " is unsafe!")
        end
    end
    
end