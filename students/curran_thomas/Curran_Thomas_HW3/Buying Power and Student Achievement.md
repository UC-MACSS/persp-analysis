## Buying Power and Student Achievement: *experimental design*

Tom Curran
MACS 30000
October 30, 2017

### Introduction:

In the previous two assignments, I proposed an observational study and survey using the financial reports published by the Oklahoma State Department of Education, which was then compiled into a MySQL database by the non-profit education group the Oklahoma Public School Resource Center. These reports offered detailed record of school district revenues and expenditures and as such, have acted as a pivotal source of information for the ongoing debate over school funding throughout the state of Oklahoma.

Currently, the debate over school funding boils down to whether rural school districts (called Independent districts) should continue to receive special revenues from taxes, these revenue line items are called gross production tax and motor vehicle tax. The argument against these additional revenues is that those school districts can spend more money on resources and talent (i.e. better teachers). The pro side of the argument says that since these Independent school districts are rural and therefore lack other forms of revenue that are seen in suburban and urban school districts, it is simply leveling the playing field. 

For the observational study, I proposed using the MySQL database created by OPSRC to understand, and possibly predict, the outcomes of independent and dependent school districts on the A-F report card. Using a survey methodology, the observational study was enhanced using enriched asking and capturing the qualitative data about a school that revenue, expenditures and financial statements cannot express. Though both methods offer important insights and utility into understanding the impact of motor vehicle and gross production tax’s impact on school performance, it has ultimately failed to reveal what Salganik calls a ‘mechanism’ for which student performance is increased. 

Using the experimental designs put forth in Bit by Bit, we can more deeply understand what is enabling increases in student performance and if that mechanism doing the enabling is at all related to the gross production and motor vehicle tax

### Research Question:

Do increases in school revenues, effectively increasing a school district’s “buying power”, result an increase in student achievement and performance on the Oklahoma State Department of Education A – F School Report Card from the previous year?
### Experimental Design:

Each teacher would receive a curriculum and set of classroom tablets for their students. The teachers would be given a yearlong curriculum that aligned with the state standards in each subject. The curriculum would include worksheets, age appropriate reading materials, as well as materials for lessons in math. These curriculum materials would also cover science and history, but focus primarily on reading and math as it more closely reflects the current policy environment. The materials would correspond to weekly assessments that tested the skills that the state standards were targeting (i.e. Reading comprehension, math skills). At the end of each week students would take the assessment and their scores would be captured via the tablet. Each student would have their own log in or identifier (for example using Touch ID on an IPad) that allowed for capturing information beyond the assessment. Information such as demographic, Free and Reduced Lunch status, disciplinary record and classroom accommodation information would be linked to each individual student to slice and analyze the assessment results. 

The treatment group is to be given a visa gift card for purchasing materials. The teachers are free to purchase whatever materials that they believe are necessary for successfully teaching the week or unit’s material. This could range from pencils to enrichment activities like science projects and more. The teachers’ spending would be tracked via the typical online portal offered by visa gift cards for data collection as well as to ensure that the teachers were not using the money for personal items or items outside the scope of the classroom or experiment (i.e. food, clothing). 

**Stage 1: Identifying Participants and Recruitment**

Using the OPSRC MySQL database, we create a list of independent and dependent school districts and their schools. This list would also contain metrics of student and teacher demographics, average property value, teacher experience information, student-teacher ratio, and Free and Reduced Lunch percentage (an indicator of poverty). For this experiment, we would use only elementary schools, and focus on third grade. Third grade classrooms are typically self-contained (i.e. 1 teacher for multiple subjects) as well as a pivotal testing year based on current education policy in the state (see ‘Reading Sufficiency Act’). Based on this information we would create different strata of schools based on different properties. For example, stratum that contain similar percentages of Free and Reduced Lunch student would allow for controlling for the effects of poverty in a school. While poverty is a pivotal factor in education, it is outside the scope of the experiment because we are not necessarily testing for the impact of poverty on education. This aggregated and stratified list would provide a starting point for recruitment of participants.

Pending the initial approval of the experiment by the various levels within the school district (i.e. Superintendent), we would contact the teachers in the list to ask if they were interested in participating in our experiment.

**Stage 2: Randomization**

Once recruited, participating teachers would be sorted randomly into a treatment and control group via a randomization algorithm in Python (or R). Since we have filtered the list and controlled for several variables in the initial recruitment, the treatment indicator should allow for sufficient control in the experiment. Furthermore, using Python (or R) allows for true randomization. It is possible that teachers with similar unobservable traits are selected for either treatment or control, but given that our sample is large enough (which it should be) than it is less of a concern. 

**Stage 3: Delivery of Treatment**

