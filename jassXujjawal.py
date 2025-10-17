import pyttsx3
import speech_recognition as sr
import wikipedia
import pyautogui
import pyjokes
import datetime
import webbrowser
import random
import time
import sys

class HRInterviewAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.8)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Interview questions organized by category
        self.questions = self._load_questions()
        self.current_question_index = 0
        self.interview_active = False
        
        # Calibrate microphone for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
    
    def _load_questions(self):
        """Load structured interview questions based on Ujjawal Raj's resume"""
        questions = {
            "technical": [
                "Can you walk me through your experience with Python and how you've applied it in your AI projects at Hewlett Packard and GE Aerospace?",
                "Your resume mentions working with C++ for the Power of Two Max Heap project. What specific challenges did you face with memory management and optimization?",
                "How did you approach designing and implementing RESTful APIs in your projects, and what considerations did you make for scalability?",
                "Could you explain your experience with AWS Elastic Beanstalk and how you ensured reliable deployment for your applications?",
                "What was your role in the Utility Plant Optimizer project, and how did you handle data preprocessing and model evaluation?",
                "How have you used React and Vue.js in different projects, and what are the key differences you've observed between these frameworks?",
                "Can you describe your experience with SQL database design and optimization in your Walmart Global Tech internship?"
            ],
            "ai_ml": [
                "In your AI chatbot integration work, how did you approach prompt engineering and what techniques did you find most effective?",
                "Could you explain a time when you had to preprocess complex datasets for machine learning, and what strategies you used to ensure data quality?",
                "What metrics did you use to evaluate your predictive models at Blue Space Consulting, and how did you interpret these results?",
                "How did you handle the challenge of integrating AI components with existing software systems in your projects?",
                "Can you discuss your experience with model deployment and how you ensured your AI solutions were production-ready?"
            ],
            "practical_scenario": [
                "During your HP internship where you improved code coverage, what specific strategies did you implement and what was the outcome?",
                "When scaling hosting solutions at AWS, what were the key technical challenges you faced and how did you overcome them?",
                "Could you describe a complex front-end feature you built for GE Aerospace and how you ensured it met both user requirements and performance standards?",
                "Tell me about a time you had to debug a critical issue in production. What was your systematic approach to identifying and resolving the problem?",
                "In your SDLC implementation project, how did you balance agile development practices with the need for thorough testing and documentation?"
            ],
            "behavioral": [
                "Can you describe a situation where you had to collaborate with a difficult team member on a technical project? How did you handle it?",
                "Tell me about a time you had to learn a new technology quickly to meet project deadlines. What was your learning strategy?",
                "How do you approach giving and receiving technical feedback in a hybrid work environment?",
                "Describe a situation where you had to make a technical decision with incomplete information. What was your thought process?",
                "How do you prioritize tasks when working on multiple projects with competing deadlines, like during your concurrent internships?"
            ],
            "career_motivation": [
                "What specifically draws you to AI and software development roles, and how have your internships shaped this interest?",
                "Looking back at your five internships, what was the most valuable lesson you learned about working in the tech industry?",
                "Where do you see your career progressing in the next 3-5 years, and what skills are you looking to develop?",
                "How has your Bachelor of Computer Applications degree prepared you for real-world software engineering challenges?",
                "What type of work environment and projects motivate you the most, based on your diverse internship experiences?"
            ]
        }
        return questions
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice input and convert to text"""
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
            
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return "timeout"
        except sr.UnknownValueError:
            return "unknown"
        except sr.RequestError:
            return "error"
    
    def start_interview(self):
        """Begin the HR interview session"""
        self.speak("Hello! I'm your HR Interview Assistant. I'll be conducting a comprehensive interview based on Ujjawal Raj's resume.")
        self.speak("The interview will cover technical knowledge, AI understanding, practical scenarios, behavioral questions, and career motivation.")
        self.speak("You can say 'next question' to move forward, 'repeat question' to hear it again, or 'stop interview' to end the session.")
        
        self.interview_active = True
        self.current_question_index = 0
        self.ask_questions()
    
    def ask_questions(self):
        """Ask interview questions in a structured manner"""
        categories = list(self.questions.keys())
        question_pool = []
        
        # Create a balanced mix of questions from all categories
        for category in categories:
            question_pool.extend(self.questions[category])
        
        random.shuffle(question_pool)  # Randomize question order
        
        for i, question in enumerate(question_pool):
            if not self.interview_active:
                break
                
            self.current_question_index = i
            self.speak(f"Question {i+1} of {len(question_pool)}: {question}")
            self.speak("Please take your time to answer. Say 'next question' when you're ready to continue.")
            
            # Wait for user to indicate they're ready for next question
            while True:
                response = self.listen()
                if "next question" in response:
                    break
                elif "repeat question" in response:
                    self.speak(f"Repeating question: {question}")
                elif "stop interview" in response:
                    self.end_interview()
                    return
                elif response in ["timeout", "unknown", "error"]:
                    self.speak("I didn't catch that. Please say 'next question' to continue or 'stop interview' to end.")
                else:
                    self.speak("Please say 'next question' to continue to the next question.")
        
        self.speak("That concludes all the interview questions. Thank you for your participation!")
        self.interview_active = False
    
    def end_interview(self):
        """End the interview session"""
        self.speak("Ending the interview session. Thank you for your time!")
        self.interview_active = False
    
    def provide_evaluation_guide(self):
        """Provide HR evaluation criteria"""
        guide = """
        HR EVALUATION GUIDE FOR UJJAWAL RAJ'S INTERVIEW:
        
        TECHNICAL KNOWLEDGE - Listen for:
        • Depth of understanding in Python, C++, and frameworks mentioned
        • Specific examples of technical implementation
        • Problem-solving approach and methodology
        • Understanding of software architecture principles
        
        AI & ML UNDERSTANDING - Listen for:
        • Clear explanation of AI concepts and their practical application
        • Experience with data preprocessing and model evaluation
        • Understanding of production deployment challenges
        • Knowledge of current AI trends and limitations
        
        PRACTICAL SCENARIOS - Listen for:
        • Structured problem-solving approach
        • Learning from past experiences
        • Ability to handle real-world constraints
        • Technical decision-making process
        
        BEHAVIORAL SKILLS - Listen for:
        • Communication clarity and confidence
        • Team collaboration examples
        • Adaptability in hybrid environments
        • Growth mindset and learning orientation
        
        CAREER MOTIVATION - Listen for:
        • Alignment between interests and role requirements
        • Learning from internship experiences
        • Realistic career planning
        • Enthusiasm for continuous learning
        """
        print(guide)
        self.speak("I've displayed the HR evaluation guide on screen. This outlines what to listen for in Ujjawal's responses.")
    
    def run(self):
        """Main assistant loop"""
        self.speak("HR Interview Assistant initialized. Say 'start interview' to begin, 'evaluation guide' for assessment criteria, or 'exit' to quit.")
        
        while True:
            command = self.listen()
            
            if "start interview" in command:
                self.start_interview()
            elif "evaluation guide" in command:
                self.provide_evaluation_guide()
            elif "exit" in command or "quit" in command:
                self.speak("Goodbye!")
                break
            elif "timeout" in command:
                continue
            elif "unknown" in command or "error" in command:
                self.speak("I didn't understand that. Please say 'start interview', 'evaluation guide', or 'exit'.")
            else:
                self.speak("Please say 'start interview' to begin the interview, 'evaluation guide' for assessment criteria, or 'exit' to quit.")

# Additional utility functions
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}"

def tell_joke():
    return pyjokes.get_joke()

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Please be more specific: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

if __name__ == "__main__":
    assistant = HRInterviewAssistant()
    assistant.run()