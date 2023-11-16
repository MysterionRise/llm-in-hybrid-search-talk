# llm-in-hybrid-search-talk
Code snippets and any useful materials from the talk LLM's Role in Modern Search Strategies


Creating a `README.md` section for explaining the usage of `pre-commit` can be quite helpful for developers working on your project. Here's a template you can use and adapt as needed:

---

### Using Pre-Commit

#### Introduction
[Pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks. It helps identify simple issues before submission to code review, ensuring code consistency and quality.

#### Installation

1. **Install pre-commit:**

   Ensure that you have Python installed on your system. Then, install `pre-commit` via pip:

   ```bash
   pip install pre-commit
   ```

   Alternatively, you can install `pre-commit` as part of our development dependencies from `requirements-dev.txt`:

   ```bash
   pip install -r requirements-dev.txt
   ```

   This file includes `pre-commit` and other development tools.

2. **Set up the pre-commit hook:**

   After installation, set up the pre-commit hooks in your local repository:

   ```bash
   pre-commit install
   ```

   This command will install the pre-commit script in your `.git/hooks/pre-commit`.

#### Configuration

- **`.pre-commit-config.yaml`:**

  This file contains the configuration for the hooks. You can customize which hooks to run and their parameters.

- **Updating Hooks:**

  To update the hooks to their latest versions, run:

  ```bash
  pre-commit autoupdate
  ```

  This command will update your configuration file with the latest versions of the hooks.

#### Usage

- **Run pre-commit on all files:**

  To manually run pre-commit on all files in the repository, use:

  ```bash
  pre-commit run --all-files
  ```

  This command is useful for running hooks on files that are not part of the current commit.

- **Run pre-commit on staged files:**

  Normally, pre-commit will run automatically on staged files during the `git commit` command. If you wish to manually check staged files, use:

  ```bash
  pre-commit run
  ```

#### Conclusion

Pre-commit is a powerful tool to ensure code quality and consistency. By following these steps, you can integrate it into your development workflow for a more efficient and error-free coding process.
