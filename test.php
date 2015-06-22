<?php

// Customize this (get ID/token values in your SmartyStreets account)
$authId = urlencode("AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ");

// Address input
$input1 = urlencode("jama masjid delhi");


// Build the URL
$req = "https://maps.googleapis.com/maps/api/geocode/json?address={$input1}&key={$authId}";

// GET request and turn into associative array
$result = json_decode(file_get_contents($req),true);

echo "<pre>";
print_r($result[geometry]);
echo "</pre>";

?>