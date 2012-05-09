require "rubygems"
require "sqlite3"
require "redis"
require "bayes_on_redis"


db = SQLite3::Database.new "connotation.db"
bor = BayesOnRedis.new(redis_host: '127.0.0.1', redis_port: 6379, redis_db: 0)

db.execute( "select * from source_data" ) do |row|
  bor.train row[2], row[1]
end
