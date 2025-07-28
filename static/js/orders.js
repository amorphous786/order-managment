// Order Management System JavaScript

class OrderManager {
    constructor() {
        this.selectedRows = new Set();
        this.isEditMode = false;
        this.currentEditOrderId = null;
        this.originalRowData = null;
        this.currentPage = window.paginationInfo ? window.paginationInfo.current_page : 1;
        
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // Button event listeners
        document.getElementById('addBtn').addEventListener('click', () => this.showAddModal());
        document.getElementById('editBtn').addEventListener('click', () => this.startEditMode());
        document.getElementById('deleteBtn').addEventListener('click', () => this.showDeleteModal());
        document.getElementById('updateBtn').addEventListener('click', () => this.saveEditMode());
        document.getElementById('cancelBtn').addEventListener('click', () => this.cancelEditMode());
        document.getElementById('saveOrderBtn').addEventListener('click', () => this.saveOrder());
        document.getElementById('confirmDeleteBtn').addEventListener('click', () => this.deleteOrders());

        // Table row click listeners
        document.addEventListener('click', (e) => {
            const row = e.target.closest('tr[data-order-id]');
            if (row && !this.isEditMode) {
                this.handleRowClick(e, row);
            }
        });

        // Pagination event listeners
        document.addEventListener('click', (e) => {
            const pageLink = e.target.closest('.page-link[data-page]');
            if (pageLink && !pageLink.parentElement.classList.contains('disabled')) {
                e.preventDefault();
                const page = pageLink.dataset.page;
                this.loadPage(page);
            }
        });

        // Modal event listeners
        const orderModal = document.getElementById('orderModal');
        orderModal.addEventListener('hidden.bs.modal', () => this.resetModal());

        // Form validation
        document.getElementById('orderForm').addEventListener('input', (e) => this.validateField(e.target));
    }

    // Row Selection Methods
    handleRowClick(e, row) {
        const orderId = row.dataset.orderId;
        
        // Clear previous selections
        document.querySelectorAll('#ordersTable tbody tr').forEach(tr => {
            tr.classList.remove('selected');
        });
        this.selectedRows.clear();
        
        // Select clicked row
        this.selectedRows.add(orderId);
        row.classList.add('selected');
        
        this.updateButtonStates();
    }

    updateButtonStates() {
        const addBtn = document.getElementById('addBtn');
        const editBtn = document.getElementById('editBtn');
        const deleteBtn = document.getElementById('deleteBtn');
        const updateBtn = document.getElementById('updateBtn');
        const cancelBtn = document.getElementById('cancelBtn');

        if (this.isEditMode) {
            addBtn.disabled = true;
            editBtn.disabled = true;
            deleteBtn.disabled = true;
            updateBtn.disabled = false;
            cancelBtn.disabled = false;
        } else {
            addBtn.disabled = false;
            editBtn.disabled = this.selectedRows.size !== 1;
            deleteBtn.disabled = this.selectedRows.size === 0;
            updateBtn.disabled = true;
            cancelBtn.disabled = true;
        }

        // Edit button style
        if (!editBtn.disabled) {
            editBtn.classList.remove('btn-outline-primary');
            editBtn.classList.add('btn-primary');
        } else {
            editBtn.classList.remove('btn-primary');
            editBtn.classList.add('btn-outline-primary');
        }

        // Update and Cancel button styles
        if (!updateBtn.disabled) {
            updateBtn.classList.remove('btn-outline-success');
            updateBtn.classList.add('btn-success');
        } else {
            updateBtn.classList.remove('btn-success');
            updateBtn.classList.add('btn-outline-success');
        }

        if (!cancelBtn.disabled) {
            cancelBtn.classList.remove('btn-outline-secondary');
            cancelBtn.classList.add('btn-secondary');
        } else {
            cancelBtn.classList.remove('btn-secondary');
            cancelBtn.classList.add('btn-outline-secondary');
        }
    }

    // Modal Methods
    showAddModal() {
        document.getElementById('orderModalLabel').textContent = 'Add New Order';
        document.getElementById('orderForm').reset();
        this.clearValidationErrors();
        
        const modal = new bootstrap.Modal(document.getElementById('orderModal'));
        modal.show();
    }

