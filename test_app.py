# A simple CI test that parses our HTML to make sure we didn't break the layout tags!
def test_html_structure():
    with open("index.html", "r") as f:
        content = f.read()
        
    # Assert that critical structural tags exist
    assert "<!DOCTYPE html>" in content
    assert '<div id="answer"' in content
    assert '<div id="message"' in content or '<p id="message"' in content