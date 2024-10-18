from spire.doc import *
from spire.doc.common import *

# Create a Word document
doc = Document()

# Add a section
section = doc.AddSection()

# Add a paragraph
paragraph = section.AddParagraph()
paragraph.AppendHyperlink("https://www-iceblue.com/", "Home Page", HyperlinkType.WebLink)

# Append line breaks
paragraph.AppendBreak(BreakType.LineBreak)
paragraph.AppendBreak(BreakType.LineBreak)

# Add an email link
paragraph.AppendHyperlink("mailto:support@e-iceblue.com", "Mail Us", HyperlinkType.EMailLink)

# Append line breaks
paragraph.AppendBreak(BreakType.LineBreak)
paragraph.AppendBreak(BreakType.LineBreak)

# Add a file link
filePath = "C:\\Users\\Administrator\\Desktop\\report.xlsx"
paragraph.AppendHyperlink(filePath, "Click to open the report", HyperlinkType.FileLink)

# Append line breaks
paragraph.AppendBreak(BreakType.LineBreak)
paragraph.AppendBreak(BreakType.LineBreak)

# Add another section and create a bookmark 
section2 = doc.AddSection()
bookmarkParagrapg = section2.AddParagraph()
bookmarkParagrapg.AppendText("Here is a bookmark")
start = bookmarkParagrapg.AppendBookmarkStart("myBookmark")
bookmarkParagrapg.Items.Insert(0, start)
bookmarkParagrapg.AppendBookmarkEnd("myBookmark")

# Link to the bookmark
paragraph.AppendHyperlink("myBookmark", "Jump to a location inside this document", HyperlinkType.Bookmark)

# Append line breaks
paragraph.AppendBreak(BreakType.LineBreak)
paragraph.AppendBreak(BreakType.LineBreak)

# Add an image link
image = "C:\\Users\\ADMIN\\Desktop\\python Scripts\\Opencv\\addedalone.jpg"
# picture = paragraph.AppendPicture(image)
paragraph.AppendHyperlink("myBookmark", image, HyperlinkType.Bookmark)

# Save to file
doc.SaveToFile("output/CreateHyperlinks_1.docx", FileFormat.Docx2019)
doc.Dispose()