    resetModal() {
        document.getElementById('orderForm').reset();
        this.clearValidationErrors();
    }

    clearValidationErrors() {
        const inputs = document.querySelectorAll('#orderForm .form-control');
        inputs.forEach(input => {
            input.classList.remove('is-invalid', 'is-valid');
        });
    }

    validateField(field) {
        const value = field.value.trim();
        let isValid = true;

        switch (field.name) {
            case 'order_id':
                isValid = value.length > 0;
                break;
            case 'customer_name':
                isValid = value.length > 0;
                break;
            case 'freight':
                isValid = value > 0;
                break;
        }

        field.classList.remove('is-invalid', 'is-valid');
        field.classList.add(isValid ? 'is-valid' : 'is-invalid');
        
        return isValid;
    }

    // CRUD Operations
    async saveOrder() {
        const form = document.getElementById('orderForm');
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        // Validate all fields
        let isValid = true;
        form.querySelectorAll('.form-control').forEach(field => {
            if (!this.validateField(field)) {
                isValid = false;
            }
        });

        if (!isValid) {
            this.showAlert('Please fill in all required fields correctly.', 'danger');
            return;
        }

        try {
            this.setLoadingState(true);
            
            const response = await fetch('/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            
            if (result.success) {
                bootstrap.Modal.getInstance(document.getElementById('orderModal')).hide();
                this.showAlert('Order created successfully!', 'success');
                // Refresh current page to show the new order
                this.loadPage(this.currentPage);
            } else {
                this.showValidationErrors(result.errors);
            }
        } catch (error) {
            this.showAlert('Error creating order. Please try again.', 'danger');
        } finally {
            this.setLoadingState(false);
        }
    }

    startEditMode() {
        if (this.selectedRows.size !== 1) return;
        
        const orderId = Array.from(this.selectedRows)[0];
        const row = document.querySelector(`tr[data-order-id="${orderId}"]`);
        
        this.isEditMode = true;
        this.currentEditOrderId = orderId;
        this.originalRowData = this.getRowData(row);
        
        // Make row editable
        this.makeRowEditable(row);
        
        this.updateButtonStates();
    }

    makeRowEditable(row) {
        const cells = row.querySelectorAll('td');
        
        cells.forEach((cell, index) => {
            const currentValue = cell.textContent.replace('$', '');
            const input = document.createElement('input');
            
            // Set input type based on column index
            if (index === 2) { // Freight field (3rd column)
                input.type = 'number';
                input.step = '0.01';
                input.min = '0';
            } else { // All other fields are text
                input.type = 'text';
            }
            
            input.className = 'form-control form-control-sm';
            input.value = currentValue;
            
            cell.innerHTML = '';
            cell.appendChild(input);
        });
    }

    getRowData(row) {
        return {
            order_id: row.querySelector('.order-id').textContent,
            customer_name: row.querySelector('.customer-name').textContent,
            freight: row.querySelector('.freight').textContent.replace('$', ''),
            ship_name: row.querySelector('.ship-name').textContent,
            ship_country: row.querySelector('.ship-country').textContent
        };
    }

    async saveEditMode() {
        const row = document.querySelector(`tr[data-order-id="${this.currentEditOrderId}"]`);
        const inputs = row.querySelectorAll('input');
        
        // Ensure we have all 5 inputs
        if (inputs.length !== 5) {
            this.showAlert('Error: Invalid number of input fields', 'danger');
            return;
        }
        
        const data = {
            order_id: inputs[0].value,
            customer_name: inputs[1].value,
            freight: inputs[2].value,
            ship_name: inputs[3].value,
            ship_country: inputs[4].value
        };

        try {
            this.setLoadingState(true);
            
            const response = await fetch(`/update/${this.currentEditOrderId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            
            if (result.success) {
                this.exitEditMode();
                // Unselect the row after successful update
                this.clearRowSelection();
                this.showAlert('Order updated successfully!', 'success');
                // Refresh current page to show the updated order
                this.loadPage(this.currentPage);
            } else {
                this.showValidationErrors(result.errors);
            }
        } catch (error) {
            this.showAlert('Error updating order. Please try again.', 'danger');
        } finally {
            this.setLoadingState(false);
        }
    }

    cancelEditMode() {
        const row = document.querySelector(`tr[data-order-id="${this.currentEditOrderId}"]`);
        this.restoreRowData(row, this.originalRowData);
        this.exitEditMode();
    }

    restoreRowData(row, data) {
        row.querySelector('.order-id').textContent = data.order_id;
        row.querySelector('.customer-name').textContent = data.customer_name;
        row.querySelector('.freight').textContent = `$${data.freight}`;
        row.querySelector('.ship-name').textContent = data.ship_name;
        row.querySelector('.ship-country').textContent = data.ship_country;
    }

    updateRowData(row, data) {
        row.querySelector('.order-id').textContent = data.order_id;
        row.querySelector('.customer-name').textContent = data.customer_name;
        row.querySelector('.freight').textContent = `$${data.freight}`;
        row.querySelector('.ship-name').textContent = data.ship_name;
        row.querySelector('.ship-country').textContent = data.ship_country;
    }

    exitEditMode() {
        this.isEditMode = false;
        this.currentEditOrderId = null;
        this.originalRowData = null;
        
        this.updateButtonStates();
    }

    showDeleteModal() {
        const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
        modal.show();
    }

    async deleteOrders() {
        const orderIds = Array.from(this.selectedRows);
        
        try {
            this.setLoadingState(true);
            
            for (const orderId of orderIds) {
                const response = await fetch(`/delete/${orderId}/`, {
                    method: 'DELETE'
                });
                
                const result = await response.json();
                if (!result.success) {
                    this.showAlert(`Error deleting order ${orderId}. Please try again.`, 'danger');
                    return;
                }
            }
            
            this.selectedRows.clear();
            this.updateButtonStates();
            bootstrap.Modal.getInstance(document.getElementById('deleteModal')).hide();
            this.showAlert('Order(s) deleted successfully!', 'success');
            
            // Refresh current page to show updated data
            this.loadPage(this.currentPage);
        } catch (error) {
            this.showAlert('Error deleting order(s). Please try again.', 'danger');
        } finally {
            this.setLoadingState(false);
        }
    }

    addOrderToTable(order) {
        const tbody = document.querySelector('#ordersTable tbody');
        
        // Remove empty state if exists
        const emptyRow = tbody.querySelector('tr td[colspan="5"]');
        if (emptyRow) {
            emptyRow.closest('tr').remove();
        }
        
        const row = document.createElement('tr');
        row.dataset.orderId = order.order_id;
        row.innerHTML = `
            <td class="order-id">${order.order_id}</td>
            <td class="customer-name">${order.customer_name}</td>
            <td class="freight">$${order.freight}</td>
            <td class="ship-name">${order.ship_name}</td>
            <td class="ship-country">${order.ship_country}</td>
        `;
        
        tbody.appendChild(row);
    }

    showEmptyState() {
        const tbody = document.querySelector('#ordersTable tbody');
        tbody.innerHTML = `
            <tr>
                <td colspan="6" class="text-center text-muted">
                    <i class="fas fa-inbox fa-2x mb-2"></i>
                    <br>No orders found. Click "Add" to create your first order.
                </td>
            </tr>
        `;
    }

    showValidationErrors(errors) {
        Object.keys(errors).forEach(fieldName => {
            const field = document.getElementById(fieldName);
            if (field) {
                field.classList.add('is-invalid');
                const errorDiv = document.createElement('div');
                errorDiv.className = 'invalid-feedback';
                errorDiv.textContent = errors[fieldName][0];
                field.parentNode.appendChild(errorDiv);
            }
        });
    }

    showAlert(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(alertDiv);
        
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }

    setLoadingState(loading) {
        const buttons = document.querySelectorAll('.btn');
        buttons.forEach(btn => {
            if (loading) {
                btn.disabled = true;
                if (btn.id === 'saveOrderBtn') {
                    btn.innerHTML = 'Saving...';
                } else if (btn.id === 'updateBtn') {
                    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span>Update';
                } else if (btn.id === 'confirmDeleteBtn') {
                    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span>Delete';
                }
            } else {
                // Only reset text for modal buttons
                if (btn.id === 'saveOrderBtn') {
                    btn.innerHTML = 'Save Order';
                } else if (btn.id === 'updateBtn') {
                    btn.innerHTML = '<i class="fas fa-save"></i> Update';
                } else if (btn.id === 'confirmDeleteBtn') {
                    btn.innerHTML = 'Delete';
                }
                // Always re-enable all action buttons
                if ([
                    'addBtn', 'editBtn', 'deleteBtn', 'updateBtn', 'cancelBtn',
                    'saveOrderBtn', 'confirmDeleteBtn'
                ].includes(btn.id)) {
                    btn.disabled = false;
                }
            }
        });
        // After loading, update button states for correct enable/disable
        this.updateButtonStates();
    }

    clearRowSelection() {
        // Clear all row selections
        document.querySelectorAll('#ordersTable tbody tr').forEach(tr => {
            tr.classList.remove('selected');
        });
        this.selectedRows.clear();
        this.updateButtonStates();
    }

    // Pagination Methods
    async loadPage(page) {
        try {
            this.setLoadingState(true);
            
            const response = await fetch(`/api/orders/?page=${page}`);
            const data = await response.json();
            
            if (data.success) {
                this.currentPage = parseInt(page);
                this.updateTableWithOrders(data.orders);
                this.updatePaginationControls(data.pagination);
                this.clearRowSelection();
            } else {
                this.showAlert('Error loading orders. Please try again.', 'danger');
            }
        } catch (error) {
            this.showAlert('Error loading orders. Please try again.', 'danger');
        } finally {
            this.setLoadingState(false);
        }
    }

    updateTableWithOrders(orders) {
        const tbody = document.querySelector('#ordersTable tbody');
        
        if (orders.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center text-muted">
                        No orders found. Click "Add" to create your first order.
                    </td>
                </tr>
            `;
            return;
        }
        
        tbody.innerHTML = orders.map(order => `
            <tr data-order-id="${order.order_id}">
                <td class="order-id">${order.order_id}</td>
                <td class="customer-name">${order.customer_name}</td>
                <td class="freight">$${order.freight}</td>
                <td class="ship-name">${order.ship_name}</td>
                <td class="ship-country">${order.ship_country}</td>
            </tr>
        `).join('');
    }

    updatePaginationControls(pagination) {
        const paginationContainer = document.querySelector('.pagination-container');
        if (!paginationContainer) return;
        
        const nav = paginationContainer.querySelector('nav');
        const info = paginationContainer.querySelector('.text-muted');
        
        // Update navigation
        nav.innerHTML = this.generatePaginationHTML(pagination);
        
        // Update info text
        if (info) {
            info.textContent = `Showing ${pagination.current_page * 10 - 9} to ${Math.min(pagination.current_page * 10, pagination.total_orders)} of ${pagination.total_orders} orders`;
        }
    }

    generatePaginationHTML(pagination) {
        let html = '<ul class="pagination justify-content-center">';
        
        // Previous button
        if (pagination.has_previous) {
            html += `
                <li class="page-item">
                    <a class="page-link" href="#" data-page="${pagination.previous_page_number}">
                        <i class="fas fa-chevron-left"></i> Previous
                    </a>
                </li>
            `;
        } else {
            html += `
                <li class="page-item disabled">
                    <span class="page-link"><i class="fas fa-chevron-left"></i> Previous</span>
                </li>
            `;
        }
        
        // Page numbers
        for (let i = 1; i <= pagination.total_pages; i++) {
            if (i === pagination.current_page) {
                html += `<li class="page-item active"><span class="page-link">${i}</span></li>`;
            } else {
                html += `<li class="page-item"><a class="page-link" href="#" data-page="${i}">${i}</a></li>`;
            }
        }
        
        // Next button
        if (pagination.has_next) {
            html += `
                <li class="page-item">
                    <a class="page-link" href="#" data-page="${pagination.next_page_number}">
                        Next <i class="fas fa-chevron-right"></i>
                    </a>
                </li>
            `;
        } else {
            html += `
                <li class="page-item disabled">
                    <span class="page-link">Next <i class="fas fa-chevron-right"></i></span>
                </li>
            `;
        }
        
        html += '</ul>';
        return html;
    }
}

// Initialize the order manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new OrderManager();
}); 