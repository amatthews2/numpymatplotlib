import json

filename = "sample_data.txt"
my_dict = {}
pat = []


def diagnosis(test_results):
    sorted_tsh = TSH(test_results)
    for lvl in sorted_tsh:
        if lvl > 4.0:
            diag = 'hypothyroidism'
            break
        elif lvl < 1.0:
            diag = 'hyperthyroidism'
            break
        else:
            diag = 'normal thyroid function'
    return diag


def TSH(test_results):
    tsh_list = test_results.split(",")
    tsh_list = (tsh_list[1:])
    for index, item in enumerate(tsh_list):
        tsh_list[index] = float(item)
    sorted_tsh = sorted(tsh_list)
    return sorted_tsh


def sep_data(patient_data):
    for p in range(int(len(patient_data))):
        f_name, l_name = patient_data[p][0].split(' ', 1)
        full_name = patient_data[p][0].replace(' ', '_')
        my_dict["First Name"] = f_name
        my_dict["Last Name"] = l_name
        my_dict["Age"] = int(patient_data[p][1])
        my_dict["Gender"] = patient_data[p][2]
        my_dict["Diagnosis"] = diagnosis(patient_data[p][3])
        my_dict["TSH"] = TSH(patient_data[p][3])
        output_file(my_dict, full_name)
    return


def output_file(my_dict, full_name):
    out_file = open('%s.json' % full_name, "w")
    json.dump(my_dict, out_file)
    out_file.close()
    return


def input_file(filename):
    with open(filename) as fh:
        i = 0
        p = 0
        l = fh.readlines()
        for i in range(len(l)):
            l[i] = l[i].strip('\n')
        for p in range(int((len(l) - 1) / 4)):
            pat.append(list(l[(p * 4):(p * 4) + 4]))
    return pat


if __name__ == "__main__":
    pat = input_file(filename)
    sep_data(pat)
