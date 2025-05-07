from kubernetes import client, config

def main():
    config.load_incluster_config()
    with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace") as f:
        namespace = f.read().strip()

    v1 = client.CoreV1Api()
    secrets = v1.list_namespaced_secret(namespace)

    print(f"Secrets in namespace '{namespace}':")
    for secret in secrets.items:
        print(f"- {secret.metadata.name}")

if __name__ == "__main__":
    main()

