require 'rspec'
require 'pp'

# Assumes that the name of the file being tested is ../something.rb, and the name of this script is test_something.rb
$:.unshift File.join(File.dirname(__FILE__),'..')
script_under_test = File.basename(__FILE__).gsub(/^test_/,'')
require script_under_test
def assert_equal(e,o); o.should eq(e); end


describe script_under_test do
  it 'should obvious test' do
    seqs = %w(a a a)
    trimmed = Bio::Alignment.new(seqs).trim_uninformative_columns
    trimmed[0].size.should eq(0) #"all seqs should be empty since they are all uninformative"
    assert_equal 3, trimmed.size #"should still have 3 seqs in it"
  end
end