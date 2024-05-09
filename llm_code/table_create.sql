
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    user_type ENUM('prompt_engineer', 'model_developer') NOT NULL,
    email VARCHAR(255) NOT NULL
    );

CREATE TABLE IF NOT EXISTS Prompts (
                                       prompt_id INTEGER PRIMARY KEY,
                                       prompt_text TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS metric_result (
    username VARCHAR(100) NOT NULL,
    metric_name VARCHAR(100) NOT NULL,
    prompt VARCHAR(100) NOT NULL,
    prompt_generation TEXT NOT NULL,
    metric_value FLOAT,
    model_id VARCHAR(100) NOT NULL
);