import pyarrow as pa
import pyarrow.parquet as pq

def save_parquet(df, path):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, path, compression="snappy")








# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/