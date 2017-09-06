from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Oriana'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': '''
               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam at lacus sit amet quam lacinia semper. Etiam ex elit, vehicula in congue sed, laoreet sed orci. Morbi risus lacus, scelerisque sit amet lectus ac, scelerisque scelerisque arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum maximus lorem at sapien congue maximus. Maecenas at justo rhoncus, rhoncus sapien nec, porttitor nibh. Nunc eu imperdiet metus. In lectus orci, fermentum eu nunc eget, rutrum consectetur tellus. Cras finibus massa maximus, ultrices nisl in, pharetra libero.
               Suspendisse non porttitor massa. Morbi semper ullamcorper mauris, in iaculis leo bibendum in. Vivamus vehicula et dui id venenatis. Cras nec posuere erat. Sed convallis sapien sed dolor rutrum, nec semper risus placerat. Mauris facilisis lacinia quam a hendrerit. Quisque consequat neque diam, vitae sollicitudin turpis venenatis sed.
               Phasellus lacinia massa tortor, ut imperdiet augue bibendum vitae. Vivamus dictum diam congue placerat tristique. Etiam at purus purus. Pellentesque dignissim pretium ipsum, quis ultricies nulla lobortis id. Donec ante est, scelerisque non risus nec, tempus efficitur velit. Proin rhoncus tortor nibh, eu volutpat leo sagittis nec. Cras at justo volutpat, consequat enim ut, condimentum nisi. Aliquam eu nibh et metus placerat sodales non mollis ex.
               Praesent ac nisi turpis. Proin ut laoreet nibh, vel rutrum ex. Vestibulum aliquam tellus ac purus congue, at varius dolor hendrerit. Proin id eros rutrum, aliquet lorem non, maximus est. Donec sit amet tempor erat. Mauris quis velit nec magna tristique maximus in at nisl. Vivamus porta aliquam ipsum a iaculis. Nulla eget sollicitudin ex. Nam non semper nulla. Sed fringilla luctus finibus. Sed nulla tortor, tincidunt at dignissim eu, tristique mollis dui.
           '''
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Inicio de sesión del OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Iniciar sesión', form=form, providers=app.config['OPENID_PROVIDERS'])