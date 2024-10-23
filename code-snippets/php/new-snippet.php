<?php

add_action('wp_footer', 'my_custom_snippet_function');

function my_custom_snippet_function () {
    echo "Built with love by IlyesHaddad";
    
}