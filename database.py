from sqlalchemy import create_engine
from sqlalchemy import text


db_connect_string = "mysql+pymysql://ypuq2w686p9wa9k85e0b:pscale_pw_j9n0kto6EC8xSQCApt4ETL7Fk7YaIPe0L4zSkLHPrB6@aws.connect.psdb.cloud/juan_portfolio_website_v2?charset=utf8mb4"
engine = create_engine(db_connect_string,connect_args={
    "ssl":{
        "ssl_ca":""
    }
})


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())