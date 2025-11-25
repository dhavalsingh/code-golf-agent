from google import genai
c,h=genai.Client(),[]
while 1:h+=[{"role":"user","parts":[{"text":input("> ")}]}];r=c.models.generate_content(model="gemini-2.0-flash",contents=h);h+=[r.candidates[0].content];print(r.text)