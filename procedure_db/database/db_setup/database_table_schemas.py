# Tables and column descriptions for database `tunafish`.

def db_table_schemas():
  table_list = [
    "simprocedures",
    ]

  # `Key` is table name and `value` is an array of columns
  table_attributes = {
    "simprocedures": [
      ["name", "varchar(50)", "not null", "", ""],
      ["arch", "varchar(20)", "not null", "", ""],
      ["file_type", "varchar(15)", "not null", "", ""],
      ["os_version", "varchar(20)", "not null", "", ""],
      ["contains_bytes", "varchar(150)", "not null default ''", "", ""],
      ["models_os", "varchar(1)", "not null default '0'", "", ""],
      ["models_libs", "varchar(1)", "not null default '0'", "", ""],
      ["timestamp", "timestamp", "not null default current_timestamp on update current_timestamp", "last login UTC time", ""],
      ["recno", "BIGINT", " not null auto_increment", "Unique record number (row)", ""]
    ]
  }
  return (table_list, table_attributes)

#print(db_table_schemas())
