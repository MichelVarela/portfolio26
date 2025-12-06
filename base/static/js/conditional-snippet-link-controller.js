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
        const pageField = document.querySelector('[data-contentpath="page_link"]');
        const urlField = document.querySelector('[data-contentpath="url"]');
        const mailtoField = document.querySelector('[data-contentpath="mailto"]');
        const phoneField = document.querySelector('[data-contentpath="phone"]');
        const imageField = document.querySelector('[data-contentpath="image"]');
        const documentField = document.querySelector('[data-contentpath="document"]');
        const anchorField = document.querySelector('[data-contentpath="anchor"]');

        // Ocultar todos
        if (pageField) pageField.closest('.w-panel').style.display = 'none';
        if (urlField) urlField.closest('.w-panel').style.display = 'none';
        if (mailtoField) mailtoField.closest('.w-panel').style.display = 'none';
        if (phoneField) phoneField.closest('.w-panel').style.display = 'none';
        if (imageField) imageField.closest('.w-panel').style.display = 'none';
        if (documentField) documentField.closest('.w-panel').style.display = 'none';
        if (anchorField) anchorField.closest('.w-panel').style.display = 'none';

        // Mostrar el correspondiente
        if (linkType === 'internal' && pageField) {
            pageField.closest('.w-panel').style.display = 'block';
        } else if (linkType === 'external' && urlField) {
            urlField.closest('.w-panel').style.display = 'block';
        } else if (linkType === 'mailto' && mailtoField) {
            mailtoField.closest('.w-panel').style.display = 'block';
        } else if (linkType === 'phone' && phoneField) {
            phoneField.closest('.w-panel').style.display = 'block';
        } else if (linkType === 'image' && imageField) {
            imageField.closest('.w-panel').style.display = 'block';
        } else if (linkType === 'document' && documentField) {
            documentField.closest('.w-panel').style.display = 'block';
        } else if (linkType === 'anchor' && anchorField) {
            anchorField.closest('.w-panel').style.display = 'block';
        }
    }
}

window.wagtail.app.register('conditional-snippet-link', ConditionalSnippetLinkController);