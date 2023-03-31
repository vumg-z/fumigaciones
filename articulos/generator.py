import json

def read_template_file():
    with open("articulos/1/template.html", "r") as file:
        return file.read()

def create_new_html_file(filename, content):
    with open("articulos/1/"+filename, "w") as file:
        file.write(content)

def replace_content(template, json_object):
    new_content = template
    for key, value in json_object.items():
        if key == "imgs":
            new_content = new_content.replace("{{{imgs}}}", value[0])
        elif key == "h5s":
            new_content = new_content.replace("{{{h5s}}}", json_object["h5s_original"][0])
        elif key == "h5s_original":
            continue
        else:
            new_content = new_content.replace(f"{{{key}}}", value[0])
    return new_content

def read_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)

def main():
    json_filename = "articulos/articulos.json"  # Cambia esto por el nombre de tu archivo JSON
    articles = read_json_file(json_filename)
    template_content = read_template_file()

    for article in articles:
        new_filename = article["h5s"][0].replace(" ", "_") + ".html"
        new_content = replace_content(template_content, article)
        create_new_html_file(new_filename, new_content)

if __name__ == "__main__":
    main()