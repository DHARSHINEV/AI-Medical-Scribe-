const transcriptBox =
    document.getElementById("transcript");

const soapBox =
    document.getElementById("soapNote");

const alertsBox =
    document.getElementById("alerts");

const entitiesBox =
    document.getElementById("entities");

const codingBox =
    document.getElementById("coding");


async function runDemo() {

    try {

        const response =
            await fetch("/api/demo");

        const data =
            await response.json();

        transcriptBox.value =
            data.transcript;

        displayResults(data);

    } catch (error) {

        alert(
            "Could not connect to backend. " +
            "Make sure the server is running."
        );

        console.error(error);
    }
}


async function analyzeTranscript() {

    const transcript =
        transcriptBox.value.trim();

    if (!transcript) {

        alert(
            "Please enter a transcript."
        );

        return;
    }


    try {

        const response =
            await fetch(
                "/api/analyze",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        transcript:
                            transcript
                    })
                }
            );


        const data =
            await response.json();

        displayResults(data);

    } catch (error) {

        alert(
            "Backend connection failed."
        );

        console.error(error);
    }
}


function displayResults(data) {

    const soap =
        data.soap;


    soapBox.innerHTML = 

        <div class="soap-section">

            <h3>Subjective</h3>

            <p>
                ${soap.subjective}
            </p>

        </div>


        <div class="soap-section">

            <h3>Objective</h3>

            <p>
                ${soap.objective}
            </p>

        </div>


        <div class="soap-section">

            <h3>Assessment</h3>

            <p>
                ${soap.assessment}
            </p>

        </div>


        <div class="soap-section">

            <h3>Plan</h3>

            <p>
                ${soap.plan}
            </p>

        </div>

    ;


    alertsBox.innerHTML = "";


    data.alerts.forEach(
        alert => {

            const div =
                document.createElement("div");

            div.className =
                alert ${alert.level};

            div.textContent =
                alert.message;

            alertsBox.appendChild(div);
        }
    );


    codingBox.innerHTML = 

        <hr>

        <h3>🏷 Coding Recommendation</h3>

        <p>
            <strong>ICD-10:</strong>
            ${soap.coding.icd10}
        </p>

        <p>
            <strong>CPT:</strong>
            ${soap.coding.cpt}
        </p>

        <p>
            <strong>Confidence:</strong>
            ${soap.coding.confidence}
        </p>

    ;


    displayEntities(data.entities);
}


function displayEntities(entities) {

    entitiesBox.innerHTML = "";


    const grid =
        document.createElement("div");

    grid.className =
        "entity-grid";


    Object.entries(entities).forEach(
        ([key, values]) => {

            const item =
                document.createElement("div");

            item.className =
                "entity-item";


            const title =
                document.createElement("strong");

            title.textContent =
                formatTitle(key);


            const value =
                document.createElement("span");

            value.textContent =
                values.length
                    ? values.join(", ")
                    : "Not detected";


            item.appendChild(title);

            item.appendChild(value);

            grid.appendChild(item);
        }
    );


    entitiesBox.appendChild(grid);
}


function formatTitle(text) {
        return text
        .replace(/_/g, " ")
        .replace(/\b\w/g,
            letter =>
                letter.toUpperCase()
        );
}


document
    .getElementById("demoButton")
    .addEventListener(
        "click",
        runDemo
    );


document
    .getElementById("analyzeButton")
    .addEventListener(
        "click",
        analyzeTranscript
    );
