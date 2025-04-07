# 📦 Stockify – Application de gestion d'inventaire

**Stockify** est une application web destinée aux **commerçants** souhaitant gérer l'inventaire de leur magasin. Développée dans le cadre d’un **projet scolaire** en Django, elle inclut une logique de rôles pour sécuriser les actions sensibles tout en offrant une vue publique.

---

## 🧠 Technologies utilisées

- **Backend** : Django 5.1.7  
- **Base de données** : SQLite (choisie pour sa simplicité)
- **Frontend** :
  - Bootstrap (interface responsive)
  - Charts.js (graphiques pour les statistiques)

---

## 🔐 Identifiants de test

Super utilisateur avec tous les droits pour tester l'application en local :

- **Email** : `john.doe@example.com`  
- **Mot de passe** : `@12345678Jd`

---

## 🎯 Objectifs de l’application

- Gérer un stock de produits
- Suivre les commandes clients
- Assurer un suivi des ventes (recettes)
- Sécuriser l’accès aux fonctionnalités selon le rôle utilisateur

---

## 🧑‍💼 Utilisateurs & rôles

- Tout utilisateur peut s’inscrire librement.
- Un nouvel utilisateur a le rôle **lecteur** par défaut.
- Seul un **admin** peut promouvoir un utilisateur en **éditeur**.
- **Lecteur** : peut consulter les produits et passer commande.
- **Éditeur** : peut ajouter, modifier, supprimer des produits, et valider les commandes.

---

## 📦 Fonctionnalités principales

### ✅ Produits
- Liste des produits avec tri par nom, stock, prix
- Ajout, modification, suppression (réservé aux éditeurs)
- Export des produits (à venir)

### 🛒 Commandes
- Tout utilisateur peut passer une commande
- Une commande doit être **validée** avant d’être effective
- À la validation :
  - le **stock** est décrémenté automatiquement
  - le **montant total** est ajouté aux **recettes**

### 🔐 Sécurité
- Seuls les utilisateurs connectés peuvent modifier les produits
- Même si l’inscription est publique, la modification du stock est protégée par un **système de rôles**
- Les vues du dashboard sont visibles par tous (lecture seule), mais restreintes en environnement de production

---

## 📊 Fonctionnalités avancées

- 🔍 Tri dynamique des produits
- 📤 Export des données (CSV / Excel - en cours)
- 🧾 Journalisation des actions (création, suppression, modification)
- 📈 Statistiques des ventes via Charts.js
- 🔔 Système de notification (à venir)

---

## 🧱 Structure du projet résumé

```
stockify.boukary.dev/
├── requirements.txt
└── src/
    ├── manage.py
    ├── db.sqlite3
    ├── accounts/       ← Gestion des utilisateurs et rôles
    ├── inventory/      ← Gestion des produits & logs d'activité
    ├── store/          ← Commandes et front store public
    ├── stockify/       ← Configuration globale du projet
    ├── medias/         ← Uploads d'images de produits
    └── templates/      ← Templates globaux (layout, dashboard, etc.)
```

<details>
<summary>🧱 Voir la structure complète du projet</summary>

📂 Le détail de la structure du projet est disponible ici :  
👉 [STRUCTURE.md](./STRUCTURE.md)

</details>


### 📁 Détail des apps

- `accounts/`
  - Signin / Signup
  - Attribution des rôles
  - Modèle utilisateur personnalisé
- `inventory/`
  - Produits
  - Journaux d'activité (`ActivityLog`)
- `store/`
  - Passation de commande
  - Validation & calcul des recettes
- `stockify/`
  - Middleware
  - URLs globales
  - Fichiers de config

---

## 🧪 Features avancées

- **Export CSV/Excel** de l’inventaire et des commandes
- **Filtrage dynamique** des produits par nom / stock
- **Logs d’activité** détaillés (création, modification)
- **Pagination** des vues produits
- **Statistiques visuelles** (recettes, ventes par produit)
- **Notifications mail** à la validation d’une commande  (en cours)

---

## 🛠️ Installation (local)

```bash
# Cloner le projet
git clone https://github.com/BoubakarPI/stockify.boukary.dev.git
cd stockify.boukary.dev/src/

# Créer un environnement virtuel

# Sur Linux (ou macOS) :

  python -m venv venv
  source venv/bin/activate
  

# Sur Windows :

  python -m venv venv
  .\venv\Scripts\activate

# Installer les dépendances
pip install -r ../requirements.txt

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver
```

---

## 🚨 Contraintes pédagogiques respectées

- Seuls les **utilisateurs connectés** peuvent modifier un produit.
- Une logique de **rôle** a été ajoutée pour éviter la corruption des stocks.
- Les utilisateurs peuvent voir le dashboard, mais ne peuvent **agir** qu'avec les bons rôles.
- **Middleware de restriction** prévu pour la production.

---

## 🙌 Contributions

Toute contribution est la bienvenue pour enrichir le projet :
- Ajout des moyens de paiement (Carte, Mobile Money)
- Authentification par email/token
- Ajout de tests unitaires

---

## ✨ Merci

Merci de tester et contribuer à **Stockify** !
