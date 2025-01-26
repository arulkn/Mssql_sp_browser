// Highlight the selected procedure
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.procedure-link').forEach(link => {
        link.addEventListener('click', function() {
            // Remove the 'active' class from all procedure links
            document.querySelectorAll('.procedure-link').forEach(l => l.classList.remove('active'));
            // Add the 'active' class to the clicked procedure link
            this.classList.add('active');
        });
    });
});

function loadProcedure(fullName) {
    const codeDisplay = document.getElementById('code-display');
    codeDisplay.classList.add('loading');

    fetch(`/get_procedure/${encodeURIComponent(fullName)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                codeDisplay.innerHTML = `<div class="error">${data.error}</div>`;
            } else {
                codeDisplay.innerHTML = data.definition;
                highlightWordInClass('from', 'source');
                highlightWordInClass('select', 'source');
            }
        })
        .finally(() => {
            codeDisplay.classList.remove('loading');
        });
        
}

function filterProcedures(char) {
    const procedures = document.querySelectorAll('.procedure-link');
    procedures.forEach(procedure => {
        // Get the displayed procedure name (without usp_)
        const displayedName = procedure.textContent.trim();
        
        // Extract the base name for filtering (remove schema and convert to uppercase)
        const baseName = displayedName
            .split('.')[1] // Remove schema name (e.g., 'dbo')
            .toUpperCase(); // Convert to uppercase for case-insensitive comparison

        console.log(`Displayed Name: ${displayedName}, Base Name: ${baseName}, Filter: ${char}`); // Debugging output

        // Apply the filter
        if (char === 'ALL' || baseName.startsWith(char.toUpperCase())) {
            procedure.style.display = 'block';
        } else {
            procedure.style.display = 'none';
        }
    });
}
function formatSQL() {
    highlightWordInClass('from', 'source');
}


function toggleAuth() {
    const useWindowsAuth = document.getElementById('trusted_connection').checked;
    document.getElementById('credentials').style.display = useWindowsAuth ? 'none' : 'block';
}

function testConnection() {
    const formData = new FormData(document.getElementById('configForm'));
    fetch('/test_connection', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.success) {
            window.location.reload();
        }
    });
}
function highlightWord(word) {
    const body = document.body;
    const regex = new RegExp(`\\b${word}\\b`, 'gi'); // Match whole word, case-insensitive
    const highlightClass = 'highlight';

    // Recursive function to replace text with highlighted spans
    function recursiveHighlight(node) {
        if (node.nodeType === 3) { // Text node
            const match = regex.exec(node.nodeValue);
            if (match) {
                const span = document.createElement('span');
                span.className = highlightClass;
                span.textContent = match[0];

                const after = node.splitText(match.index);
                after.nodeValue = after.nodeValue.substring(match[0].length);

                node.parentNode.insertBefore(span, after);
                recursiveHighlight(after);
            }
        } else if (node.nodeType === 1 && node.childNodes) { // Element node
            Array.from(node.childNodes).forEach(recursiveHighlight);
        }
    }                                           

    recursiveHighlight(body);
}
function markAsComplete() {
    // Find the currently selected procedure link
    const procedureLink = document.querySelector('.procedure-link.active');

    // If no procedure is selected, show an alert and stop execution
    if (!procedureLink) {
        alert('Please select a procedure from the sidebar first.');
        return;
    }

    // Get the full name of the selected procedure
    const fullName = procedureLink.getAttribute('data-full-name');

    // Send a POST request to mark the procedure as complete
    fetch('/mark_complete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ procedure_name: fullName }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            //alert('Procedure marked as complete.');
            procedureLink.remove(); // Remove the procedure from the sidebar
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        alert('Error: ' + error.message);
    });
}
highlightWordInClass('from')