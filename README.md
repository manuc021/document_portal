### Below command is for windows(CMD)
```
    mkdir <project_folder_name>
    cd <project_folder_name>
    code .
```

### For conda env setup
```
    conda create -p <env_name> python=3.10 -y
    conda activate <path_of_the_env>
    pip install -r requirements.txt
```

### Git commands(this commands is for the later uses)
```
    git init
    git add .
    git commit -m "<write your commit message>"
    git push
```

### Minimum requirement for this project ###
1. LLM Model ## grocq (freely), openai, gemini, claude, huggingface (freely)
2. Embedding model ## openai, hf, gemini
3. Vector DB ## In Memory , ##ondisk##, ## cloudbase (AWS Bedrock)