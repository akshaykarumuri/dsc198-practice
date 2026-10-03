# dsc198-practice

Practice repository for DSC 198. It holds the Session 1 lab code and a folder for each week's solutions.

## Layout

| Path | Purpose |
|---|---|
| `hello.py` | A small `hello(name="world")` function |
| `test_hello.py` | Tests for `hello` |
| `week1/` to `week5/` | One folder per week for solutions |
| `.gitignore` | Ignores Python caches, virtual environments and editor files |

## Running the tests

Install pytest, then run it from the repository root:

    pip install pytest
    pytest

## Workflow

Work on a branch, commit, push, and open a pull request for review before merging into `main`:

    git switch -c my-branch
    git add .
    git commit -m "Describe the change"
    git push -u origin my-branch

After the pull request is merged, update your local copy:

    git switch main
    git pull

`git log --oneline --graph` shows the merge history.

## If a push is rejected

Your machine may have no SSH key, or the key may not be on your GitHub account. Generate one and add it:

    ssh-keygen -t ed25519 -C "your@email"
    cat ~/.ssh/id_ed25519.pub

Paste the output into GitHub under Settings, SSH and GPG keys, then push again.
