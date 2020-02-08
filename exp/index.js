const k = `
Authentication: Done
Setup: 70% Done
Organization: 9th Aug, 2019
Instructors: 12th Aug, 2019
Learners: 15th Aug, 2019
Dashboard: 19th Aug, 2019
My courses: 27th Aug, 2019
Courses: 10th Sep, 2019
Discuss: 19th Sep, 2019
Settings: 1st Nov, 2019
Final delivery (testing, bug fixes, etc): 8th Nov, 2019`

const koya = [
    {name: 'Authentication', duration : 1, startDate: '', endDate: ''},
    {name: 'Setup', duration : 1, startDate: '', endDate: ''},
    {name: 'Organization', duration : 2, startDate: '', endDate: ''},
    {name: 'Instructors', duration : 3, startDate: '', endDate: ''},
    {name: 'Learners', duration : 2, startDate: '', endDate: ''},
    {name: 'Dashboard', duration : 6, startDate: '', endDate: ''},
    {name: 'My courses', duration : 10, startDate: '', endDate: ''},
    {name: 'Courses', duration : 7, startDate: '', endDate: ''},
    {name: 'Discuss', duration : 7, startDate: '', endDate: ''},
    {name: 'Settings', duration : 5, startDate: '', endDate: ''},
    {name: 'Final delivery (testing, bug fixes, etc)', duration : 7, startDate: '', endDate: ''},
];

const project = {
    id: 'meteor-id',
    name: 'project-name',
    startDate: new Date(),
    exclude: {
        byWeekDays: new Set(),
        byDate: []
    },
    sections: koya,
};

const weekDays = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

const getWeekDay = dayInt => {
    return weekDays[dayInt]
}

const excludeWeekDay = (weekday, project) => {
    project.exclude.byWeekDays.add(weekday);
}

const excludeDate = (date, project) => {
    // this needs more work to exclude days by months
    project.exclude.byDate.push(date);
}


const getEndDate = (startDate, days, weekDays, dates) => {
    // given a start, finish, and days to exclude
    // return the finish date and next start date
    let finishDate
        i = 0;
        tomorrow = startDate;

    while (i < days) {
        // tomorrow accummulates
        tomorrow.setDate(tomorrow.getDate() + 1)
        const weekday = getWeekDay(tomorrow.getDay());
        if (weekDays.has(weekday)  || dates.includes(tomorrow)) {
            // pass
        }
        else {
            finishDate = tomorrow;
            i++;
        }
    }
    return finishDate
};

const computeDates = (startDate, project) => {
    let start = startDate || new Date();
    const weekDays = project.exclude.byWeekDays;
    const dates = project.exclude.byDate;

    for (let section of project.sections) {
        section.startDate = new Date(start);
        const finish = getEndDate(start, section.duration, weekDays, dates);
        section.endDate = finish;
        start = new Date(finish);
    };
    return project
};


excludeWeekDay('Saturday', project);
excludeWeekDay('Sunday', project);

const computed = computeDates(null, project)

// console.log(getWeekDay(new Date().getDay()))
// console.log('Koya', koya)
// console.log(c.sections)
