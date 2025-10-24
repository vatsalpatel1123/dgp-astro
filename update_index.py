import re

# Read the file
with open(r'D:\Projects\system\dgp-astro\src\pages\index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Update frontmatter to add component imports
content = content.replace(
    '---\n// index.astro\n---',
    '''---
// index.astro
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
import StickyCTA from '../components/StickyCTA.astro';
---'''
)

# Step 2: Remove navbar CSS styles (from line 52 to around line 317)
# Find and remove the NAVBAR STYLES section
navbar_css_pattern = r'/\* ============================================\s+NAVBAR STYLES\s+============================================ \*/.*?/\* ============================================\s+HERO SECTION\s+============================================ \*/'
content = re.sub(navbar_css_pattern, r'/* ============================================\n       HERO SECTION\n    ============================================ */', content, flags=re.DOTALL)

# Step 3: Remove navbar HTML (from <div class="nav-bar-dark"> to closing </div>)
navbar_html_pattern = r'<!-- ============================================\s+NAVBAR SECTION\s+============================================ -->\s*<div class="nav-bar-dark">.*?</div>\s*(?=<!-- ============================================)'
content = re.sub(navbar_html_pattern, r'', content, flags=re.DOTALL)

# Step 4: Add component usage at the beginning of body
content = content.replace(
    '<body>',
    '''<body>

  <!-- Navbar Component -->
  <Navbar />'''
)

# Step 5: Remove footer CSS styles
footer_css_pattern = r'/\* ============================================\s+FOOTER STYLES\s+============================================ \*/.*?/\* Floating CTA Buttons \*/'
content = re.sub(footer_css_pattern, r'/* Floating CTA Buttons - Handled by StickyCTA component */', content, flags=re.DOTALL)

# Step 6: Remove floating CTA CSS (already in component)
floating_css_pattern = r'/\* Floating CTA Buttons \*/.*?@media \(max-width: 991px\) \{'
content = re.sub(floating_css_pattern, r'    /* Responsive styles */\n    @media (max-width: 991px) {', content, flags=re.DOTALL)

# Step 7: Remove footer HTML
footer_html_pattern = r'<!-- ============================================\s+FOOTER SECTION\s+============================================ -->\s*<div class="footer">.*?</div>\s*(?=<!-- Floating CTA)'
content = re.sub(footer_html_pattern, r'', content, flags=re.DOTALL)

# Step 8: Remove floating CTA HTML and replace with component
floating_html_pattern = r'<!-- Floating CTA Buttons -->\s*<div class="floating-cta">.*?</div>'
content = re.sub(floating_html_pattern, r'<!-- Footer Component -->\n  <Footer />\n\n  <!-- Sticky CTA Component -->\n  <StickyCTA />', content, flags=re.DOTALL)

# Write the updated content
with open(r'D:\Projects\system\dgp-astro\src\pages\index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.astro updated successfully!")
print("- Added component imports")
print("- Replaced navbar with <Navbar /> component")
print("- Replaced footer with <Footer /> component")
print("- Replaced floating CTA with <StickyCTA /> component")
print("- Removed redundant CSS styles")
