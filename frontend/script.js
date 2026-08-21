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
