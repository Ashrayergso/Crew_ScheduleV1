document.addEventListener('DOMContentLoaded', (event) => {
    // Function to handle assignment creation
    const createAssignment = () => {
        // Get form data
        const crewMemberId = document.getElementById('crewMemberId').value;
        const shipId = document.getElementById('shipId').value;
        const startDate = document.getElementById('startDate').value;
        const endDate = document.getElementById('endDate').value;
        const positionId = document.getElementById('positionId').value;

        // Create assignment object
        const assignment = {
            crewMember: crewMemberId,
            ship: shipId,
            startDate: startDate,
            endDate: endDate,
            position: positionId
        };

        // Send POST request to create assignment
        fetch('/assignments/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(assignment),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Assignment created successfully!');
            } else {
                alert('Failed to create assignment.');
            }
        });
    };

    // Add event listener to assignment creation button
    const createAssignmentButton = document.getElementById('createAssignmentButton');
    createAssignmentButton.addEventListener('click', createAssignment);

    // Function to handle automatic assignment
    const assignCrewToShips = () => {
        // Send GET request to trigger automatic assignment
        fetch('/assignments/assignCrewToShips/', {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Crew members assigned to ships successfully!');
            } else {
                alert('Failed to assign crew members to ships.');
            }
        });
    };

    // Add event listener to automatic assignment button
    const assignCrewToShipsButton = document.getElementById('assignCrewToShipsButton');
    assignCrewToShipsButton.addEventListener('click', assignCrewToShips);
});