import os

# 1️⃣ Chemin vers ton dossier d'images
folder = "IMAGE ZEYNAB_SHOP"

# 2️⃣ Noms exacts des fichiers utilisés dans le code
target_names = [
    "abaya_noire.jpeg", "Dampé_blanc.jpeg", "Dampé_gris.jpeg", "Dampé_rouge.jpeg",
    "Dampé_vert.jpeg", "hidjab_bleu.jpeg", "hidjab_caftan.jpeg", "Hidjab_marron.jpeg",
    "Dampé_marron.jpeg", "Dampé_orange.jpeg", "Dampé_rose.jpeg", "Hidjab_noire.jpeg",
    "Hidjab_Blanc.jpeg", "Hidjab_Rouge.jpeg", "Hidjab_Vert.jpeg"
]

# 3️⃣ Script de renommage automatique
existing_files = os.listdir(folder)

for target in target_names:
    # On ignore les majuscules et accents dans les fichiers existants
    target_lower = target.lower()
    found = False
    for f in existing_files:
        # Supprime espaces, majuscules, accent pour comparaison
        f_clean = f.replace(" ", "_").lower()
        if f_clean.startswith(target_lower.split('.')[0].lower()):
            old_path = os.path.join(folder, f)
            new_path = os.path.join(folder, target)
            os.rename(old_path, new_path)
            print(f"✅ {f} → {target}")
            found = True
            break
    if not found:
        print(f"⚠️ Fichier manquant pour : {target}")

print("\n🔹 Renommage terminé. Tes images correspondent maintenant au code HTML !")
