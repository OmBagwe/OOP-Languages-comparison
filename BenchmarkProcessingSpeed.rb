# benchmark_processing_speed.rb
require 'json'

def measure_processing_speed
  start_time = Time.now
  result = 0
  (0...10000000).each { |i| result += i }
  end_time = Time.now
  processing_speed = end_time - start_time
  {processing_speed: processing_speed}
end

puts measure_processing_speed.to_json
