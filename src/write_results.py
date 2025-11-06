import csv

def write_results(columns, data):
    with open('results.txt', 'w', newline='') as csvfile:
        # clear prior text content
        csvfile.truncate(0)

        # write new data to results.txt
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(data)

        # close file
        csvfile.close()

    print(f"Results written to results.txt")