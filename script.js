// Global variables
let scannedFiles = [];
let currentConfig = {};

// Tab management
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => tab.classList.remove('active'));
    
    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => button.classList.remove('active'));
    
    // Show selected tab content
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
}

// Loading management
function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
}

// API calls
async function apiCall(endpoint, method = 'GET', data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        }
    };
    
    if (data) {
        options.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(`/api${endpoint}`, options);
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || 'API call failed');
        }
        
        return result;
    } catch (error) {
        console.error('API Error:', error);
        alert('Error: ' + error.message);
        throw error;
    }
}

// Scan functionality
async function scanDirectory() {
    const directory = document.getElementById('directory-input').value;
    
    if (!directory) {
        alert('Please enter a directory path');
        return;
    }
    
    showLoading();
    
    try {
        const result = await apiCall('/scan', 'POST', { directory: directory });
        scannedFiles = result.files;
        displayScanResults(result);
    } catch (error) {
        console.error('Scan failed:', error);
    } finally {
        hideLoading();
    }
}

function displayScanResults(result) {
    const container = document.getElementById('scan-results');
    
    if (result.files.length === 0) {
        container.innerHTML = '<p>No files found in the specified directory.</p>';
        return;
    }
    
    let html = `
        <div class="stats">
            <div class="stat-card">
                <h3>${result.count}</h3>
                <p>Files Found</p>
            </div>
        </div>
        <h3>Scanned Files:</h3>
    `;
    
    result.files.forEach(file => {
        html += `
            <div class="file-item">
                <h4>${file.name}</h4>
                <p><strong>Path:</strong> ${file.path}</p>
                <p><strong>Size:</strong> ${formatFileSize(file.size)}</p>
                <p><strong>Extension:</strong> ${file.extension}</p>
                <p><strong>Modified:</strong> ${new Date(file.modification_time).toLocaleString()}</p>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Rule management
function addRule() {
    const container = document.getElementById('rules-container');
    const ruleItem = document.createElement('div');
    ruleItem.className = 'rule-item';
    ruleItem.innerHTML = `
        <input type="text" placeholder="Rule name" class="rule-name">
        <select class="rule-field">
            <option value="extension">File Extension</option>
            <option value="path">File Path</option>
            <option value="name">File Name</option>
            <option value="size">File Size</option>
        </select>
        <select class="rule-operator">
            <option value="equals">Equals</option>
            <option value="contains">Contains</option>
        </select>
        <input type="text" placeholder="Value" class="rule-value">
        <select class="rule-action">
            <option value="move">Move to</option>
            <option value="rename">Rename</option>
            <option value="add_tag">Add Tag</option>
            <option value="delete">Delete</option>
        </select>
        <input type="text" placeholder="Action value" class="rule-action-value">
        <button onclick="removeRule(this)" class="btn btn-danger">Remove</button>
    `;
    container.appendChild(ruleItem);
}

function removeRule(button) {
    button.parentElement.remove();
}

function getRulesFromForm() {
    const ruleItems = document.querySelectorAll('.rule-item');
    const rules = [];
    
    ruleItems.forEach((item, index) => {
        const name = item.querySelector('.rule-name').value;
        const field = item.querySelector('.rule-field').value;
        const operator = item.querySelector('.rule-operator').value;
        const value = item.querySelector('.rule-value').value;
        const actionType = item.querySelector('.rule-action').value;
        const actionValue = item.querySelector('.rule-action-value').value;
        
        if (name && field && operator && value && actionType) {
            const rule = {
                rule_id: `rule_${index + 1}`,
                name: name,
                conditions: [
                    {
                        field: field,
                        operator: operator,
                        value: value
                    }
                ],
                actions: [
                    {
                        type: actionType
                    }
                ],
                enabled: true
            };
            
            if (actionValue) {
                if (actionType === 'move') {
                    rule.actions[0].destination = actionValue;
                } else if (actionType === 'rename') {
                    rule.actions[0].new_name = actionValue;
                } else if (actionType === 'add_tag') {
                    rule.actions[0].tag = actionValue;
                }
            }
            
            rules.push(rule);
        }
    });
    
    return rules;
}

// Organization functionality
async function applyRules() {
    if (scannedFiles.length === 0) {
        alert('Please scan files first');
        return;
    }
    
    const rules = getRulesFromForm();
    
    if (rules.length === 0) {
        alert('Please add at least one rule');
        return;
    }
    
    showLoading();
    
    try {
        const result = await apiCall('/organize', 'POST', { 
            files: scannedFiles, 
            rules: rules 
        });
        
        displayOrganizeResults(result.files);
        scannedFiles = result.files; // Update the scanned files with organized results
    } catch (error) {
        console.error('Organization failed:', error);
    } finally {
        hideLoading();
    }
}

function displayOrganizeResults(files) {
    const container = document.getElementById('organize-results');
    
    let html = '<h3>Organization Results:</h3>';
    
    files.forEach(file => {
        html += `
            <div class="file-item">
                <h4>${file.name}</h4>
                <p><strong>Path:</strong> ${file.path}</p>
                <p><strong>Tags:</strong> ${file.tags ? file.tags.join(', ') : 'None'}</p>
                <p><strong>Category:</strong> ${file.category ? file.category.join(', ') : 'None'}</p>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Duplicates functionality
async function findDuplicates() {
    if (scannedFiles.length === 0) {
        alert('Please scan files first');
        return;
    }
    
    showLoading();
    
    try {
        const result = await apiCall('/duplicates', 'POST', { files: scannedFiles });
        displayDuplicatesResults(result.duplicates);
    } catch (error) {
        console.error('Duplicate detection failed:', error);
    } finally {
        hideLoading();
    }
}

function displayDuplicatesResults(duplicates) {
    const container = document.getElementById('duplicates-results');
    
    if (duplicates.length === 0) {
        container.innerHTML = '<p>No duplicate files found.</p>';
        return;
    }
    
    let html = '<h3>Duplicate Files Found:</h3>';
    
    duplicates.forEach((group, index) => {
        html += `
            <div class="duplicate-group">
                <h4>Duplicate Group ${index + 1}</h4>
                <p><strong>Hash:</strong> ${group.hash}</p>
                <p><strong>Files:</strong></p>
                <ul>
        `;
        
        group.files.forEach(file => {
            html += `<li>${file}</li>`;
        });
        
        html += `
                </ul>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Recommendations functionality
async function getRecommendations() {
    if (scannedFiles.length === 0) {
        alert('Please scan files first');
        return;
    }
    
    showLoading();
    
    try {
        const result = await apiCall('/recommendations', 'POST', { 
            files: scannedFiles, 
            rules: currentConfig.default_rules || {} 
        });
        displayRecommendationsResults(result.recommendations);
    } catch (error) {
        console.error('Recommendations failed:', error);
    } finally {
        hideLoading();
    }
}

function displayRecommendationsResults(recommendations) {
    const container = document.getElementById('recommendations-results');
    
    if (recommendations.length === 0) {
        container.innerHTML = '<p>No recommendations available.</p>';
        return;
    }
    
    let html = '<h3>Organization Recommendations:</h3>';
    
    recommendations.forEach(rec => {
        html += `
            <div class="recommendation-item">
                <h4>${rec.type.replace(/_/g, ' ').toUpperCase()}</h4>
                <p>${rec.description}</p>
                ${rec.file ? `<p><strong>File:</strong> ${rec.file}</p>` : ''}
                ${rec.files ? `<p><strong>Files:</strong> ${rec.files.length} files</p>` : ''}
                ${rec.suggested_category ? `<p><strong>Suggested Category:</strong> ${rec.suggested_category}</p>` : ''}
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Configuration functionality
async function loadConfig() {
    try {
        const config = await apiCall('/config', 'GET');
        currentConfig = config;
        
        // Populate form fields
        document.getElementById('work-keywords').value = config.default_rules.work.join(', ');
        document.getElementById('course-keywords').value = config.default_rules.course.join(', ');
        document.getElementById('personal-keywords').value = config.default_rules.personal.join(', ');
        document.getElementById('ski-keywords').value = config.default_rules.ski.join(', ');
        
        alert('Configuration loaded successfully');
    } catch (error) {
        console.error('Failed to load configuration:', error);
    }
}

async function saveConfig() {
    const config = {
        default_rules: {
            work: document.getElementById('work-keywords').value.split(',').map(s => s.trim()),
            course: document.getElementById('course-keywords').value.split(',').map(s => s.trim()),
            personal: document.getElementById('personal-keywords').value.split(',').map(s => s.trim()),
            ski: document.getElementById('ski-keywords').value.split(',').map(s => s.trim())
        },
        scan_settings: {
            include_hidden: false,
            max_depth: 10
        }
    };
    
    try {
        await apiCall('/config', 'POST', config);
        currentConfig = config;
        alert('Configuration saved successfully');
    } catch (error) {
        console.error('Failed to save configuration:', error);
    }
}

// Utility functions
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    loadConfig();
});

