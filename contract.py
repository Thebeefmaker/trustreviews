# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

class TrustReviews(gl.Contract):
    reviews: DynArray[dict]

    def __init__(self):
        self.reviews = []

    @gl.public.write
    def submit_review(self, subject: str, review_text: str, reviewer: str) -> None:
        prompt = f"""
        You are a review moderation AI. Analyze this review and determine if it is genuine.
        
        Subject being reviewed: {subject}
        Review: {review_text}
        
        A genuine review:
        - Contains specific details or personal experience
        - Is not purely promotional or purely hateful
        - Makes sense in context
        - Is not spam or gibberish
        
        Respond with exactly one word: GENUINE or FAKE
        """
        
        result = gl.exec_prompt(prompt).strip().upper()
        is_genuine = "GENUINE" in result
        
        self.reviews.append({
            "subject": subject,
            "review": review_text,
            "reviewer": reviewer,
            "verified": is_genuine,
            "status": "✅ Verified Genuine" if is_genuine else "❌ Flagged as Fake"
        })

    @gl.public.view
    def get_reviews(self) -> list:
        return self.reviews

    @gl.public.view
    def get_verified_reviews(self) -> list:
        return [r for r in self.reviews if r["verified"]]