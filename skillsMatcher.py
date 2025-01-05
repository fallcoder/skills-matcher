def display_skills(title, skills_set):
    if skills_set:
        print(f"\n{title}")
        for skill in sorted(skills_set):
            print(f"- {skill}")
    else:
        print(f"\nNone {title.lower()}")

user_skills_input = input("enter your skills (separated by commas) : ")
job_skills_input = input("enter the skills required for the job (separated by commas) : ")

skills = set(user_skills_input.split(','))
job_skills = set(job_skills_input.split(','))

common_skills = skills & job_skills
extra_skills = skills - job_skills
missing_skills = job_skills - skills

#display skills
display_skills("commons skills", common_skills)
display_skills("additional skills you have", extra_skills)
display_skills("missing skills for the job", missing_skills)

user_levels = {}
for skill in skills:
    level = input(f"what is your level for {skill}? (beginner, intermediate, advanced) : ")
    user_levels[skill] = level

if user_levels:
    print("\nyour skill levels :")
    for skill, level in user_levels.items():
        print(f"{skill}: {level}")