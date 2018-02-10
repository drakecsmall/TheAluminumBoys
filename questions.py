Answerhtml=""" <dd class="fake-input answer col col-xs-6 thumb-xs-inline " data-outcome="2412">
                <input type="radio" name="question-3272" id="7189-answer-14569" value="2412">
                <label for="7189-answer-14569" class="" data-track-action="Answer Selected" data-track-label="/quiz/und-hungry-hogg-have-aten-oll-th-bibles-een-aur-ve-7189">
                    <div class="answer-container content-box">
                        

                        <div class="inner">Answer_______</div>
                    </div>
                </label>
                
            </dd>"""
Questionhtml="""
<li class="question" data-unanswered="true">
    <dl class="layout-stacked">
        <dt class="prompt">Question_______</dt>

        <div class="row">

        
        Answers_______

          
            </div>
 
    </dl>
</li>"""

class question:
    def __init__(self):
        self.question=""
        self.answers={
            "answer1":1,
            "answer2":0,
            "answer3":0,
            "answer4":0
        }
        self.answertext=""
    def __init__(self,question,answers,answertext):
        self.question=question
        self.answers=answers
        self.answertext=answertext

        def formattedquestion(self):
            global Questionhtml
            global Answerhtml
            answers = '\n'.join([Answerhtml.replace("Answer_______",i) for i in self.answers.keys()])
            return Questionhtml.replace("Question_______",self.question).replace("Answers_______",answers)

questions=[]
questions.append(question("How many sanitation trucks run in Schenectady?",
                 {"220":1,"160":0,"50":0,"85":0},"Schenectady County is running 220 sanitation trucks to keep our streets clean!"))
questions.append(question("How many stops are on the average Schenectady sanitation route?",
                 {"266":1,"198":0,"180":0,"140":0},"Each truck has a crew of 2 individuals"))
questions.append(question("How many tons of garbage are collected every week in Schenectady?",
                 {"180":0,"270":0,"60":1,"94":0},"Schenectady County produces 60 tons of garbage weekly"))
questions.append(question("Where is the largest waste disposal location in the area?",
                 {"Schenectady":1,"Latham":0,"Colonie":0,"Scotia":0},"Republic Services Schenectady Transfer Station handles the greatest volume of waste in the Capital Region"))
questions.append(question("Which of the following cannot be recylced?",
                 {"Take-Out food containers":1,"Glass bottles":0,"Plastic bottles":0,"Wood":0},"Any grease or food particles that may be present can potentially damage and/or contaminate the other materials that are to be recycled"))
questions.append(question("What does the number on a plastic recyleable represent?",
                 {"The number of times the material can be recycled":0,"The thickness of the plastic":0,"It is a code that represents the type of plastic":1,"It is a represnetation of the color":0},"The number 1 represents PETE, 2 HDPE, 3 polyvinyl chloride, 4 LDPE, 5 polypropylene, 6 polystyrene."))
questions.append(question("How many miles does the average garbage truck drive on pick-up day?",
                 {"68":1,"91":0,"84":0,"109":0},"Most trucks have over 50,000 miles on them, which is about 9 years of service."))
