class File:

    def write_file(expr_set, ans_set, expr_file, ans_file):
        print("Saving  the topic")
        index = 0
        with open(expr_file, 'w+', encoding='utf-8') as ef, \
                open(ans_file, 'w+', encoding='utf-8') as af:
            ef.write('+' + '-' * 6 + '+' + '-' * 38 + '+' + '\n')
            ef.write('|'+'NO'.center(6,' ')+'|' + 'Arithmetic'.center(38,' ') + '|\n')
            ef.write('+' + '-' * 6 + '+' + '-' * 38 + '+' + '\n')
            af.write('+' + '-'*6 + '+' + '-'*12 + '+' + '-'*38 + '+' + '\n')
            af.write('|'+'NO'.center(6,' ')+'|' + 'Answer'.center(12,' ') + '|'+'Arithmetic'.center(38,' ')+'|\n')
            af.write('+' + '-' * 6 + '+' + '-' * 12 + '+' + '-' * 38 + '+' + '\n')


            for ans, content in zip(ans_set, expr_set):
                index += 1
                ef.write('|'+str(index).center(6,' ') + '|' + str(content).center(37,' ') + '|\n')
                af.write('|' + str(index).center(6,' ') + '|' + str(ans).center(12,' ') + '|' + str(content).center(37,' ') +'|'+ '\n')
            ef.write('+' + '-' * 6 + '+' + '-' * 38 + '+' + '\n')
            af.write('+' + '-' * 6 + '+' + '-' * 12 + '+' + '-' * 38 + '+' + '\n')
        print("save successfully ！")

    def write_grade_file(grade_file, correct, wrong):
        print("Saving the grade")
        with open(grade_file, 'w+', encoding='utf-8') as gf:
            gf.write("{:<9}".format("Correct:") + str(len(correct)) + str(correct) + '\n')
            gf.write("{:<9}".format("Wrong:") + str(len(wrong)) + str(wrong) + '\n')
        print("Success!")