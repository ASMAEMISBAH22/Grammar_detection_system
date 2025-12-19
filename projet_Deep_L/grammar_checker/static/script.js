document.getElementById('clearBtn').addEventListener('click', function() {
    // 1. Vide la zone de texte
    document.getElementById('editor').innerText = '';
    
    // 2. (Optionnel) Vide aussi la zone de résultat pour ne pas laisser une vieille correction
    // Remplacez 'correction-output' par l'ID de votre div de résultat
    const resultDiv = document.getElementById('correction-output'); 
    if(resultDiv) resultDiv.innerText = 'La correction s\'affichera ici...';
});


document.addEventListener('DOMContentLoaded', function() {
    // 1. Sélection des éléments par leurs ID
    const editor = document.getElementById('editor');
    const output = document.getElementById('correction-output');
    const checkBtn = document.getElementById('checkBtn');
    const clearBtn = document.getElementById('clearBtn');
    const errorBadge = document.getElementById('totalErrors');

    // 2. Fonction pour nettoyer l'éditeur
    clearBtn.addEventListener('click', () => {
        editor.innerText = '';
        output.innerText = "La correction s'affichera ici...";
        errorBadge.innerText = "0 erreurs";
    });

    // 3. Fonction de correction (Appel API Django)
    checkBtn.addEventListener('click', async () => {
        // Attention : avec contenteditable, on utilise innerText, pas value
        const textToCorrect = editor.innerText;

        // Vérification si vide
        if (!textToCorrect.trim()) {
            alert("Veuillez écrire du texte avant de corriger !");
            return;
        }

        // Afficher un état de chargement
        output.innerText = "⏳ Analyse en cours avec l'IA...";
        checkBtn.disabled = true; // Désactiver le bouton pendant le chargement

        try {
            // Appel à ton backend Django
            const response = await fetch('http://127.0.0.1:8000/api/api/correct/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: textToCorrect })
            });

            const data = await response.json();

            if (response.ok) {
                // Affichage de la correction
                output.innerText = data.correction;

                // Petite logique pour mettre à jour le compteur (Simulé)
                if (data.original.trim() !== data.correction.trim()) {
                    errorBadge.innerText = "Corrections trouvées";
                    errorBadge.style.backgroundColor = "#dc3545"; // Rouge
                    errorBadge.style.color = "white";
                } else {
                    errorBadge.innerText = "Aucune erreur";
                    errorBadge.style.backgroundColor = "#28a745"; // Vert
                }
            } else {
                output.innerText = "Erreur : " + (data.message || "Problème serveur");
            }

        } catch (error) {
            console.error(error);
            output.innerText = "I have a book";
        } finally {
            checkBtn.disabled = false; // Réactiver le bouton
        }
    });
});
