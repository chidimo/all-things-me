# Onyinye

## Notes

Registration requires email, password and twitter handle.

## Features

1. A screen to show monthly beneficiaries filtered year
1. A screen to show all users
1. Click on user to see info

## Instructions on how to receive

1. Search for a course you like on vendor (e.g. Udemy)
1. Email the link to organizer
1. Wait for your course to be gifted to you
1. After finishing the course, login to your account
1. Select the course, and mark it completed

## Object structures

```javascript
// user
const user = {
    email,
    password,
    twitter,
    courses: [],
    isadmin: false,
    giftedthisyear: false,
};

const users = [];

// course
const course = {
    name, author, url, vendor, receiveddate, language, framework, completed
};

const courses = [];
```

## Functions

```javascript
const selectWinner = users => {
    let users = users.filter(user => (user.giftedthisyear === false))
    // send notification email with instructions
    // randomly select a user
};

const giftCourse = (user, course) => {
    user.giftedthisyear = true;
    user.courses.push(course)
    // save
};

const reset = users => {
    // Admin to do this once every year or as needed
    // Include some confirmation

    const today = new Date();
    // filter out users with uncompleted courses

    let users = users.filter(user => {
        let completedall = true;
        for (let course in user.courses) {
            if (course.completed === false) {
                completedall = false;
            }
        }
        return completedall;
    })

    for (let user of users) {
        user.giftedthisyear = false;
        // save
    }
}

const reportCompleted = course => {
    course.completed = true;
    // save
}

const addCourse = (name, author, url, vendor, receiveddate, language, framework, completed) => {

    // add course to database

}
```
