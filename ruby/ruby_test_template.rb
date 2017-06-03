require 'rspec'
require 'pp'
require 'open3'

# To run this test:
# $ rspec /path/to/test_script_being_tested.rb

# Assumes that the name of the file being tested is ../something.rb, and the name of this script is test_something.rb
$:.unshift File.join(File.dirname(__FILE__),'..')
script_under_test = File.basename(__FILE__).gsub(/^test_/,'')
require script_under_test
def assert_equal(e,o); o.should eq(e); end
path_to_script = File.join(File.dirname(__FILE__),'..',script_under_test)



describe script_under_test do
  it 'should obvious test' do
    seqs = %w(a a a)
    trimmed = Bio::Alignment.new(seqs).trim_uninformative_columns
    trimmed[0].size.should eq(0) #"all seqs should be empty since they are all uninformative"
    assert_equal 3, trimmed.size #"should still have 3 seqs in it"
  end
  
  it 'should open3 test' do
    seqs = %w(>scaffold1 AANNTGTG)
    
    Open3.popen3(path_to_script) do |stdin, stdout, stderr|
      stdin.puts seqs.join("\n")
      stdin.close
      
      err = stderr.readlines
      err.should eq([]), err.join("")
      answer = %w(>scaffold1_1_2 AA >scaffold1_5_8 TGTG).join("\n")+"\n"
      stdout.read.should eq(answer)
    end
  end
end