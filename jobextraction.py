from jobtitle import job_title

file = open("recognized.txt", "r")


def extract_job_title():
    job1 = []
    for line in file:
        line = line.strip().split()
        for word in line:
            word = word.lower()
            # print(word)
            if word in job_title:
                # print(word)
                job1.append(word)
    return job1
