# benchmark_memory.rb
require 'json'

def measure_memory_usage
  initial_memory = GC.stat(:heap_allocated_pages)
  lst = (0...1000000).to_a
  final_memory = GC.stat(:heap_allocated_pages)
  memory_used = final_memory - initial_memory
  {memory_used: memory_used * GC::INTERNAL_CONSTANTS[:RVALUE_SIZE]}
end

puts measure_memory_usage.to_json
