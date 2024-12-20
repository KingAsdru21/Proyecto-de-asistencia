<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Asistencia</title>
    <script src="https://cdn.jsdelivr.net/npm/firebase@9.22.0/firebase-app.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/firebase@9.22.0/firebase-database.js"></script>
    <style>
        /* Agrega tus estilos aquí */
    </style>
</head>
<body>
    <h1>Lista de Asistencia</h1>
    <div id="attendance-list">
        <!-- Aquí se mostrarían los nombres y el estado -->
    </div>
    <div id="present-count">Personas presentes: 0</div>

    <script>
        // Configura Firebase
        const firebaseConfig = {
            apiKey: "YOUR_API_KEY",
            authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
            databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com",
            projectId: "YOUR_PROJECT_ID",
            storageBucket: "YOUR_PROJECT_ID.appspot.com",
            messagingSenderId: "YOUR_SENDER_ID",
            appId: "YOUR_APP_ID"
        };
        const app = firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        let attendanceData = {};

        // Función para cargar la lista de asistencia
        function loadAttendanceList() {
            const listRef = db.ref('attendance');
            listRef.on('value', (snapshot) => {
                attendanceData = snapshot.val();
                displayAttendanceList();
                updatePresentCount();
            });
        }

        // Función para mostrar la lista de asistencia
        function displayAttendanceList() {
            const listDiv = document.getElementById("attendance-list");
            listDiv.innerHTML = ""; // Limpiar lista anterior

            for (const name in attendanceData) {
                const status = attendanceData[name];
                const nameDiv = document.createElement("div");
                nameDiv.textContent = `${name}: ${status}`;
                const presentButton = document.createElement("button");
                presentButton.textContent = "Presente";
                presentButton.onclick = () => updateStatus(name, "Presente");

                const absentButton = document.createElement("button");
                absentButton.textContent = "Ausente";
                absentButton.onclick = () => updateStatus(name, "Ausente");

                nameDiv.appendChild(presentButton);
                nameDiv.appendChild(absentButton);
                listDiv.appendChild(nameDiv);
            }
        }

        // Función para actualizar el estado de presencia
        function updateStatus(name, status) {
            db.ref('attendance/' + name).set(status);
        }

        // Función para actualizar el contador de personas presentes
        function updatePresentCount() {
            const presentCount = Object.values(attendanceData).filter(status => status === "Presente").length;
            document.getElementById("present-count").textContent = `Personas presentes: ${presentCount}`;
        }

        // Cargar la lista de asistencia al inicio
        loadAttendanceList();
    </script>
</body>
</html>
