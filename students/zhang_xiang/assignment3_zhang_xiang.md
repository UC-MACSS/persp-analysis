## Does College Reputation Matters for Labor Market Outcome

#### Perspective in Computational Analysis, Assignment 3
#### Name: Xiang Zhang
#### October 29th, 2017

### Introduction
Differences in educational attainment are an initial and stable source of inequality: empirical evidence suggest that the employment rate of students from different colleges differs a lot (Katz and Murphy, 1992). On the one hand, different colleges provide their students with a different set of skills, which could result in different skill levels. On the other hand, the labor market may use the identity of their college as a signal of students’ ability, through which college reputation could affect students’ job application. Conceptually, employers might be sensitive to college reputation, and this sensitivity can be reduced when better information becomes available. Thus, in order to reduce inequality between students from different colleges, it is important to study how, and to what extent that college reputation could affect students' job application success rate.

While this question is extremely important, evidence is scant on how college reputation can influence job application success rate. On top of it, when analyzing what drives differences in job application success rate, it is hard to disentangle college reputation effects from students’ skill levels effects. In this research proposal, I propose an online experiment design which uses digital-enhanced technology to better justify whether college reputation matters for students’ job application outcome.

### Experiment Plan
In this experiment, I would generate and send thousands of fake resumes to the opening jobs listed on LinkedIn automatically. The content of all resumes in response to certain job will be identical except for the educational background part (indicating which university/ college you attend). By comparing the callback rate of different experiment groups (colleges with different reputation), I could detect whether college reputation matters. In this section, I will introduce my experiment procedure, the outcome of my experiment, and discuss the computational-enhanced nature of my experiment design.

#### Experiment Procedures
The first step of the experimental design is to select colleges/ universities to be included in the resumes sent to employers. To ensure that the college/ universities selected differ in their reputation, I would rely on USNEWS Best Colleges Ranking. From the list, I would select fifteen different colleges/ universities. The colleges/ universities chosen are colleges/ universities ranked the 1st to 5th, 51th to 55th, and 151th to 155th in the National University Ranking. The "excellent reputation colleges" are composed of the first group of colleges (ranked 1st to 5th), the "good reputation colleges" are composed of the second group of colleges (ranked 51th to 55th), and the "colleges with fair reputation" consists of the last five colleges selected (ranked 151 to 155). The reason I choose five universities for each reputation group comes from the concern that different individuals may have different opinions on whether a university if good. By having five universities in each group, I can somehow attenuate such concern.

After the selection of colleges/ universities, the second step is to select target job advertisements and prepare resume for the jobs. The primary source of job advertisements is LinkedIn. On LinkedIn website, they will list millions of jobs available. Each post will have a label indicating the fields of employment (for example, consulting, banking, computer engineering). In my experiment, I plan to target for 100 different fields, and send my fake resumes in response to 100 different job advertisements from each of 100 different fields. In my experiment, I would prepare one version of the same resumes for each field.

When responding to the job advertisements, I would adopt a “paired CV” strategy. That is, for each job posted, I would send exactly three identical resumes to it. For each job I respond, the only difference between the resumes is the colleges/ universities name. For resumes send to each job advertisement, I will randomly select one university from each of the three "reputation group" (namely, select one college from "excellent reputation group", one from "good reputation", one from "fair reputation"). One thing to note here is, I will send the resumes in different days to minimize the likelihood that the employer would notice that the resumes are identical. After responding to the job advertisement, I will record the callback of the application.

#### Outcome
The outcome in my experiment is the callback rate. When the employer calls back, I regard the application as a success. By computing the callback rate (defined as the number of callbacks divided by the total number of job applications within each group) for universities from different "reputation group", I could determine whether school reputation matters in job application process.

#### Computationally-enhanced Nature of the Experiment
The experiment design relies heavily on computational techniques. The computationally-enhanced nature of the experiment can be shown in finding job advertisements and treatment delivering process. First of all, by using web scraping techniques, I could get a large number of job advertisements automatically from LinkedIn. Secondly, I could generate fake resume by simply running python code, which also saves a lot of time. Also, when respond to the job advertisement, I could send email to the "job application email" and record feedback automatically. Thus, my experiment process is somehow fully digitalized.

### Assessment of the Experimental Design
In this section, I will assess my experiment design from three different perspectives: whether the design is valid, whether I can use the experiment to analyze heterogeneity in treatment effects, and whether I can detect the mechanism through which it works.

#### Validity
Following the framework offered in Bit-by-bit, there are four main types of validity: statistical conclusion validity, internal validity, construct validity, and external validity. I will discuss these four validities in detail.

Firstly, my experiment design is valid from statistical perspective. In my experiment, the outcome is whether the employer callback to the "fake" job candidates. When the employer calls back, I regard the application as a success. For each reputation group, I can compute the callback rate (defined as the number of callback divided by the total number of job candidates). By detecting whether the callback rates of different reputation groups differ significantly, I can see whether the college reputation matters to application success rate. When measuring the outcomes, I'm actually using a valid and standard statistics method, which makes my experiment valid from statistical perspective.

Secondly, the experiment design is internally valid. The digital-enhanced technologies guarantee that my experiment could proceed smoothly. However, the employers might find that the resumes they receive are effectively identical and thus choose not to respond to all of them, which might reduce the internal validity of my experiment design. To assure the internal validity, I will respond to the same job advertisement in different days, thus, I can minimize the likelihood that the employer would notice the resumes are identical.

Thirdly, my experiment is valid from construct validity perspective. The research question I want to ask here is whether college reputation can increase the success chance of a job application. The outcome I want to measure is just the same as the outcome of the research question, so here, the experiment design is construct valid.

Last but not least, my results of my experiment can be generalized to broader situations due to the use of digital-enhanced technologies. In traditional experiment design, due to the lack of digital-enhanced technologies, they will yield a relatively small sample size. Using this small sample, they can only get their estimation lacking external validity. However, taking advantages of web scraping technologies, I can send the fake resumes to a broad range of jobs, which makes the estimation valid in a very broad setting.

#### Heterogeneity of treatment effects
Conceptually, I can use my experiment design to detect the heterogeneity of treatment effects in different industry and jobs with different seniority level.

In my experiment design, the target job advertisements are from different industries and having different seniority levels requirement (junior, senior, etc.). Thus, I could estimate the effects of college reputation on application successful rate by industry and by job requirement. After getting the data, I could compute the callback rate using the subsample from a certain industry or from certain seniority level requirement. Then I can sufficiently estimate in which industry the college reputation matters more, or at which seniority level the college reputation matters more. In this way, I can take advantage of my experiment design to analyze heterogeneity in treatment effects.

#### Mechanisms
In this section, I will assess my experiment design from the mechanism perspective, that is, whether my experiment design could explain the channels through which college reputation affects job application success rate.

Conceptually, one relative weakness of my experiment design is the I cannot directly test the hypothesis that "College reputation is a strong indicator of students' ability, thus employers will prefer students from colleges with better reputation" since I can only know whether the fake applications get some feedback.

To compliment the weakness of my experiment, I may need to further conduct a lab experiment. In the lab experiment, the invited experiment participants will be given three identical CVs (the only difference is college/ universities name). After that, they will be asked about which candidate they prefer to recruit and explain why. In this way, I could direct observe why college reputation matters and compliment the weakness of the online experiment I proposed.



### Reference
Katz, Lawrence F., and Kevin M. Murphy. "Changes in Relative Wages, 1963–1987: Supply and Demand Factors." The Quarterly Journal of Economics 107, no. 1 (1992): 35-78.
