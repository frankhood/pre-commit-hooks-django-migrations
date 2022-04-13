=====
Usage
=====

To use pre-commit hooks django migrations in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pre_commit_hooks_django_migrations.apps.PreCommitHooksDjangoMigrationsConfig',
        ...
    )

Add pre-commit hooks django migrations's URL patterns:

.. code-block:: python

    from pre_commit_hooks_django_migrations import urls as pre_commit_hooks_django_migrations_urls


    urlpatterns = [
        ...
        url(r'^', include(pre_commit_hooks_django_migrations_urls)),
        ...
    ]
