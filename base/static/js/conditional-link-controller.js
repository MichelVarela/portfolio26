class ConditionalLinkController extends window.StimulusModule.Controller {
    connect() {
        this.setupEventListeners();
        this.toggleAllBlocks();
    }

    setupEventListeners() {
        // Buscar todos los selects de link_type
        const linkTypeSelects = document.querySelectorAll(
            '.link-block [data-contentpath="link_type"] select'
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
            '.link-block [data-contentpath="link_type"] select'
        );
        
        linkTypeSelects.forEach(select => {
            this.toggleFieldsForBlock(select);
        });
    }

    toggleFieldsForBlock(selectElement) {
        const structBlock = selectElement.closest('.struct-block');
        if (!structBlock) return;

        const linkType = selectElement.value;
        
        // Encontrar los campos
        const pageField = structBlock.querySelector('[data-contentpath="page_link"]');
        const urlField = structBlock.querySelector('[data-contentpath="url"]');
        const mailtoField = structBlock.querySelector('[data-contentpath="mailto"]');
        const phoneField = structBlock.querySelector('[data-contentpath="phone"]');
        const imageField = structBlock.querySelector('[data-contentpath="image"]');
        const documentField = structBlock.querySelector('[data-contentpath="document"]');
        const anchorField = structBlock.querySelector('[data-contentpath="anchor"]');

        // Ocultar todos
        if (pageField) pageField.style.display = 'none';
        if (urlField) urlField.style.display = 'none';
        if (mailtoField) mailtoField.style.display = 'none';
        if (phoneField) phoneField.style.display = 'none';
        if (imageField) imageField.style.display = 'none';
        if (documentField) documentField.style.display = 'none';
        if (anchorField) anchorField.style.display = 'none';

        // Mostrar el correspondiente
        if (linkType === 'internal' && pageField) {
            pageField.style.display = 'block';
        } else if (linkType === 'external' && urlField) {
            urlField.style.display = 'block';
        } else if (linkType === 'mailto' && mailtoField) {
            mailtoField.style.display = 'block';
        } else if (linkType === 'phone' && phoneField) {
            phoneField.style.display = 'block';
        } else if (linkType === 'image' && imageField) {
            imageField.style.display = 'block';
        } else if (linkType === 'document' && documentField) {
            documentField.style.display = 'block';
        } else if (linkType === 'anchor' && anchorField) {
            anchorField.style.display = 'block';
        }
    }
}

window.wagtail.app.register('conditional-link', ConditionalLinkController);