import csv

num_sites_invalid = 0
num_sites_duplicate = 0
num_sites_used_duplicates = 0
total_attributes = 0
total_duplicates = 0
total_duplicates_used = 0
invalid_total = 0

# columns: url,attribute count,id count,invalid idref count,duplicate id count,duplicate ids used

with open('results.txt', 'r') as file:
    csvfile = csv.reader(file)
    for index, line in enumerate(csvfile):
        if index == 0:
            continue  # skip header
        else:
            invalid_count = int(line[3])
            duplicate_count = int(line[4])
            duplicate_used_count = int(line[5])
            print(f"{line[0]}: {invalid_count} invalid, {duplicate_count} duplicate ids, {duplicate_used_count} duplicate ids used")
            if invalid_count > 0:
                num_sites_invalid += 1
            if duplicate_count > 0:
                num_sites_duplicate += 1
            if duplicate_used_count > 0:
                num_sites_used_duplicates += 1
            total_duplicates += duplicate_count
            total_duplicates_used += duplicate_used_count
            total_attributes += int(line[1])
            invalid_total += invalid_count


print(f"{num_sites_invalid} sites with invalid ids, {num_sites_duplicate} sites with duplicate id, {num_sites_used_duplicates} sites that used duplicate ids")
print(f"Total duplicate ids across all sites: {total_duplicates}, total duplicate ids used across all sites: {total_duplicates_used}, of {total_attributes} id referencing attributes across all sites; {invalid_total} invalid idrefs used across all sites")