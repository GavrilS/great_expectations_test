import great_expectations as ge
import json


def test():
    my_df = ge.read_csv("./meetings.csv")
    print(my_df.head())
    print("Time for expectations")
    print(my_df.expect_table_row_count_to_be_between(250, 350))
    print(my_df.get_expectation_suite())
    with open("my_expectations_file.json", "w") as my_file:
        my_file.write(
            json.dumps(my_df.get_expectation_suite().to_json_dict())
        )

test()
