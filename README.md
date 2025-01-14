# Guide d'installation et de configuration pour Selenium avec Pytest-BDD

Ce guide vous explique comment configurer un projet Python pour utiliser Selenium, Pytest, Pytest-HTML, Webdriver-Manager et Pytest-BDD. Vous apprendrez également à créer la structure du projet et un fichier de test avec les imports nécessaires.

---

## **Prérequis**

Assurez-vous que Python est installé sur votre système. Vous pouvez vérifier en exécutant :

```bash
python --version
```

Si Python n'est pas installé, téléchargez-le et installez-le depuis le [site officiel de Python](https://www.python.org/downloads/).

---

## **Étape 1 : Installer les dépendances**

Exécutez les commandes suivantes pour installer les bibliothèques nécessaires :

```bash
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager
pip install pytest-bdd
```

---

## **Étape 2 : Créer la structure du projet**

1. Créez un dossier principal pour votre projet, par exemple :

   ```
   SELENIUM-WEBDRIVER-PYTHON-INIT
   ```

2. À l'intérieur de ce dossier, créez une structure comme suit :

   ```
   SELENIUM-WEBDRIVER-PYTHON-INIT/
   ├── tests/
   │   ├── features/
   │   ├── modules/
   │   └── test_montest.py
   ├── README.md
   ```

   - **`tests/`** : Contient tous vos fichiers de tests.
   - **`features/`** : Contient les fichiers `.feature` pour le BDD.
   - **`modules/`** : Contient les modules ou utilitaires nécessaires pour vos tests.
   - **`test_montest.py`** : Fichier de test principal.

3. Créez le fichier `test_montest.py` dans le dossier `tests`.

---

## **Étape 3 : Ajouter les imports dans `test_montest.py`**

Ajoutez le code suivant dans `test_montest.py` :

```python
import pytest
import pytest_bdd
from pytest_bdd import parsers
from selenium import webdriver  # Import the Selenium Webdriver
from selenium.webdriver.common.by import By  # Import the By class
from pytest_bdd import given, when, then, scenario
```

---

## **Étape 4 : Écrire votre premier scénario (optionnel)**

Une fois les imports ajoutés, vous pouvez commencer à écrire vos étapes pour un scénario de test. Par exemple :

```python
@scenario('features/example.feature', 'Example scenario')
def test_example():
    pass

@given("the browser is open")
def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    return driver

@when("the user performs an action")
def perform_action(driver):
    element = driver.find_element(By.ID, "someElementID")
    element.click()

@then("the expected result is observed")
def verify_result(driver):
    assert "Expected Title" in driver.title
    driver.quit()
```

---

## **Étape 5 : Exécuter le test**

1. Placez vos scénarios BDD dans un fichier `.feature` dans le dossier `features`.
2. Exécutez vos tests avec la commande :

   ```bash
   pytest --html=report.html
   ```

---

## **Vérification des installations**

Pour vérifier que toutes les bibliothèques sont correctement installées :

```bash
pip show selenium pytest pytest-html webdriver-manager pytest-bdd
```

Vous êtes maintenant prêt à automatiser vos tests avec Selenium et Pytest-BDD !

Pour plus d'informations, consultez la documentation officielle de chaque bibliothèque :

- [Documentation de Selenium](https://www.selenium.dev/documentation/)
- [Documentation de Pytest](https://docs.pytest.org/)
- [Documentation de Pytest-HTML](https://pytest-html.readthedocs.io/)
- [Documentation de Webdriver-Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Documentation de Pytest-BDD](https://pytest-bdd.readthedocs.io/)

```
