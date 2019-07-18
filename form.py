from forms import ContactForm
from flask.ext.mail import Message, Mail


mail = Mail()
app = Flask(__name__)


app.secret_key = 'development key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'email'
app.config['MAIL_PASSWORD'] = 'password'
mail.init_app(app)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():

 class ContactForm(Form):
    name = TextField("Name", [wtforms.validators.Required('Please enter your name')])
    email = TextField("Email", [wtforms.validators.Required('Please enter your email'), wtforms.validators.Email()])
    subject = TextField("Subject", [wtforms.validators.Required('Please enter a subject')])
    message = TextAreaField("Message", [wtforms.validators.Required('Please enter a message')])
    submit = SubmitField("Send")
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='imauld@gmail.com', recipients=['qwekubenjamin17@gmail.com']
             msg.body = """From: %s &lt;%s&gt; %s""" % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
        elif request.method == 'GET':
        return render_template('contact.html', form=form)