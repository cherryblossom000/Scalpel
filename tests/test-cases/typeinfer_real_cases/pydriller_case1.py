from pydriller.repository_mining import RepositoryMining


class ProcessMetrics():
    """
    This class is responsible to implement the following process metrics:

    - Commit Count - measures the number of commits made to a file
    """

    def commits_count(self, path_to_repo: str, filepath: str, commit_hash: str = None):
        """
        Return the number of commits made to a file from the first commit to the one identified by commit_hash.

        :path_to_repo: path to a single repo
        :commit_hash: the SHA of the commit to stop counting. If None, the analysis starts from the latest commit
        :filepath: the path to the file to count for. E.g. 'doc/README.md'

        :return: int number of commits made to the file
        """
        count = 0
        start_counting = commit_hash is None

        for commit in RepositoryMining(path_to_repo, reversed_order=True).traverse_commits():

            if not start_counting and commit_hash == commit.hash:
                start_counting = True

            # Skip commit if not counting
            if not start_counting:
                continue

            for modified_file in commit.modifications:
                if modified_file.filename == filepath:
                    count += 1

                    # Stop counting if the file has been created at the current commit
                    if not modified_file.old_path:
                        return count

                    # Else rename filepath with the older one (which can be the same)
                    filepath = modified_file.old_path

                    break

        return count