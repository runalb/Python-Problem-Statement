# PS-06 WAP to take marks of 5 subject and display the grade

c = 0
while c != 5:
    try:
        marks = int(input("Enter subject-{} marks:".format(c+1)))

        if marks >= 0 and marks <=100:
            c = c + 1

            if marks >= 90 and marks <= 100:
                print("Subject-{} grade: A".format(c))

            elif marks >= 80 and marks < 90:
                print("Subject-{} grade: B".format(c))

            elif marks >= 70 and marks < 80:
                print("Subject-{} grade: C".format(c))

            elif marks >= 60 and marks < 70:
                print("Subject-{} grade: D".format(c))

            elif marks >= 50 and marks < 60:
                print("Subject-{} grade: E".format(c))

            else:
                print("Subject-{} grade: F".format(c))

        else:
            print("Enter marks between 0-100")

    except:
        print("Invalid value")