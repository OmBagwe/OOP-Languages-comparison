# benchmark_efficiency.rb
require 'json'

def measure_efficiency
  lst = Array.new(1000000) { rand(1..1000000) }
  start_time = Time.now
  sorted_list = lst.sort
  end_time = Time.now
  efficiency = end_time - start_time
  {efficiency: efficiency}
end

puts measure_efficiency.to_json
