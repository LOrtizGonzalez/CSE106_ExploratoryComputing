#Lab1 Q4

class courseInfo():

    def __init__(self, round, dept, num, name, credits, lect_days, start, end, avg):
        self.course = round
        self.course_dept = dept
        self.course_num = num
        self.course_name = name
        self.course_credits = credits
        self.course_lect_days = lect_days
        self.start_time = start
        self.end_time = end
        self.avg_grade = avg

    def course_info(self):
        print("COURSE {}: {}{}: {}".format(self.course, self.course_dept, self.course_num, self.course_name))
        print("Number of credits:", self.course_credits)
        print("Days of Lecture:", self.course_lect_days)
        print("Lecture Time:", self.start_time,"-", self.end_time)
        print("Stat: on average, students get {}% in this course\n".format(self.avg_grade))
        

def main():
    
    file = open("classesInput.txt", 'r')
    s = " "
    r = []
    while(s):
        s = file.readline()
        r.append(s.strip()) #Removes the next-line character
    file.close()

    num = int(r[0]) #Number of courses to be entered
    course_arr = []
    
    for i in range(0,num):
        t = i * 8 + 1
        course_arr.append(courseInfo(i+1, r[t], r[t+1], r[t+2], r[t+3], r[t+4], r[t+5], r[t+6], r[t+7]))
    
    for x in range(0,num):
        course_arr[x].course_info() #Do not need print statement since it would return 'None' output


if __name__ == '__main__':
    main()