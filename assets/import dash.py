import dash
import dash_html_components as html

# Note: You do not need to specify external_stylesheets since styles.css is in the assets folder.
# Dash automatically serves CSS files in the assets folder.

app = dash.Dash(__name__)

app.title = "Global Six Sigma Concept Hub"

app.layout = html.Div(className='container', children=[
    html.H1("Global Six Sigma Concept Hub makes advanced, quality education accessible to capable students everywhere by delivering completely free online offerings."),
    html.P("The University is a community of students, alumni, faculty, and partner organizations dedicated to supporting each other in lifelong learning."),
    html.H2("Are you ready to pursue your career as a quantitative analyst?"),
    html.P("Our accredited two-year MSc in Financial Engineering Program, led by industry and academic experts, is where mathematics, computer science, and financial theory converge."),
    html.P("Accepted students join thousands of students in the world’s largest Financial Engineering Program, completely free of cost."),
    html.Ul(children=[
        html.Li("Mathematical + Computational Modeling"),
        html.Li("Derivative Pricing"),
        html.Li("Deep Learning"),
        html.Li("Financial Data Visualization and Analysis"),
        html.Li("Stochastic Modeling"),
        html.Li("Portfolio Management"),
        html.Li("Financial Econometrics"),
        html.Li("Machine Learning"),
        html.Li("Risk Management"),
    ]),
    html.H2("Data science skills are in demand across industries."),
    html.P("That’s why the credentialed 16-week Applied Data Science Lab pushes students to tackle real-world problems and build the foundation skills to work in data science. Walk away with a portfolio of projects in just a few months."),
    html.Ul(children=[
        html.Li("Data Analysis + Visualization"),
        html.Li("Machine Learning Ethics"),
        html.Li("Predictive Model-Building"),
    ]),
    html.H2("Our Mission", style={'marginTop': '20px'}),
    html.P("A global mission, a global community: Education is most effective when educators, employers, and students work together."),
    html.Blockquote(children=[
        html.P('“The challenge was real. If you are passionate about math and finance, and considering a MScFE program, I’d say go for it!”'),
    ], style={'fontStyle': 'italic', 'marginLeft': '20px', 'marginRight': '20px'}),
    html.P("Global Six Sigma Concept Hub President recently traveled to the World Economic Forum in Davos to speak about AI, flexible schedules, and the future of work."),
    html.P("An experience that combines theoretical knowledge, practical applications, and collaborative learning opportunities."),
    html.P("Exploring Predictive AI's developing role in education and business with industry experts."),
    html.P("Our students are committed lifelong learners who balance competing priorities to grow their skills and advance their careers. Learning with peers worldwide, they master the communication and collaboration skills necessary for modern work and inspire each other to meet their goals."),
    html.Div(children=[
        html.P("Our offerings are designed to help students build high-demand skills in financial engineering and data sciences. Discover the best fit for you."),
        html.P("Contact: raymondonwude@outlook.com"),  # Your email contact
    ], style={'margin': '20px'}),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# Load the CSV file
data = pd.read_csv("/home/raymondonwude/Downloads/sarah_cookies_sales_data.csv", parse_dates=['Date'])
