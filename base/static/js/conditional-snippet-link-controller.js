console.log("ConditionalSnippetLinkController")

class ConditionalSnippetLinkController extends window.StimulusModule.Controller {
    connect() {
        this.setupEventListeners();
        this.toggleAllBlocks();
    }

    setupEventListeners() {
        // Buscar todos los selects de link_type
        const linkTypeSelects = document.querySelectorAll(
            '[data-contentpath="link_type"] select'
        );
        
        linkTypeSelects.forEach(select => {
            select.addEventListener('change', (e) => {
                this.toggleFieldsForBlock(e.target);
            });
            
            // Toggle inicial
            this.toggleFieldsForBlock(select);
        });
    }

    toggleAllBlocks() {
        const linkTypeSelects = document.querySelectorAll(
            '[data-contentpath="link_type"] select'
        );
        
        linkTypeSelects.forEach(select => {
            this.toggleFieldsForBlock(select);
        });
    }

    toggleFieldsForBlock(selectElement) {
        const section = selectElement.closest('.w-panel');
        if (!section) return;

        const linkType = selectElement.value;
        
        // Encontrar los campos
        const pageField = document.querySelector('[data-contentpath="page_link"]').closest('.w-panel');
        const urlField = document.querySelector('[data-contentpath="url"]').closest('.w-panel');
        const mailtoField = document.querySelector('[data-contentpath="mailto"]').closest('.w-panel');

        // Ocultar todos
        if (pageField) pageField.style.display = 'none';
        if (urlField) urlField.style.display = 'none';
        if (mailtoField) mailtoField.style.display = 'none';

        // Mostrar el correspondiente
        if (linkType === 'internal' && pageField) {
            pageField.style.display = 'block';
        } else if (linkType === 'external' && urlField) {
            urlField.style.display = 'block';
        } else if (linkType === 'mailto' && mailtoField) {
            mailtoField.style.display = 'block';
        }
    }
}

window.wagtail.app.register('conditional-snippet-link', ConditionalSnippetLinkController);