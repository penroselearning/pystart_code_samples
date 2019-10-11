print('Student Grade Calculator')

student_scores = []

try:
    student_scores = [input("Enter Student Name: "),
                  (int(input("Enter English Score (Max 100): \n")),
                   int(input("Enter Math Score (Max 100): \n")),
                   int(input("Enter Chemistry Score (Max 100): \n")),
                   int(input("Enter Physics Score (Max 100): \n")),
                   int(input("Enter Geography Score (Max 100): \n")),)]


except ValueError:
    print("Kindly provide the correct Scores")
else:

    avg = (student_scores[1][0] + student_scores [1][1] + student_scores [1][2] + student_scores [1][3] + student_scores [1][1])/5

    print()

    if avg >= 90:
        grade = 'A'
    elif avg >= 80 and avg < 90:
        grade= 'B'
    elif avg >= 70 and avg < 80:
        grade= 'C'
    elif avg >= 60 and avg < 70:
        grade= 'D'
    elif avg >= 50 and avg < 60:
        grade = 'E'
    elif avg < 50:
        grade = 'F'
    else:
        print("Sorry something went wrong.")

    print(f'Your final grade is: {grade}')