"""Day 10: pandas mini project with merge and join."""

import pandas as pd
import numpy as np

job_listings_df = pd.DataFrame({
    "Job_ID":[1001, 1001, 1002, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1016, 1017],
    "Title": [
        "Data Analyst",
        "Data Analyst",
        "Python Developer",
        "UI Designer",
        "Project Manager",
        "SQL Engineer",
        "Marketing Analyst",
        "DevOps Engineer",
        "HR Specialist",
        "Product Manager",
        "Mobile Developer",
        "Business Analyst",
        "QA Engineer",
        "Content Writer",
        "Data Engineer",
        "Support Specialist",
    ],
    "Skills": [
        ["Python", "SQL"],
        ["Python", "SQL"],
        ["Python", "Flask"],
        ["Figma", "UI"],
        ["Planning", "Leadership"],
        ["SQL", "ETL"],
        ["Excel", "Analytics"],
        ["Linux", "Cloud"],
        ["Recruitment", "HR"],
        ["Strategy", "Roadmap"],
        ["Flutter", "Mobile"],
        ["Excel", "Reporting"],
        ["Testing", "Automation"],
        ["Writing", "SEO"],
        ["Python", "Spark"],
        ["Troubleshooting", "Communication"],
    ],
    "Budget": [9000, 9000, 12000, np.nan, 15000, 11000, 8000, 13000, np.nan, 14000, 10000, 8500, 7500, 5000, 12500, np.nan],
    "Budget_Type": [
        "fixed", "fixed", "hourly", "fixed", "hourly", "fixed",
        "hourly", "fixed", "hourly", "fixed", "hourly",
        "fixed", "hourly", "fixed", "hourly", "fixed"
    ],
    "Category": [
        "Data", "Data", "Software", "Design", "Operations",
        "Data", "Marketing", "Infrastructure", "HR",
        "Product", "Software", "Business", "Quality",
        "Content", "Data", "Support"
    ],
    "Experience_Level": [
        "Mid", "Mid", "Senior", "Junior", "Mid",
        "Mid", "Junior", "Senior", "Junior",
        "Mid", "Mid", "Mid", "Junior",
        "Junior", "Senior", "Junior"
    ],
})

applications_df = pd.DataFrame({
    "Job_ID": [1001, 1002, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1016, 1017],
    "Matched_Skill": [
        "Python", "Flask", "UI", "Leadership", "SQL",
        "Cloud", "HR", "Roadmap", "Mobile", "Reporting",
        "Automation", "SEO", "Spark", "Data", "Support"
    ],
    "Date_Applied": [
        "2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09",
        "2024-01-10", "2024-01-11", "2024-01-12", "2024-01-13", "2024-01-14",
        "2024-01-15", "2024-01-16", "2024-01-17", "2024-01-18", "2024-01-19"
    ],
    "Status": [
        "Applied", "Interviewing", "Applied", "Rejected", "Applied",
        "Interviewing", "Applied", "Applied", "Interviewing", "Applied",
        "Rejected", "Applied", "Interviewing", "Applied", "Rejected"
    ],
})

job_listings_df = job_listings_df.drop_duplicates(subset=["Job_ID"])

job_listings_df["Title"] = job_listings_df["Title"].str.lower().str.strip()
job_listings_df["Category"] = job_listings_df["Category"].str.lower().str.strip()
count_grid = job_listings_df.pivot_table(index="Category", columns="Experience_Level", values="Job_ID", aggfunc="count" ,fill_value=0)

merged_df = pd.merge(job_listings_df, applications_df, on="Job_ID", how="left")

grouped_by_budget = job_listings_df.groupby("Category")["Budget"].mean()

grouped_by_experience = job_listings_df.groupby("Experience_Level")["Budget"].mean()

budget_rank = grouped_by_budget.rank()
exploded_df = job_listings_df.explode("Skills")
skill_counts = exploded_df["Skills"].value_counts()
top_category = grouped_by_budget.idxmax()
top_value = grouped_by_budget.max()
print(f"Highest average budget: {top_category} (${top_value:.2f})")
print(grouped_by_budget.sort_values(ascending=False))
print("Listing count by Category and Experience Level:")
print(count_grid)
status_breakdown = applications_df["Status"].value_counts()
print("Application status breakdown:")
print(status_breakdown)
print("Top 5 most in-demand skills:")
print(skill_counts.head(5))
print("Category rank by average budget (1 = lowest):")
print(budget_rank.sort_values(ascending=False))
print("Average budget of listings you actually applied to vs all listings")
print(merged_df)