Both treatment and control would be given curriculum materials, and a tablet that contain weekly assessments of lesson plans as well as one final assessment. The assessment would be delivered via tablet in order to capture meta-data as well as measure learning outcomes for students. 

The treatment group would be given a visa gift card with a fixed amount of money each semester. This visa gift card can only be used for educational materials or professional purposes (i.e. attend professional development session). The visa gift card accounts would be monitored by the research team to make sure that expenditures were being spent on goods for the classroom (and not on personal business) as well as categorize types, frequency and quality of purchases. 

**Stage 4: Measurement of Outcomes**

Using the tablets administered to both treatment and control groups, we would measure the outcomes of the assessments at the end of each semester. Furthermore, we would use the meta-data and financial records captured in the process to understand and analyze the “mechanism” in the experiment.  

### Assessment of Experimental Design:

**Ethical and Fiscal Concerns**

The merit of this experimental design is outweighed by the ethical, fiscal and logistical costs. First, I do not believe it to be an ethical option to deny enhanced education to some students but not others. The reality of this experiment is that many of the targeted schools already lack resources needed to provide even the most basic education, so widening that gap could potentially prove very harmful. Furthermore, since we target third grade classrooms there are long lasting implications to the individual student’s education future. If somehow the experiment impeded a student’s ability to pass their end-of-year reading test via the Reading Sufficiency Act in Oklahoma, then they would be forced to be held back for another year. Furthermore, using unique identifiers via Touch ID on an iPad raises serious security concerns. While collecting and storing student information raises serious privacy concerns. These concerns, especially since they are being collected by a third party, make the experiment ethically dubious at best. 

Second, the financial cost of the experiment is very high. To develop a curriculum and purchase enough iPad or other digital mediums to scale the experiment for accuracy is both extremely expensive and time intensive. 

**Validity**

Despite controlling for factors like poverty (via Free and Reduced Lunch), student teacher ratio and more, the experiment fails to capture and control for a teacher’s innate ability. The reality of the classroom is that years of experience does not necessarily result in better teaching. Furthermore, composure of classrooms is almost always random where a classroom could receive a disproportionately high amount of special ed students, or students that require services beyond what is considered ‘normal’. The classroom makeup and the unaccounted for social dynamics between teachers and students, and intra-student dynamics, are all threats to internal validity that would be extremely hard to control for. Even if they could be controlled for it would have intense spillover effects with non-participating classrooms in the school. For those characteristics that can be measured, we would check for balance using typical balance checks (i.e. T-test). 

While the internal validity is questionable, the external validity, or generalizability, are adequate. As such, if the experiment was presented to another teacher, policy maker or school administrator, they could easily see how the results could be applied to their school. Especially since the experiment tracks and categorized the purchases, we can draw a line between that resource and that week or unit’s goals. For the policy maker, the experiment can demonstrate the impact of funding laws, and for the school administrator the results can be generalized to resource allocation. The external validity arises because we controlled for several variables as well as stratified the results. The emphasis on external validity was chosen over internal validity because things like teacher and student motivation, teacher ability, and social dynamics are extremely difficult to control for. 

**Heterogeneity of Treatment Effects**

Where this experiment does have merit is the heterogeneity of treatment effects. The nature of elementary (i.e. 3rd grade classrooms) is that each student is inherently different in behavior, learning style and ability. We can forgo the average treatment effect because the average treatment effect essentially sacrifices the uniqueness of each student. By collecting the information like learning disabilities, disciplinary records and more, the experiment can help refine the impact of buying power on achievement for certain types of students. For example, buying power may have a neutral effect on students with no learning disabilities, while have more buying power results in a marked improvement of achievement for special education students. While the ethics of collecting this information are questionable, the merit of its potential analytic insight cannot be ignored.

**Causal Mechanisms**

As mentioned previously, this experiment does not measure unobservable characteristics like teacher ability and classroom social dynamics. Being unable to identify or measure such unobservable characteristics makes identifying a clear mechanism for success difficult. While the mechanism can be strongly indicated, we cannot entirely attribute success to buying power. 

**Relationship to Observational Studies and Surveys**

While this experiment would be extremely interesting from an economic or policy stance, I do not think it would be enough to outweigh the ethical or practical concerns. Collecting and storing student information is extremely sensitive, akin to healthcare data, and influencing a student’s opportunity to learn is unethical. Practically speaking, teachers would have a hard time following the curriculum as provided given different teaching styles. From a usefulness standpoint, the experiment is more useful than the survey as it offers a clearer relationship between student success and buying power.  For those threats to internal validity, I believe the observational study would be better than an experiment. Furthermore, given the detailed records of school district financial statements, an observational study would be more than sufficient to infer the relationship between student achievement and buying power. 