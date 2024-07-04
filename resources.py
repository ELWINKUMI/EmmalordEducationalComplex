import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_header(c, width, height, title):
    # School Header
    c.setFillColorRGB(0.01, 0.21, 0.21)  # Dark green header
    c.rect(0, height - 100, width, 100, fill=1)
    
    c.drawImage("images/logo.png", 30, height - 80, width=60, height=60)
    c.setFillColorRGB(1, 1, 1)  # White text
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, height - 40, "EMMALORD EDUCATIONAL COMPLEX")
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 60, "P.O BOX 961, DUMASUA - SUNYANI")
    c.drawString(100, height - 75, "Knowledge is Power")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(width / 2 - c.stringWidth(title, "Helvetica-Bold", 16) / 2, height - 130, title)

def create_pdf_resource(title, filename, content):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    draw_header(c, width, height, title)
    
    c.setFont("Helvetica", 12)
    y_position = height - 180

    for paragraph in content:
        for line in paragraph.split("\n"):
            c.drawString(50, y_position, line)
            y_position -= 15
            if y_position < 50:
                c.showPage()
                draw_header(c, width, height, title)
                y_position = height - 100  # Adjusted position to avoid overlapping with header

    c.save()

def create_academic_calendar():
    content = [
        "September:\n - 5th: First Day of School\n - 24th: School Resumes\n",
        "October:\n - 15th: PTA Meeting\n",
        "December:\n - 23rd: Ourday/Vacation\n",
        "January:\n - 3rd: School Resumes\n",
        "April:\n - 15th: Mid-Term Break\n",
        "August:\n - 5th: Graduation\n",
    ]
    create_pdf_resource("Academic Calendar", "resources/academic_calendar.pdf", content)

def create_student_handbook():
    content = [
        "Welcome to Emmalord Educational Complex!",
        "Our mission is to provide quality education and foster personal growth.",
        "School Rules and Regulations:\n1. Be respectful to all staff and students.\n2. Maintain punctuality and attend all classes regularly.\n3. Adhere to the dress code.\n4. No use of mobile phones during school hours.\n5. Complete all assignments on time.",
        "Academic Policies:\n- Students must achieve a minimum of 60% in all subjects.\n- Regular assessments will be conducted to monitor progress.\n- Extra help sessions are available for students who need additional support.",
    ]
    create_pdf_resource("Student Handbook", "resources/student_handbook.pdf", content)

def create_parent_guide():
    content = [
        "Dear Parents,",
        "Welcome to Emmalord Educational Complex. We are delighted to partner with you in your child's education.",
        "Parental Involvement:\n- Attend all PTA meetings.\n- Encourage your child to complete homework on time.\n- Monitor your child's academic progress and communicate with teachers.",
        "School Communication:\n- We use email and SMS to send important updates.\n- Feel free to contact us at info@emmalord.edu for any queries or concerns.",
        "Together, we can ensure the success and well-being of your child.",
    ]
    create_pdf_resource("Parent Guide", "resources/parent_guide.pdf", content)

def create_tutoring_services():
    content = [
        "Tutoring Services at Emmalord Educational Complex",
        "We offer tutoring services to help students excel in their academics.",
        "Subjects Offered:\n- Mathematics\n- Science\n- English\n- Social Studies\n",
        "Tutoring Schedule:\n- Monday to Friday: 3 PM - 5 PM\n- Saturday: 9 AM - 12 PM",
        "To enroll your child in our tutoring program, please contact the administration office.",
    ]
    create_pdf_resource("Tutoring Services", "resources/tutoring_services.pdf", content)

def create_college_prep():
    content = [
        "College Preparation Guide",
        "At Emmalord Educational Complex, we prepare our students for college and beyond.",
        "Steps to College Preparation:\n1. Research potential colleges and programs.\n2. Prepare for standardized tests (SAT, ACT).\n3. Participate in extracurricular activities.\n4. Maintain a high GPA.\n5. Seek guidance from college counselors.",
        "Important Dates:\n- SAT Registration: August 1\n- ACT Registration: September 15\n- College Application Deadlines: November 30",
    ]
    create_pdf_resource("College Preparation Guide", "resources/college_prep.pdf", content)

def create_financial_aid():
    content = [
        "Financial Aid Information",
        "Emmalord Educational Complex offers financial aid to support students in need.",
        "Types of Financial Aid:\n- Scholarships\n- Grants\n- Work-Study Programs\n",
        "How to Apply:\n1. Complete the financial aid application form.\n2. Submit proof of income and financial status.\n3. Meet with the financial aid advisor.",
        "Application Deadlines:\n- Fall Semester: June 1\n- Spring Semester: November 1",
        "For more information, please contact our financial aid office at financialaid@emmalord.edu.",
    ]
    create_pdf_resource("Financial Aid Information", "resources/financial_aid.pdf", content)

# Generate the PDFs
create_academic_calendar()
create_student_handbook()
create_parent_guide()
create_tutoring_services()
create_college_prep()
create_financial_aid()
