import json

def generate_swagger():
    swagger = {
        "openapi": "3.0.1",
        "info": {
            "title": "OWASP crAPI API",
            "version": "1-oas3"
        },
        "externalDocs": {
            "description": "Completely Ridiculous API (crAPI)",
            "url": "https://github.com/OWASP/crAPI"
        },
        "servers": [
            {
                "url": "http://localhost:8888"
            }
        ],
        "paths": {
            "/identity/api/auth/signup": {
                "post": {
                    "operationId": "signup",
                    "summary": "Sign up",
                    "description": "Used to create an account",
                    "tags": ["Identity / Auth"],
                    "security": [],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "required": ["email", "name", "number", "password"],
                                    "properties": {
                                        "email": {"type": "string", "example": "Cristobal.Weissnat@example.com"},
                                        "name": {"type": "string", "example": "Cristobal.Weissnat"},
                                        "number": {"type": "string", "example": "6915656974"},
                                        "password": {"type": "string", "example": "5hmb0gvyC__hVQg"}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "User successfully registered",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/CRAPIResponse"}
                                }
                            }
                        },
                        "403": {
                            "description": "",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/CRAPIResponse"}
                                }
                            }
                        },
                        "500": {
                            "description": "",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/CRAPIResponse"}
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "CRAPIResponse": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string", "example": "success"},
                        "message": {"type": "string", "example": "User successfully registered"}
                    }
                }
            },
            "securitySchemes": {
                "digestAuth": {"type": "http", "scheme": "digest"},
                "bearerAuth": {"type": "http", "scheme": "bearer"},
                "basicAuth": {"type": "http", "scheme": "basic"},
                "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
                "jwtBearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"},
                "negotiateAuth": {"type": "http", "scheme": "negotiate"}
            }
        }
    }

    with open("swagger.json", "w") as file:
        json.dump(swagger, file, indent=2)
        print("Swagger file generated: swagger.json")

if __name__ == "__main__":
    generate_swagger()
