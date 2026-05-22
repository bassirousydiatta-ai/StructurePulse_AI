# StructurePulse AI — Documentation Technique Complète
### Hackathon Digital Innov'Next 2026 · UMP Oujda

---

## 🎯 Vue d'ensemble

**StructurePulse AI** est une application web Django de surveillance structurelle en temps réel.
Elle reçoit les données d'un boîtier ESP32 + capteur ultrason, les analyse, et les affiche sur un dashboard avec alertes automatiques, historique filtrable, et export PDF.

---

## 📁 Structure du projet

```
structurepulse/
├── config/
│   ├── settings.py     # Configuration Django
│   └── urls.py         # Routes principales
├── monitor/
│   ├── models.py       # Modèle Mesure (SQLite)
│   ├── views.py        # Toute la logique (API + pages)
│   └── serializers.py  # Sérialisation JSON
├── templates/
│   ├── base.html       # Layout avec sidebar
│   ├── login.html      # Page de connexion
│   ├── dashboard.html  # Dashboard temps réel
│   └── historique.html # Historique + filtres
└── manage.py
```

---

## ⚡ Installation (à faire le jour du hackathon)

### 1. Prérequis
- Python 3.10+ installé
- pip disponible

### 2. Installer les dépendances

```bash
pip install django djangorestframework django-cors-headers reportlab
```

### 3. Décompresser le projet

```bash
unzip StructurePulse_WebApp.zip -d structurepulse
cd structurepulse
```

### 4. Initialiser la base de données

```bash
python manage.py migrate
```

### 5. Créer le compte admin

```bash
python manage.py createsuperuser
```
Ou utiliser le compte par défaut déjà configuré :
- **Username :** `admin`
- **Password :** `structurepulse2026`

> ⚠️ Si la base de données est fraîche (nouveau migrate), relancer :
```bash
echo "from django.contrib.auth import get_user_model; U=get_user_model(); U.objects.create_superuser('admin','admin@ump.ma','structurepulse2026')" | python manage.py shell
```

### 6. Lancer le serveur

```bash
python manage.py runserver 0.0.0.0:5000
```

> L'app est accessible sur `http://[IP_PC]:5000`
> L'IP de ton PC : `ipconfig` (Windows) ou `ifconfig` (Linux/Mac)

---

## 🌐 Pages disponibles

| URL | Description |
|-----|-------------|
| `http://[IP]:5000/` | Dashboard temps réel |
| `http://[IP]:5000/historique/` | Historique filtrable |
| `http://[IP]:5000/export/pdf/` | Télécharger rapport PDF |
| `http://[IP]:5000/login/` | Connexion admin |
| `http://[IP]:5000/admin/` | Interface d'administration Django |

---

## 📡 API (pour l'ESP32)

### Recevoir une mesure — `POST /data`

**URL :** `http://[IP]:5000/data`
**Headers :** `Content-Type: application/json`
**Body :**
```json
{
  "distance": 214.5,
  "deplacement": 2.3,
  "statut": "ALERTE"
}
```
**Réponse :**
```json
{"status": "ok", "id": 42}
```

### Lire les mesures — `GET /api/mesures/?n=50`

Retourne les 50 dernières mesures en JSON (ordre décroissant).

### Statistiques — `GET /api/stats/`

```json
{
  "total": 150,
  "derniere": { "id": 150, "distance": 214.5, "deplacement": 2.3, "statut": "ALERTE", "timestamp": "2026-05-22 11:30:00" },
  "moy_24h": 1.8,
  "max_24h": 5.2,
  "nb_alertes_24h": 12,
  "nb_critiques_24h": 3
}
```

---

## 📊 Fonctionnalités

### Dashboard (/)
- **4 KPIs** en temps réel : statut actuel, déplacement, alertes 24h, critiques 24h
- **Graphe linéaire** : déplacement des 50 dernières mesures avec seuils (2mm orange, 5mm rouge)
- **Donut chart** : répartition Normal / Alerte / Critique
- **Bannière d'alerte** clignotante en cas de statut CRITIQUE
- **Tableau** des 15 dernières mesures
- **Rafraîchissement automatique** toutes les 4 secondes

### Historique (/historique/)
- Filtrage par **statut** (Normal / Alerte / Critique)
- Filtrage par **date**
- Tableau des 200 dernières mesures filtrées

### Export PDF (/export/pdf/)
Génère automatiquement un rapport professionnel incluant :
1. Résumé exécutif (statut global, stats 24h)
2. Analyse financière avec **calcul ROI**
3. Tableau des 20 dernières mesures
4. Recommandations d'intervention automatiques

---

## 🔧 Seuils RDM (définis par l'ami Génie Civil)

| Déplacement | Statut | Couleur |
|-------------|--------|---------|
| < 2 mm | NORMAL | 🟢 Vert |
| 2 — 5 mm | ALERTE | 🟠 Orange |
| > 5 mm | CRITIQUE | 🔴 Rouge |

---

## 💰 Calcul ROI intégré dans le PDF

| Poste | Valeur |
|-------|--------|
| Maintenance curative annuelle | 150 000 DH |
| Maintenance prédictive avec solution | 45 000 DH |
| Coût StructurePulse AI/an | 6 200 DH |
| **Économie nette** | **98 800 DH** |
| **ROI** | **~1593%** |

---

## 🚨 Dépannage

**Erreur "Address already in use"**
```bash
python manage.py runserver 0.0.0.0:5001
# puis mettre à jour le SERVER_URL dans le code Arduino
```

**L'ESP32 reçoit Erreur HTTP -1**
1. Vérifier que le serveur tourne bien
2. Vérifier que l'ESP32 et le PC sont sur le même WiFi
3. Vérifier l'IP : `ipconfig` → chercher "Adresse IPv4"
4. Tester manuellement :
```bash
curl -X POST http://[IP]:5000/data -H "Content-Type: application/json" -d '{"distance":215,"deplacement":1.5,"statut":"NORMAL"}'
```
Doit retourner : `{"status": "ok", "id": ...}`

**Page blanche ou erreur 500**
```bash
# Activer les logs détaillés
python manage.py runserver 0.0.0.0:5000 --verbosity=2
```

---

## 🎤 Pour le pitch (rappel)

La démo live devant le jury :
1. Montrer le boîtier ESP32 physique
2. Appuyer sur la surface → déplacement augmente sur le graphe en direct
3. Dépasser 5mm → bannière rouge clignote + titre onglet change
4. Cliquer "Exporter PDF" → rapport téléchargé avec le ROI calculé

**Durée totale démo : ~2 minutes**

---

*StructurePulse AI · Hackathon Digital Innov'Next 2026 · Équipe Mécatronique + Informatique + Génie Civil*
