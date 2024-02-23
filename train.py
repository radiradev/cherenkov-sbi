from torch.utils.data import DataLoader
import torch
from dataset import H5Dataset
from model import Net

net = Net()
ds = H5Dataset()
dl = DataLoader(ds, batch_size=32, shuffle=True)

# Train the network
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(2):  # loop over the dataset multiple times
    
        running_loss = 0.0
        for i, data in enumerate(dl, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data
            # swap 0 and 1 dim of input
            inputs = inputs.unsqueeze(1)
    
            # zero the parameter gradients
            optimizer.zero_grad()
    
            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
    
            # print statistics
            running_loss += loss.item()
            if i % 20 == 19:    # print every 20 mini-batches
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

print('Finished Training')


