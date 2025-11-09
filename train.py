import torch
import torchvision
import torchvision.transforms as transforms

num_epochs = 10
batch_size = 64
learning_rate = 0.001
img_size = 256

from constants import augmented_data_dir
from constants import model_dir


def train(device):
    transform = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor()
    ])

    train_dataset = torchvision.datasets.ImageFolder(augmented_data_dir, transform=transform)
    train_loader = torch.utils.data.DataLoader(
        dataset=train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=5)

    model = torchvision.models.resnet50()
    model = torch.nn.DataParallel(model)
    model = model.to(device)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        print(f'Epoch {epoch + 1}/{num_epochs} started.')
        loss = 0

        for inputs, labels in train_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(inputs)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}')

    torch.save(model.state_dict(), model_dir)


def main():
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    train(device)


if __name__ == '__main__':
    main()
