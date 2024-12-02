# based on https://github.com/hyperneutrino/advent-of-code/blob/main/scripts.sh
# will make 2024 and future folder compliant with this

AOC="~/Projects/Advent-Of-Code/$(echo `date +%Y/d%d` | sed 's/\/d0/\/d/g')"
AOC_COOKIE="" # get this from the cookies tab in network tools on the AOC website

alias aoc-load="cd $AOC; curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > inp.txt"

alias aoc1="cd $AOC; echo 'part one'; python3 p1.py < inp.txt"
alias aoc2="cd $AOC; echo 'part two'; python3 p2.py < inp.txt"
alias aoc="aoc1; echo; aoc2"
