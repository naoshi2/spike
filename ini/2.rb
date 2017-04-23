def parse(str)
  ini_hash = Hash.new{ |h, k| h[k] = {} }
  section = ""
  str.each_line do |line|
    case line
    when /\[(.+)\]/
      section = $1
    #when /([^=]+)=(.+)/
    when /(^.{1,}$)/
      ini_hash[section][$1] = $2
    end
  end
  ini_hash
end

inifile = parse(open('./a.ini').read)
inifile.each do |section, hash|
  p section
  hash.each_key do |key|
    p key
  end
  #puts hash["hoge1"]
  #puts hash["hoge2"]
  #puts hash["hoge3"]
  #puts hash["hoge4"]
end
