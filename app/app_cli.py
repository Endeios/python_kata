import argparse
import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The app elaborates an input file and prints the result on a file or "
                                                 "standard output")
    parser.add_argument("input", help="the input file of this program", type=str)
    parser.add_argument("-o", "--output", help="The name of the file to use as an output", required=False)
    args = parser.parse_args()
    with open(args.input) as input_file:
        input_data = input_file.read()
        result = app.echo(input_data)
        if args.output:
            with open(args.output, "w") as out:
                out.write(result)
        else:
            print(result)
