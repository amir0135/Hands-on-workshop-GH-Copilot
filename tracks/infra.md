# Infrastructure/Operations Hackathon 👩‍💻👨🏾‍💻
Welcome to the Infrastructure/Operations Hackathon. The challenge is to deploy cloud infrastructure using Infrastructure as Code (IaC) with modern development tools: GitHub Repos for code, GitHub Actions for automation, your local development environment, and obtaining assistance from GitHub Copilot.

## Development Environment 💻
**Prerequisites:**
- **[Terraform](https://www.terraform.io/downloads)** (v1.0 or later) - Infrastructure as Code tool for building, changing, and versioning infrastructure
- **[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)** - Command-line tool for managing Azure resources
- **Azure Subscription** - Use your organizational Azure subscription with appropriate permissions (not personal subscriptions)
- **VS Code or your preferred IDE** - Code editor for writing Terraform configurations
- **GitHub Copilot extension** (recommended) - AI pair programmer for faster development
- **Git** - Version control system installed locally

**Recommended VS Code Extensions:**
- HashiCorp Terraform
- Azure Terraform
- GitHub Copilot
- Azure Account
- Azure Resources

## Setup Instructions 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/hosseinzahed/demant-github-hackathon.git
cd demant-github-hackathon
git checkout -b team1  # Replace 'team1' with your team name
```

### 2. Verify Terraform Installation
```bash
terraform version  # Should show 1.0 or later
```

### 3. Verify Azure CLI Installation
```bash
az --version
```

### 4. Login to Azure
```bash
az login
# Select your subscription
az account set --subscription "your-subscription-id"
```

### 5. Configure Azure Credentials for Terraform
For local development, you can use Azure CLI authentication or set up a service principal:

**Option A: Azure CLI (Recommended for local development)**
```bash
# Already authenticated with 'az login'
# Terraform will automatically use these credentials
```

**Option B: Service Principal (For CI/CD)**
```bash
# Create a service principal
az ad sp create-for-rbac --name "terraform-sp" --role Contributor --scopes /subscriptions/{subscription-id}

# Set environment variables
export ARM_CLIENT_ID="your-client-id"
export ARM_CLIENT_SECRET="your-client-secret"
export ARM_TENANT_ID="your-tenant-id"
export ARM_SUBSCRIPTION_ID="your-subscription-id"
```

For more details, visit the [Terraform Azure Provider documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret).

### 6. Create Project Structure
```bash
# Create infrastructure directory
mkdir infrastructure
cd infrastructure

# Create main Terraform files
touch main.tf variables.tf outputs.tf
```

💡**Important:** The resources deployment must happen in an Azure resource group already created for your team and accessible with the configured credentials. The name of the resource group is: `rg-hackathon-team-N` (replace N with your team number).

# Challenge 1: Application Infrastructure ☁️

The infrastructure must be created using Infrastructure as Code (IaC) in Azure with Terraform. Use a storage account for state management and deploy resources in an existing resource group.

## Infrastructure Components 🏛️

### Required Resources:

1. **Resource Group** 🗂️
   - Container for all Azure resources
   - Use the pre-created resource group: `rg-hackathon-team-N`

2. **Storage Account for Terraform State** 💾
   - Create a storage account for team collaboration and state locking
   - Naming convention: `sahacktfstate{team-number}` (e.g., `sahacktfstate1`)
   - Configure remote backend in Terraform
   - Create a container named `tfstate` within the storage account

3. **Azure App Service** 🌐
   - Fully managed platform for hosting web applications
   - App Service Plan (choose appropriate tier)
   - Application Insights for monitoring

4. **Azure SQL Database** 🗄️
   - Fully managed relational database
   - Configure appropriate pricing tier
   - Database for customers, products, and orders

### Optional/Advanced Resources:

5. **Virtual Network & Private Endpoint** 🔒 (Optional)
   - Secure network connectivity
   - Private endpoint for Azure SQL Database
   - VNet integration for App Service
   - The App Service must reach the Azure SQL Database over a private network

6. **Azure Front Door** 🚪 (Optional)
   - Global load balancer and CDN
   - Enhanced security with WAF
   - SSL/TLS termination
   - The application must be exposed for security and delivery purposes

## Implementation Requirements 📋

💡**Configuration Tips:**
- Create a Connection String named `DatabaseConnectionString` in App Service configuration (this will be used by the Application to access the database)
- Use Terraform variables for reusable and environment-specific values
- Tag all resources with team name and environment
- Enable diagnostic logs for all services
- Use outputs to expose important resource information

# Challenge 2: CI/CD 🚀
The infrastructure must be deployed using GitHub Actions.

💡**GitHub Actions Tips:**
- To connect to Azure, credentials are already configured for you as GitHub Actions secrets with these names: `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID`. You can expose them as environment variables for the action.
- A skeleton of the GitHub Action has been created at [.github/workflows/deploy-infrastructure.yml](.github/workflows/deploy-infrastructure.yml). Do not modify the trigger. Complete it with your code and make sure to launch it for your branch.
- Use `terraform plan` artifact for review before apply
- Implement validation steps (`terraform fmt -check`, `terraform validate`)



# GitHub Copilot Assistance 🤖
Given the infrastructure requirements, try to ask GitHub Copilot for help. Here are some sample prompts:

## Project Setup 🚀
- "Generate Terraform file with Azure provider and state on storage account"
- "Create variables.tf with common Azure infrastructure variables"
- "Generate outputs.tf for App Service and SQL Database connection information"

## Resource Group & State Management 🗂️
- "Reference an existing Azure resource group in Terraform"
- "Configure Terraform backend for Azure Storage Account with state locking"
- "Create Terraform configuration for resource group with tags"

## App Service 🌐
- "Generate code for Azure App Service for .NET App"
- "Configure a Log Analytics Workspace Based Application Insights for the App Service"
- "Create Azure App Service with B1 pricing tier"
- "Add Application Insights with Log Analytics Workspace for App Service monitoring"

## Azure SQL Database 🗄️
- "Generate code for Azure SQL Database"
- "Add connection string to Azure SQL as Configuration to the App Service"
- "Create Azure SQL Database with DTU-based pricing tier"
- "Add firewall rules to Azure SQL Server for Azure services"

## Networking (Optional) 🔒
- "Add a virtual network"
- "Connect the App Service to the Azure SQL Database through the virtual network"
- "Add Private DNS Zone for SQL Server to existing VNet"
- "Add record to Private DNS Zone for SQL Server Private Endpoint IP"
- "Generate private endpoint for Azure SQL Database"

## Azure Front Door (Optional) 🚪
- "Add an Azure Front Door that exposes the Azure App Service"
- "Create Azure Front Door with custom domain for App Service"
- "Generate Azure Front Door configuration with WAF policy"

## GitHub Actions 🔄
- "Generate a GitHub Action that deploys the Terraform in Azure"
- "Create GitHub Actions workflow with Terraform validate, plan, and apply steps"
- "Add Azure CLI login to GitHub Actions workflow using service principal"

💡**Tips for Effective Copilot Usage:**
- Be specific about Azure resource types and configurations
- Mention Terraform version and provider versions in your prompts
- Ask for best practices and security recommendations
- Request comments and documentation in generated code
- Use Copilot Chat to explain complex Terraform syntax
- Iterate on prompts to refine the generated infrastructure code


# Challenge 3: Resource Cleanup 🧹

Properly tear down your infrastructure to prevent unnecessary Azure costs and maintain a clean environment.

## Cleanup Steps 💰

### Option 1: Terraform Destroy (Recommended)
```bash
# Navigate to your infrastructure directory
cd infrastructure

# Review what will be destroyed
terraform plan -destroy

# Destroy all resources managed by Terraform
terraform destroy

# Confirm by typing 'yes' when prompted
```

### Option 2: Selective Resource Removal
```bash
# Remove a specific resource
terraform destroy -target=azurerm_app_service.main

# Review and confirm
```

### Option 3: Azure Portal/CLI (Manual)
```bash
# List resources in your resource group
az resource list --resource-group rg-hackathon-team-N --output table

# Delete specific resources
az resource delete --ids <resource-id>
```

### Cleanup Verification ✅
```bash
# Verify resources are deleted
az resource list --resource-group rg-hackathon-team-N --output table

# Check Terraform state
terraform state list
```

💡**Important Notes:**
- Always run `terraform plan -destroy` first to review what will be deleted
- Be careful not to delete the pre-created resource group or state storage account
- Use `terraform state list` to see all managed resources before cleanup
- Keep your Terraform state file safe if you need to recreate resources later
- Consider using resource locks on critical infrastructure to prevent accidental deletion