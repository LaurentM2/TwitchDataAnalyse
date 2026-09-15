# Pipeline Data End-to-End : Analyse des Tendances d'Audience Twitch

## 📌 Présentation du Projet
Ce projet a pour objectif d'automatiser la collecte, le traitement et la visualisation des données d'audience de la plateforme Twitch. En partant d'une donnée brute accessible via l'API officielle, j'ai construit un pipeline complet permettant de nettoyer les volumes de données en Python pour ensuite modéliser un tableau de bord interactif d'aide à la décision sur Power BI.

---

## 🛠️ Architecture du Pipeline & Technologies

Le projet s'articule autour de trois grandes étapes techniques :

1. Collecte (Ingestion) : Utilisation d'un script **Python** pour requêter l'API Twitch (via des requêtes HTTP authentifiées) afin de récupérer les métriques en temps réel (viewers, jeux les plus streamés, chaînes actives).
2. Traitement & Nettoyage (ETL) : Utilisation de la librairie Pandas en Python pour :
   * Structurer et fusionner les données brutes.
   * Nettoyer les valeurs manquantes ou aberrantes.
   * Exporter les données prêtes à l'analyse au format **CSV**.
3. Visualisation (Business Intelligence) : Modélisation et conception d'un dashboard interactif sur Power BI (thème Dark adapté à l'univers du gaming) mettant en avant les indicateurs clés de performance (KPIs) et les tendances temporelles des jeux sélectionnés.

---

## 📁 Structure des Fichiers dans ce Repository

* 📄 `twitch-analyse.py` : Le script Python contenant la pour récupérer la data depuis Twitch via les API.
* 📄 `analyse_cleaning_twitch.py` : Le script Python la logique pour nettoyer les données collecté via le script précèdent.
* 📊 `powerbi twitch.pbix` : Le fichier source Power BI contenant le modèle de données et les rapports visuels.
* 💾 `twitch_dataset_clean.csv` : Un échantillon des données nettoyées et prêtes à l'emploi.

---

## 💡 Compétences Validées dans ce Projet
* Traitement de données avec Python & Pandas
* Connexion et authentification aux API Rest
* Modélisation de données et création de mesures implicites sur Power BI
* Visualisation de données et Design d'interface utilisateur (UI/UX)
* Résolution de problèmes et autonomie technique
