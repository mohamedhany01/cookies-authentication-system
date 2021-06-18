// A timer function with redirection feature
function timer(seconds_number, location) {

    let seconds = document.getElementById("seconds");

    if (seconds != null)
    {
        // Initialize seconds node
        seconds.innerText = seconds_number;

        let countDownTimer = setInterval(function () {

            // Convert to a Number
            let secondsNum = Number.parseInt(seconds.innerText);

            // Clear only if seconds became ZERO
            if (secondsNum <= 0)
            {
                // Clear and redirect
                clearInterval(countDownTimer);

                window.location.href = location;
            }
            else
            {
                // Decrement seconds number, every 1s
                seconds.innerText = secondsNum - 1;
            }
            
        }, 1000);
    }
}

// A function check if cookies are enabled or not and display a warning
function checkCookiesEnabled() {
    
    let isCookiesEnabled = navigator.cookieEnabled,
    cookiesStatus = document.querySelector(".cookies-status");

    if(!isCookiesEnabled)
    {
        cookiesStatus.innerText = "Warning: cookies aren't enabled, the application will not work correctly. Please enable cookies."
    }
}