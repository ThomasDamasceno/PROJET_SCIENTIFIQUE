import yaml
from jinja2 import Environment, FileSystemLoader

# Chargement des données du fichier YAML dans un dictionnaire Python
config = yaml.load(open('router_bbn.yaml'))

# Chargement Jinja2 template
env = Environment(loader = FileSystemLoader('.'))
template = env.get_template('interface_template.j2')

# Rendu grâce au template en utilisant les données et envoie de la sortie
print(template.render(config))


# Ecriture de la sortie dans un fichier texte
output = str(template.render(config))

with open("router_config.txt", "w") as f:
    f.write(output)
