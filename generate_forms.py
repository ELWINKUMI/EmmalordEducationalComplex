from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def draw_header(c, width, height):
    # School Header
    c.setFillColorRGB(0.01, 0.21, 0.21)  # Dark green header
    c.rect(0, height - 100, width, 100, fill=1)
    
    c.drawImage("images/logo.png", 30, height - 80, width=60, height=60)
    c.setFillColorRGB(0.01, 0.21, 0.21)  # Dark green header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, height - 40, "EMMALORD EDUCATIONAL COMPLEX")
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 60, "P.O BOX 961, DUMASUA - SUNYANI")
    c.drawString(100, height - 75, "Knowledge is Power")

def create_form(title, filename, fields):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    def draw_header(c, width, height):
        # School Header
        c.setFillColorRGB(1, 1, 1)  # White header
        c.rect(0, height - 100, width, 100, fill=1)
        
        c.drawImage("images/logo.png", 30, height - 80, width=60, height=60)
        c.setFillColorRGB(0.01, 0.21, 0.21)  # Black text
        c.setFont("Helvetica-Bold", 18)
        c.drawString(100, height - 40, "EMMALORD EDUCATIONAL COMPLEX")
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 60, "P.O BOX 961, DUMASUA - SUNYANI")
        c.drawString(100, height - 75, "Knowledge is Power")

    def create_form(title, filename, fields):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        def draw_first_page_header(c, width, height):
            c.setFillColorRGB(1, 1, 1)  # White background
            c.rect(0, 0, width, height, fill=1)
            draw_header(c, width, height)
            c.setFillColorRGB(0, 0, 0)  # Black text
            c.setFont("Helvetica-Bold", 16)
            c.drawString(200, height - 130, title)
            c.setFont("Helvetica", 10)
            c.drawString(width - 130, height - 150, "Passport Picture")
            c.rect(width - 140, height - 200, 100, 100, stroke=1, fill=0)

        def draw_subsequent_page_header(c, width, height):
            c.setFillColorRGB(1, 1, 1)  # White background
            c.rect(0, 0, width, height, fill=1)
            c.setFillColorRGB(0, 0, 0)  # Black text
            c.setFont("Helvetica-Bold", 16)
            c.drawString(200, height - 30, title)

        def draw_page(c, width, height):
            if c.getPageNumber() == 1:
                draw_first_page_header(c, width, height)
            else:
                draw_subsequent_page_header(c, width, height)

        draw_page(c, width, height)

        c.setFont("Helvetica", 12)
        y_position = height - 220

        # Form Fields
        for field, width_offset in fields:
            if width_offset == 0:  # Section header
                c.setFont("Helvetica-Bold", 12)
                c.setFillColorRGB(0, 0, 0)  # Black text
                c.drawString(50, y_position, field)
                y_position -= 20
            else:
                c.setFont("Helvetica", 12)
                c.setFillColorRGB(0, 0, 0)  # Black text
                c.drawString(50, y_position, field)
                y_position -= 25
                c.setStrokeColorRGB(0.8, 0.8, 0.8)  # Light gray line
                c.line(50, y_position, 50 + width_offset, y_position)
                y_position -= 15
            
            if y_position < 50:
                c.showPage()
                draw_page(c, width, height)
                y_position = height - 50

        c.save()

    def create_student_form():
        fields = [
            ("Name of Child:", 300),
            ("Age:", 100),
            ("Date of Birth:", 200),
            ("Place of Birth:", 300),
            ("Class Required:", 300),
            ("Last School attended:", 400),
            ("Reason for leaving school:", 400),
            ("Religious Denomination:", 400),
            ("Christian [   ]  Muslim [   ]  Other [ ] please tick ✓", 400),
            ("Father's Name:", 300),
            ("Father's Contact:", 300),
            ("Father's Occupation:", 300),
            ("House No./Location:", 300),
            ("Mother's Name:", 300),
            ("Mother's Contact:", 300),
            ("Mother's Occupation:", 300),
            ("House No./Location:", 300),
            ("Relationship of Child:", 300),
            ("Guardian's Name:", 300),
            ("Guardian's Contact:", 300),
            ("Guardian's Occupation:", 300),
            ("House No./Location:", 300),
            ("MEDICAL INFORMATION", 0),
            ("1. Does your child have any allergies?", 0),
            ("Yes [    ]  No [    ] please tick ✓", 0),
            ("   If yes, please give details:", 300),
            ("2. Does your child have a disability?", 0),
            ("Yes [    ]  No [    ] please tick ✓", 0),
            ("3. Are there any health problems of which we should be aware?", 0),
            ("Yes [    ]  No [    ] please tick ✓", 0),
            ("UNDERTAKING BY PARENT / GUARDIAN", 0),
            ("I, ________________________ (the parent [    ] or guardian [    ])", 0),
            ("of the above named learner do hereby certify that the statements made on", 0),
            ("this form are correct and that I will take responsibility for the upkeep of my ward in course of", 0),
            ("his/her stay in Emmalord Educational Complex.", 0),
            ("PARENT TO NOTE", 0),
            ("Photocopy of child's birth certificate must be attached.", 0),
        ]
        create_form("ADMISSION FORM", "student_application.pdf", fields)

    def create_health_form():
        fields = [
            ("Mother's Occupation:", 300),
            ("House No./Location:", 300),
            ("Relationship of Child:", 300),
            ("MEDICAL INFORMATION", 0),
            ("1. Does your child have any allergies?", 0),
            ("Yes [    ]  No [    ] please tick ✓", 0),
            ("   If yes, please give details:", 300),
            ("2. Does your child have a disability?", 0),
            ("Yes [    ]  No [    ] please tick ✓", 0),
            ("3. Are there any health problems of which we should be aware?", 0),
            ("Yes [    ]  No [    ] please tick ✓", 0),
            ("UNDERTAKING BY PARENT / GUARDIAN", 0),
            ("I, ________________________ (the parent [    ] or guardian [    ])", 0),
            ("of the above named learner do hereby certify that the statements made on", 0),
            ("this form are correct and that I will take responsibility for the upkeep of my ward in course of", 0),
            ("his/her stay in Emmalord Educational Complex.", 0),
            ("Additional Information:", 300),
            ("Please provide any additional information you think is important:", 300),
        ]
        create_form("HEALTH RECORD FORM", "health_record.pdf", fields)

    def create_recommendation_form():
        fields = [
            ("Recommender's Name:", 300),
            ("Recommender's Contact:", 300),
            ("Relationship to Student:", 300),
            ("Recommender's Position:", 300),
            ("How long have you known the student?", 300),
            ("In what capacity have you known the student?", 300),
            ("Please rate the student in the following areas:", 0),
            ("Academic Performance:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("Social Skills:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("Discipline:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("Leadership Skills:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("Attendance:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("Punctuality:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("General Conduct:", 0),
            ("Excellent [    ]  Good [    ]  Average [    ]  Poor [    ]", 0),
            ("Any other comments:", 300),
            ("Recommendation:", 0),
            ("_________________________________________________________________", 0),
            ("_________________________________________________________________", 0),
            ("_________________________________________________________________", 0),
            ("_________________________________________________________________", 0),
            ("_________________________________________________________________", 0),
            ("_________________________________________________________________", 0),
            ("Signature:", 200),
            ("Date:", 200),
        ]
        create_form("RECOMMENDATION FORM", "recommendation.pdf", fields)

    # Generate the forms
    create_student_form()
    create_health_form()
    create_recommendation_form()
    def draw_first_page_header(c, width, height):
        c.setFillColorRGB(0.95, 0.95, 1)  # Light blue background
        c.rect(0, 0, width, height, fill=1)
        draw_header(c, width, height)
        c.setFillColorRGB(0.01, 0.21, 0.21)  # Dark green text
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, height - 130, title)
        c.setFont("Helvetica", 10)
        c.drawString(width - 130, height - 150, "Passport Picture")
        c.rect(width - 140, height - 200, 100, 100, stroke=1, fill=0)

    def draw_subsequent_page_header(c, width, height):
        c.setFillColorRGB(0.95, 0.95, 1)  # Light blue background
        c.rect(0, 0, width, height, fill=1)
        c.setFillColorRGB(0.01, 0.21, 0.21)  # Dark green text
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, height - 30, title)

    def draw_page(c, width, height):
        if c.getPageNumber() == 1:
            draw_first_page_header(c, width, height)
        else:
            draw_subsequent_page_header(c, width, height)

    draw_page(c, width, height)

    c.setFont("Helvetica", 12)
    y_position = height - 220

    # Form Fields
    for field, width_offset in fields:
        if width_offset == 0:  # Section header
            c.setFont("Helvetica-Bold", 12)
            c.setFillColorRGB(0.01, 0.21, 0.21)  # Dark green text
            c.drawString(50, y_position, field)
            y_position -= 20
        else:
            c.setFont("Helvetica", 12)
            c.setFillColorRGB(0, 0, 0)  # Black text
            c.drawString(50, y_position, field)
            y_position -= 25
            c.setStrokeColorRGB(0.8, 0.8, 0.8)  # Light gray line
            c.line(50, y_position, 50 + width_offset, y_position)
            y_position -= 15
        
        if y_position < 50:
            c.showPage()
            draw_page(c, width, height)
            y_position = height - 50

    c.save()

def create_student_form():
    fields = [
        ("Name of Child:", 300),
        ("Age:", 100),
        ("Date of Birth:", 200),
        ("Place of Birth:", 300),
        ("Class Required:", 300),
        ("Last School attended:", 400),
        ("Reason for leaving school:", 400),
        ("Religious Denomination:", 400),
        ("Christian [   ]  Muslim [   ]  Other [   ] please tick ✓", 400),
        ("Father's Name:", 300),
        ("Father's Contact:", 300),
        ("Father's Occupation:", 300),
        ("House No./Location:", 300),
        ("Mother's Name:", 300),
        ("Mother's Contact:", 300),
        ("Mother's Occupation:", 300),
        ("House No./Location:", 300),
        ("Relationship of Child:", 300),
        ("Guardian's Name:", 300),
        ("Guardian's Contact:", 300),
        ("Guardian's Occupation:", 300),
        ("House No./Location:", 300),
        ("MEDICAL INFORMATION", 0),
        ("1. Does your child have any allergies?", 0),
        ("Yes [   ]  No [   ] please tick ✓", 0),
        ("   If yes, please give details:", 300),
        ("2. Does your child have a disability?", 0),
        ("Yes [   ]  No [   ] please tick ✓", 0),
        ("3. Are there any health problems of which we should be aware?", 0),
        ("Yes [   ]  No [   ] please tick ✓", 0),
        ("UNDERTAKING BY PARENT / GUARDIAN", 0),
        ("I, ________________________ (the parent [   ] or guardian [   ])", 0),
        ("of the above named learner do hereby certify that the statements made on", 0),
        ("this form are correct and that I will take responsibility for the upkeep of my ward in course of", 0),
        ("his/her stay in Emmalord Educational Complex.", 0),
        ("PARENT TO NOTE", 0),
        ("Photocopy of child's birth certificate must be attached.", 0),
    ]
    create_form("ADMISSION FORM", "student_application.pdf", fields)

def create_health_form():
    fields = [
        ("Mother's Occupation:", 300),
        ("House No./Location:", 300),
        ("Relationship of Child:", 300),
        ("MEDICAL INFORMATION", 0),
        ("1. Does your child have any allergies?", 0),
        ("Yes [   ]  No [   ] please tick ✓", 0),
        ("   If yes, please give details:", 300),
        ("2. Does your child have a disability?", 0),
        ("Yes [   ]  No [   ] please tick ✓", 0),
        ("3. Are there any health problems of which we should be aware?", 0),
        ("Yes [   ]  No [   ] please tick ✓", 0),
        ("UNDERTAKING BY PARENT / GUARDIAN", 0),
        ("I, ________________________ (the parent [   ] or guardian [   ])", 0),
        ("of the above named learner do hereby certify that the statements made on", 0),
        ("this form are correct and that I will take responsibility for the upkeep of my ward in course of", 0),
        ("his/her stay in Emmalord Educational Complex.", 0),
        ("Additional Information:", 300),
        ("Please provide any additional information you think is important:", 300),
    ]
    create_form("HEALTH RECORD FORM", "health_record.pdf", fields)

def create_recommendation_form():
    fields = [
        ("Recommender's Name:", 300),
        ("Recommender's Contact:", 300),
        ("Relationship to Student:", 300),
        ("Recommender's Position:", 300),
        ("How long have you known the student?", 300),
        ("In what capacity have you known the student?", 300),
        ("Please rate the student in the following areas:", 0),
        ("Academic Performance:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("Social Skills:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("Discipline:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("Leadership Skills:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("Attendance:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("Punctuality:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("General Conduct:", 0),
        ("Excellent [   ]  Good [   ]  Average [   ]  Poor [   ]", 0),
        ("Any other comments:", 300),
        ("Recommendation:", 0),
        ("_________________________________________________________________", 0),
        ("_________________________________________________________________", 0),
        ("_________________________________________________________________", 0),
        ("_________________________________________________________________", 0),
        ("_________________________________________________________________", 0),
        ("_________________________________________________________________", 0),
        ("Signature:", 200),
        ("Date:", 200),
    ]
    create_form("RECOMMENDATION FORM", "recommendation.pdf", fields)

# Generate the forms
create_student_form()
create_health_form()
create_recommendation_form()
