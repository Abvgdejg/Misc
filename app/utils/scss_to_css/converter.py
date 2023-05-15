import sass

input_path = "sass/example.scss"
output_path = "css/example.css"
compressing_type = 'expanded'

with open(output_path, "w") as css_file:
    css = sass.compile(filename=(input_path), output_style=compressing_type)
    css_file.write(css)
    
    
