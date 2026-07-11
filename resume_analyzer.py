import os
import google.generativeai as genai

# Configure Google Gemini API Key
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)

class AIResumeAnalyzer:
    def __init__(self):
        # Using the fast and efficient flash model
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        self.system_prompt = (
            "You are an expert Technical Recruiter and Career Coach. Your job is to analyze the provided "
            "resume text, find missing keywords, evaluate formatting, and give a score out of 100 with "
            "clear, professional feedback on how to improve it for job markets."
        )

    def analyze_resume(self, resume_text, target_job):
        full_prompt = (
            f"{self.system_prompt}\n\n"
            f"Target Job Profile: {target_job}\n"
            f"Resume Text Content:\n{resume_text}\n\n"
            f"Please provide: 1. Overall Score (out of 100), 2. Key Missing Strengths, 3. Bulleted Improvement Tips."
        )
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"\n❌ Connection Error: Ensure your API key is correct. Details: {str(e)}"

def main():
    analyzer = AIResumeAnalyzer()
    
    print("\n" + "="*45)
    print("      AI RESUME PARSER & ANALYZER TOOL      ")
    print("="*45)
    
    target_job = input("Enter Target Job Profile (e.g., Python Developer, Data Analyst): ")
    
    print("\nPaste your Resume text below (Press Enter, then Ctrl+D or Ctrl+Z to submit):")
    
    # Reading multiline input for resume text
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
            
    resume_text = "\n".join(lines)
    
    if not resume_text.strip():
        print("\n❌ Resume content cannot be empty!")
        return

    print("\n🤖 AI HR Manager is reviewing your resume...")
    analysis_report = analyzer.analyze_resume(resume_text, target_job)
    
    print("\n" + "="*20 + " RESUME AUDIT REPORT " + "="*20)
    print(analysis_report)
    print("="*55)

if __name__ == "__main__":
    main()
