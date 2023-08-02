from prefect import flow, task

name_list = ["Marvin", "Ford", "Arthur"]

@task(log_prints=True)
def say_hello(name: str):
    print(f"Hello {name}!")


@flow
def hello_universe(names=name_list):
    for name in names:
        say_hello(name)

if __name__ == "__main__":
    hello_universe(names=name_list)