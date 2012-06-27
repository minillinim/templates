#!/usr/bin/env ruby

require 'optparse'
require 'bio-logger'

SCRIPT_NAME = File.basename(__FILE__); LOG_NAME = SCRIPT_NAME.gsub('.rb','')

# Parse command line options into the options hash
options = {
  :logger => 'stderr',
}
o = OptionParser.new do |opts|
  #TODO Fill in usage, description and option parsing below
  opts.banner = "
    Usage: #{SCRIPT_NAME} <arguments>
    
    Description of what this program does...\n"
  # Example option
  opts.on("-e", "--eg", "description [default: #{options[:eg]}]") do |f|
    options[:operation] = OVERALL
  end
  
  # logger options
  opts.on("-q", "--quiet", "Run quietly, set logging to ERROR level [default INFO]") {Bio::Log::CLI.trace('error')}
  opts.on("--logger filename",String,"Log to file [default #{options[:logger]}]") { |name| options[:logger] = name}
  opts.on("--trace options",String,"Set log level [default INFO]. e.g. '--trace debug' to set logging level to DEBUG"){|s| Bio::Log::CLI.trace(s)}
end
o.parse!
if ARGV.length != 0 #TODO require a set number of arguments?
  $stderr.puts o
  exit 1
end
# Setup logging. bio-logger defaults to STDERR not STDOUT, I disagree
Bio::Log::CLI.logger(options[:logger]); log = Bio::Log::LoggerPlus.new(LOG_NAME); Bio::Log::CLI.configure(LOG_NAME)


#TODO what are you looking at me for? This is your script. Do something.
log.info 'e.g. logging'
