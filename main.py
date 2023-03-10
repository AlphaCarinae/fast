import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from enum import Enum

@strawberry.enum
class State(Enum):
    NSW = "NSW"
    QLD = "QLD"
    ACT = "ACT"
    WA = "WA"
    VIC = "VIC"
    TAS = "TAS"
    SA = "SA"
    NT = "NT"

@strawberry.type
class Address:
    number: str
    street: str
    city: int
    state: State
 
@strawberry.type
class Person:
    name: str
    email: str
    address: Address

mock_data = Person(name="Soheil",
        email="soheil@yahoo.com",
        address=Address(number=5,
            street="100 King Street",
            city="NewTown",
            state=State.NSW)
)

@strawberry.type
class Request:
    @strawberry.field
    def person(self) -> Person:
        return mock_data

schema = strawberry.Schema(query=Request)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

