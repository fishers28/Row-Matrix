const form = document.getElementById("workout-form");
const workoutList = document.getElementById("workout-list");
const workoutCount = document.getElementById("workout-count");
const totalDistance = document.getElementById("total-distance");

let workouts = JSON.parse(localStorage.getItem("rowMatrixWorkouts")) || [];

function displayWorkouts() {
    workoutList.innerHTML = "";

    let distanceSum = 0;

    workouts.forEach((workout) => {
        distanceSum += workout.distance;

        const item = document.createElement("li");
        item.textContent =
            `${workout.distance} meters in ${workout.duration} seconds`;

        workoutList.appendChild(item);
    });

    workoutCount.textContent =
        `Workouts completed: ${workouts.length}`;

    totalDistance.textContent =
        `Total distance: ${distanceSum} meters`;

    localStorage.setItem("rowMatrixWorkouts", JSON.stringify(workouts));
}

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const distance = Number(document.getElementById("distance").value);
    const duration = Number(document.getElementById("duration").value);

    if (!Number.isFinite(distance) || !Number.isFinite(duration)
        || distance <= 0 || duration <= 0) {
        alert("Please enter a valid distance and duration.");
        return;
    }

    workouts.push({
        distance: distance,
        duration: duration
    });

    displayWorkouts();
    form.reset();
});

displayWorkouts();