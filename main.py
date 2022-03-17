from flask import Flask, render_template
app = Flask('app')

todos = [
  {
    'name': 'Estudar Python', 'complete': False 
  },   
  {
    'name': 'Estudar JavaScript', 'complete': False
  }
]

@app.route('/')
def index():
  return render_template(
    'index.html',
    todos=todos
  )

if __name__ == '__main__':
  app.run(host='0.0.0.0')