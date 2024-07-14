
# EVA-Lern-Tool

## Beschreibung

Das EVA-Lern-Tool ist eine Quiz-Anwendung, mit der du dich auf EVA vorbereiten kannst. Fragenkataloge können erstellt und erweitert werden. Die Anwendung ist in Python mit PyQt5 geschrieben.

Diese Version enthält den Fragenkatalog 2024 mit 61 Fragen aus allen Studydrive-Dokumenten. Es wird kein Anspruch auf Richtigkeit und Vollständigkeit erhoben. Das Tool könnte buggy sein. Es wurde in kurzer Zeit entwickelt und ist weder vollständig noch qualitativ hochwertig gebaut.

## Installation

### Voraussetzungen

- Python 3.6 oder höher

### Setup

1. **Repository klonen**

   ```bash
   git clone https://git.fsinf.informatik.uni-leipzig.de/material/entwicklung-verteilter-anwendungen.git
   cd entwicklung-verteilter-anwendungen/SoSe24/lerntool_mit_fragen
   ```

2. **Virtuelle Umgebung einrichten und aktivieren**

   - **Für Linux und macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Für Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Abhängigkeiten installieren**

   ```bash
   pip install -r requirements.txt
   ```

## Nutzung

### Anwendung starten

Um die Anwendung zu starten, einfach folgendes im Terminal eingeben:

```bash
python3 main.py
```

### Funktionen

#### Projektübersicht

- **Neuen Fragenkatalog erstellen**: Klicke auf "Neuer Fragenkatalog" und gib einen Namen ein.
- **Fragenkatalog importieren**: Klicke auf "Fragenkatalog importieren" und wähle eine JSON-Datei aus.
- **Fragenkataloge laden**: Bereits vorhandene Fragenkataloge werden automatisch geladen und in der Liste angezeigt.
- **Kontextmenü**: Rechtsklick auf einen Fragenkatalog öffnet ein Kontextmenü mit folgenden Optionen:
  - **Fragen verwalten**: Öffnet den Fragenmanager für den ausgewählten Katalog.
  - **Umbenennen**: Erlaubt das Umbenennen des ausgewählten Katalogs.
  - **Zusammenfügen**: Ermöglicht das Zusammenfügen von zwei Katalogen.
  - **Löschen**: Löscht den ausgewählten Katalog.

#### Fragenmanager öffnen

Um den Fragenmanager zu öffnen, klicke mit der rechten Maustaste auf einen bestehenden Fragenkatalog und wähle "Fragen verwalten" aus dem Kontextmenü.

#### Fragenmanager

- **Fragen hinzufügen**: Im Fragenmanager auf das Pluszeichen klicken und die Frage eingeben.
- **Fragen bearbeiten**: Frage in der Liste auswählen und die Details bearbeiten.
- **Fragen löschen**: Rechtsklick auf eine Frage und "Löschen" auswählen.
- **Fragen speichern**: Änderungen werden automatisch gespeichert, wenn du den Fragenmanager schließt oder zu einer anderen Frage wechselst.

#### Quizmodus

- **Quiz starten**: Doppelklicke auf einen Fragenkatalog in der Liste, um das Quiz zu starten.
- **Fragen beantworten**: Klicke auf eine der Antwortmöglichkeiten, um zu sehen, ob sie richtig oder falsch ist.
- **Fortschritt anzeigen**: Der aktuelle Fortschritt und die korrekte Antwortquote werden unten im Quizfenster angezeigt.

### Design

- **Thema wechseln**: Klicke auf das Symbol mit Sonne/Mond, um zwischen Licht- und Dunkelmodus zu wechseln.

## Bekannte Probleme

- Beim Importieren von JSON-Dateien darauf achten, dass sie das richtige Format haben (eine Liste von Fragen mit den erforderlichen Feldern).
- Fehlermeldungen beim Laden/Speichern von Dateien werden als Pop-ups angezeigt.

## Kontakt

Entwickler: Der Pfiff  
Email: xilefma@web.de  

Viel Spaß beim Lernen mit dem EVA-Lern-Tool! 🚀
