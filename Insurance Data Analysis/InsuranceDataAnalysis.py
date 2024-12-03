import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class InsuranceDataAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_average_charges(self, group_by):
        """
        Calculate average charges grouped by a specified column.
        """
        return self.data.groupby(group_by, observed=False)['charges'].mean()

    def correlation_matrix(self):
        """
        Return the correlation matrix for numerical columns only.
        """
        numerical_data = self.data.select_dtypes(include=['number'])  # Select only numeric columns
        return numerical_data.corr()

    def bmi_category_analysis(self, visualize=False):
        """
        Categorize BMI and calculate average charges for each BMI category.
        If visualize=True, create a barplot.
        """
        self.data['bmi_category'] = self.data['bmi'].apply(self._categorize_bmi)
        avg_charges = self.calculate_average_charges('bmi_category')
        
        if visualize:
            plt.figure(figsize=(8, 6))
            sns.barplot(x=avg_charges.index, y=avg_charges.values, palette='muted')
            plt.title("Average Charges by BMI Category")
            plt.xlabel("BMI Category")
            plt.ylabel("Average Charges")
            plt.show()
        
        return avg_charges

    def age_group_analysis(self, visualize=False):
        """
        Categorize age into groups and calculate average charges for each age group.
        If visualize=True, create a barplot.
        """
        self.data['age_group'] = pd.cut(self.data['age'], bins=[18, 29, 39, 49, 59, 64], 
                                        labels=['18-29', '30-39', '40-49', '50-59', '60-64'])
        avg_charges = self.calculate_average_charges('age_group')
        
        if visualize:
            plt.figure(figsize=(8, 6))
            sns.barplot(x=avg_charges.index, y=avg_charges.values, palette='pastel')
            plt.title("Average Charges by Age Group")
            plt.xlabel("Age Group")
            plt.ylabel("Average Charges")
            plt.show()
        
        return avg_charges

    def smoker_vs_non_smoker(self, visualize=False):
        """
        Compare average charges between smokers and non-smokers.
        If visualize=True, create a barplot.
        """
        avg_charges = self.calculate_average_charges('smoker')
        
        if visualize:
            plt.figure(figsize=(8, 6))
            sns.barplot(x=avg_charges.index, y=avg_charges.values, palette='coolwarm')
            plt.title("Average Charges by Smoking Status")
            plt.xlabel("Smoker")
            plt.ylabel("Average Charges")
            plt.show()
        
        return avg_charges

    def region_analysis(self, visualize=False):
        """
        Analyze average charges by region.
        If visualize=True, create a barplot.
        """
        avg_charges = self.calculate_average_charges('region')
        
        if visualize:
            plt.figure(figsize=(8, 6))
            sns.barplot(x=avg_charges.index, y=avg_charges.values, palette='viridis')
            plt.title("Average Charges by Region")
            plt.xlabel("Region")
            plt.ylabel("Average Charges")
            plt.show()
        
        return avg_charges

    @staticmethod
    def _categorize_bmi(bmi):
        """
        Helper function to categorize BMI into groups.
        """
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Healthy'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


# Example usage
insurance_data = pd.read_csv('insurance.csv')  # Replace with the path to your CSV file
insurance_analysis = InsuranceDataAnalysis(insurance_data)

# Perform specific analyses with visualizations
avg_charges_smoker = insurance_analysis.smoker_vs_non_smoker(visualize=True)
avg_charges_region = insurance_analysis.region_analysis(visualize=True)
bmi_analysis = insurance_analysis.bmi_category_analysis(visualize=True)
age_group_analysis = insurance_analysis.age_group_analysis(visualize=True)

# Display correlation matrix with a heatmap
correlation_matrix = insurance_analysis.correlation_matrix()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
