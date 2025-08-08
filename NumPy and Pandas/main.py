from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/toc')
def toc():
    return render_template('toc.html')

# Part 1 - Getting Started
@app.route('/part1/chapter01-intro-numpy')
def chapter01():
    return render_template('chapters/part1-getting-started/chapter01-intro-numpy.html')

@app.route('/part1/chapter02-arrays-depth')
def chapter02():
    return render_template('chapters/part1-getting-started/chapter02-arrays-depth.html')

@app.route('/part1/chapter03-broadcasting-indexing')
def chapter03():
    return render_template('chapters/part1-getting-started/chapter03-broadcasting-indexing.html')


# Part 2 - NumPy Mastery
@app.route('/part2/chapter04-math-operations')
def chapter04():
    return render_template('chapters/part2-numpy-mastery/chapter04-math-operations.html')

@app.route('/part2/chapter05-linear-algebra')
def chapter05():
    return render_template('chapters/part2-numpy-mastery/chapter05-linear-algebra.html')

@app.route('/part2/chapter06-random-simulation')
def chapter06():
    return render_template('chapters/part2-numpy-mastery/chapter06-random-simulation.html')

@app.route('/part2/chapter07-vectorization')
def chapter07():
    return render_template('chapters/part2-numpy-mastery/chapter07-vectorization.html')

@app.route('/part2/chapter08-optimization')
def chapter08():
    return render_template('chapters/part2-numpy-mastery/chapter08-optimization.html')

@app.route('/part2/chapter09-numpy-challenges')
def chapter09():
    return render_template('chapters/part2-numpy-mastery/chapter09-numpy-challenges.html')

@app.route('/part2/chapter10-mini-projects')
def chapter10():
    return render_template('chapters/part2-numpy-mastery/chapter10-mini-projects.html')


# Part 3 - Intro to Pandas
@app.route('/part3/chapter11-series-dataframes')
def chapter11():
    return render_template('chapters/part3-intro-pandas/chapter11-series-dataframes.html')

@app.route('/part3/chapter12-data-cleaning')
def chapter12():
    return render_template('chapters/part3-intro-pandas/chapter12-data-cleaning.html')

@app.route('/part3/chapter13-selection-filtering')
def chapter13():
    return render_template('chapters/part3-intro-pandas/chapter13-selection-filtering.html')


# Part 4 - Pandas Advanced
@app.route('/part4/chapter14-time-series')
def chapter14():
    return render_template('chapters/part4-pandas-advanced/chapter14-time-series.html')

@app.route('/part4/chapter15-multi-indexing')
def chapter15():
    return render_template('chapters/part4-pandas-advanced/chapter15-multi-indexing.html')

@app.route('/part4/chapter16-groupby')
def chapter16():
    return render_template('chapters/part4-pandas-advanced/chapter16-groupby.html')

@app.route('/part4/chapter17-merging')
def chapter17():
    return render_template('chapters/part4-pandas-advanced/chapter17-merging.html')

@app.route('/part4/chapter18-pivot-reshape')
def chapter18():
    return render_template('chapters/part4-pandas-advanced/chapter18-pivot-reshape.html')

@app.route('/part4/chapter19-visualization')
def chapter19():
    return render_template('chapters/part4-pandas-advanced/chapter19-visualization.html')

@app.route('/part4/chapter20-pandas-challenges')
def chapter20():
    return render_template('chapters/part4-pandas-advanced/chapter20-pandas-challenges.html')


# Part 5 - Practice Projects
@app.route('/part5/chapter21-daily-drills')
def chapter21():
    return render_template('chapters/part5-practice-projects/chapter21-daily-drills.html')

@app.route('/part5/chapter22-practice-sets')
def chapter22():
    return render_template('chapters/part5-practice-projects/chapter22-practice-sets.html')

@app.route('/part5/chapter23-tests-quizzes')
def chapter23():
    return render_template('chapters/part5-practice-projects/chapter23-tests-quizzes.html')

@app.route('/part5/chapter24-interview-questions')
def chapter24():
    return render_template('chapters/part5-practice-projects/chapter24-interview-questions.html')

@app.route('/part5/chapter25-eda')
def chapter25():
    return render_template('chapters/part5-practice-projects/chapter25-eda.html')

@app.route('/part5/chapter26-ds-projects')
def chapter26():
    return render_template('chapters/part5-practice-projects/chapter26-ds-projects.html')

@app.route('/part5/chapter27-de-projects')
def chapter27():
    return render_template('chapters/part5-practice-projects/chapter27-de-projects.html')

@app.route('/part5/chapter28-pandas-sql')
def chapter28():
    return render_template('chapters/part5-practice-projects/chapter28-pandas-sql.html')

@app.route('/part5/chapter29-ml-with-pandas')
def chapter29():
    return render_template('chapters/part5-practice-projects/chapter29-ml-with-pandas.html')

@app.route('/part5/chapter30-capstone')
def chapter30():
    return render_template('chapters/part5-practice-projects/chapter30-capstone.html')

@app.route('/part6/NumPy-Quiz')
def numpyquiz():
    return render_template('quizzes/numpy_quizzes.html')

@app.route('/part6/Pandas-Quiz')
def pandasquiz():
    return render_template('quizzes/pandas_quizzes.html')

@app.route('/part6/Final-Exam')
def finalexam():
    return render_template('quizzes/final_exam.html')

@app.route('/part7/project1')
def miniproject1():
    return render_template('projects/mini/project1-basic.html')

@app.route('/part7/projec2')
def miniproject2():
    return render_template('projects/mini/project2-cleaning.html')

@app.route('/part7/projec3')
def miniproject3():
    return render_template('projects/mini/project3-viz.html')

@app.route('/part7/Capsone-Project')
def Capstone_Projec():
    return render_template('projects/capsone/capsone-project.html')

if __name__ == '__main__':

    app.run(debug=True)
