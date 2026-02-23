import json
import random
import os

# Generate 100 synthetic navbar examples with prompt + HTML/CSS code pairs
prompts = [
    "Create a responsive navbar with logo on the left and links on the right.",
    "Build a dark-themed navbar with dropdown menu for Services.",
    "Make a sticky top navbar with a login button on the right.",
    "Design a mobile-friendly navbar with hamburger menu.",
    "Build a navbar with a center-aligned logo and side links.",
    "Create a navbar using Tailwind CSS with hover effects.",
    "Make a simple navbar using Bootstrap.",
    "Responsive navbar with a search bar in the center.",
    "Sticky navbar that collapses on scroll for small screens.",
    "Navbar with social media icons on the right side."
]

html_snippets = [
    '''<nav class="flex justify-between items-center px-4 py-2 bg-white shadow">
  <div class="logo text-xl font-bold">Brand</div>
  <ul class="flex space-x-4">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>''',
    '''<nav class="bg-gray-900 text-white p-4">
  <div class="flex justify-between items-center">
    <span class="text-xl font-bold">Brand</span>
    <ul class="flex gap-4">
      <li><a href="#">Services</a></li>
      <li><a href="#">Portfolio</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </div>
</nav>''',
    '''<nav class="bg-blue-600 p-4 text-white sticky top-0">
  <div class="flex justify-between items-center">
    <h1 class="text-2xl">SiteName</h1>
    <button class="bg-white text-blue-600 px-3 py-1 rounded">Login</button>
  </div>
</nav>''',
    '''<nav class="bg-black text-white p-4">
  <div class="flex justify-between items-center">
    <div class="logo">MyApp</div>
    <div class="hamburger md:hidden">☰</div>
    <ul class="hidden md:flex gap-6">
      <li>Home</li>
      <li>Blog</li>
      <li>Contact</li>
    </ul>
  </div>
</nav>''',
    '''<nav class="p-4 bg-gray-100">
  <div class="text-center text-xl font-bold">CenteredLogo</div>
  <ul class="flex justify-between mt-2">
    <li><a href="#">Home</a></li>
    <li><a href="#">Features</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>'''
]

# Generate JSONL format
data = []
for i in range(100):
    prompt = random.choice(prompts)
    code = random.choice(html_snippets)
    data.append({"prompt": prompt, "code": code})

# Save as JSONL file
output_path = "/mnt/data/navbar_dataset_100.jsonl"
with open(output_path, "w") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")

output_path
