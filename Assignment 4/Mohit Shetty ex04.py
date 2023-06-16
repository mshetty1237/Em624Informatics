import pandas
import datetime
import operator


def print_details(file):
    list1 = [line.split(",") for line in file.readlines() if line.rstrip('\n')]
    starttime = 0
    endtime = 0
    startstation = []
    endstation = []
    mem1 = 0

    for x, columnname in enumerate(list1[0]):
        if columnname in ["Start Time", "started_at"]:
            starttime = x
        elif columnname in ["Stop Time", "ended_at"]:
            endtime = x
        elif columnname in ["Start Station Name", "start_station_name"]:
            start_station_1 = x
        elif columnname in ["End Station Name", "end_station_name"]:
            end_station_1 = x
        elif columnname in ["User Type", "member_casual\n"]:
            mem1 = x

    start_timing = [datetime.datetime.strptime(line[starttime], "%Y-%m-%d %H:%M:%S") for line in list1[1:]]
    end_timing = [datetime.datetime.strptime(line[endtime], "%Y-%m-%d %H:%M:%S") for line in list1[1:]]
    duration = [end - start for start, end in zip(start_timing, end_timing)]

    start_1 = {}
    for line in list1[1:]:
        try:
            start_1[line[start_station_1]] += 1
        except KeyError:
            start_1[line[start_station_1]] = 1
    sorted_start_stat = sorted(start_1.items(), key=operator.itemgetter(1), reverse=True)

    end_station = {}
    for line in list1[1:]:
        try:
            end_station[line[end_station_1]] += 1
        except KeyError:
            end_station[line[end_station_1]] = 1
    sorted_end_stat = sorted(end_station.items(), key=operator.itemgetter(1), reverse=True)

    mem = {}
    if mem1 is not None:
        for line in list1[0:]:
            try:
                mem[line[mem1]] += 1
            except KeyError:
                mem[line[mem1]] = 1
        if mem in ["Subscriber", "Customer"]:
            mem["member"] = mem.pop("Subscriber")
            mem["casual"] = mem.pop("Customer")
        elif mem in ["member\n", "casual\n"]:
            mem["member"] = mem.pop("member\n")
            mem["casual"] = mem.pop("casual\n")
    else:
        mem["member"] = 0
        mem["casual"] = 0

    print("\nThe details of the file ")
    print(file.name)
    print()
    print("The 5 most popular start stations")
    for station, count in sorted_start_stat[:5]:
        print(f"{station},", end=" ")
    print("\n")

    print("The 5 most popular end stations ")
    for station, count in sorted_end_stat[:5]:
        print(f"{station},", end=" ")
    print()
    transposelist = list(zip(*list1))
    list2 = transposelist[12]
    if 'member' in list2:
        index = list2.index('member')
        list1[index] = 'Subscriber'
        print()
    if 'casual' in list2:
        index = list2.index('casual')
        list1[index] = 'Customer'
    member_type = {b.replace('\n', ''): a for b, a in mem.items()}
    print(member_type)
    return member_type



file1 = "JC-201611-citibike-tripdata.csv"
file2 = "JC-202111-citibike-tripdata.csv"
with open(file1) as file_1:
    member_types = print_details(file_1)
    subscriber = member_types['Subscriber']
    customer = member_types['Customer']
    print("The percentage of Subscribers is ", subscriber / (subscriber + customer) * 100)
    print("The percentage of Customers is ", customer / (subscriber + customer) * 100)

with open(file2) as file_2:
    member_types = print_details(file_2)
    member = member_types['member']
    customer = member_types['casual']
    print("The percentage of Members is ", member / (member + customer) * 100)
    print("The percentage of Casual users is ", customer / (member + customer) * 100)

print("\nThis is the end of processing")