In this step the main goal is to integrate required apis, make clock widget functional and change background image based on current time.

## What will you do?

1.  Make a fetch api call to `https://ipv6.jsonip.com/`. It will return a response something like this

    ```json
    {
      "ip": "2405:201:400f:d1a0:55be:921f:a1ec:8080",
      "geo-ip": "https://getjsonip.com/#plus",
      "API Help": "https://getjsonip.com/#docs"
    }
    ```

2.  Use the `ipv6` response to get user location. Make api call to `https://geolocation-db.com/json/2405:201:400f:d1a0:55be:921f:a1ec:8080`. It will return a response something like this

    ```json
    {
      "country_code": "IN",
      "country_name": "India",
      "city": "Noida",
      "postal": "201301",
      "latitude": 28.57,
      "longitude": 77.32,
      "IPv4": "2405:201:400f:d1a0:55be:921f:a1ec:8080",
      "state": "Uttar Pradesh"
    }
    ```

You can also use [Geolocation api](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) to get the user's location which is more precise but require user's consent.

3.  Create a function to set current hours minutes and other required data to state. To call this function you can either use `setInterval` or `requestAnimationFrame`. If you use setInterval make sure to clear Interval on component unmount.

4.  Change greeting message based on current hour using a map like this.

    ```javascript
    const GREETING_TEXT = new Map([
      [22, "Working Late"],
      [18, "Good Evening"],
      [12, "Good Afternoon"],
      [6, "Good Morning"],
      [0, "Whoa, Early Bird"],
    ]);
    ```

5.  To change the background dynamically we can use `css variable` and change the variable value using inline styling and calling the callback function every hour.

We have completed the Clock widget and now date time, greeting message and background should change dynamically based on current date and time.
