---
name: skill-pytorch-patterns
description: Padrões de referência para a formação, avaliação e implantação do PyTorch
version: 1.0.0
phase: 03
lesson: 11
tags: [pytorch, training, deep-learning, gpu, patterns]
---

## Loop de Treinamento Canônico

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Model().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)

for epoch in range(num_epochs):
    model.train()
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

    model.eval()
    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
```

## Treinamento Misto de Precisão

```python
from torch.amp import autocast, GradScaler

scaler = GradScaler()
for inputs, targets in train_loader:
    inputs, targets = inputs.to(device), targets.to(device)
    optimizer.zero_grad()
    with autocast(device_type="cuda"):
        outputs = model(inputs)
        loss = criterion(outputs, targets)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

Utilize quando: treinamento em GPU com hardware com capacidade para float16 (V100, A100, H100, RTX 3090+).

## Acumulação gradual

```python
accumulation_steps = 4
optimizer.zero_grad()
for i, (inputs, targets) in enumerate(train_loader):
    inputs, targets = inputs.to(device), targets.to(device)
    outputs = model(inputs)
    loss = criterion(outputs, targets) / accumulation_steps
    loss.backward()
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

Utilize quando: tamanho de lote efetivo precisa ser maior do que a memória da GPU permite. Dividir a perda por accumulation_steps mantém a escala de gradiente consistente.

## Salvar e carregar

```python
torch.save({
    "epoch": epoch,
    "model_state_dict": model.state_dict(),
    "optimizer_state_dict": optimizer.state_dict(),
    "loss": loss.item(),
}, "checkpoint.pt")

checkpoint = torch.load("checkpoint.pt", weights_only=True)
model.load_state_dict(checkpoint["model_state_dict"])
optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
```

Salva sempre o estado do optimizador para retomar o treinamento. `model.state_dict()`- Não .

## Set de dados personalizados

```python
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data_dir, transform=None):
        self.samples = self._load_samples(data_dir)
        self.transform = transform

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        x, y = self.samples[idx]
        if self.transform:
            x = self.transform(x)
        return x, y

    def _load_samples(self, data_dir):
        ...
```

## Configuração do DataLoader

```python
train_loader = torch.utils.data.DataLoader(
    dataset,
    batch_size=64,
    shuffle=True,
    num_workers=4,
    pin_memory=True,
    drop_last=True,
    persistent_workers=True,
)
```

| Parameter | What it does | When to use |
|-----------|-------------|-------------|
| num_workers=4 | Parallel data loading | Always on multi-core machines |
| pin_memory=True | Page-locked CPU memory | When training on GPU |
| drop_last=True | Drop incomplete final batch | When using BatchNorm |
| persistent_workers=True | Keep workers alive across epochs | When num_workers > 0 |

## Horários de aprendizagem

```python
scheduler = torch.optim.lr_scheduler.OneCycleLR(
    optimizer,
    max_lr=1e-3,
    total_steps=num_epochs * len(train_loader),
    pct_start=0.1,
)

for epoch in range(num_epochs):
    for inputs, targets in train_loader:
        ...
        optimizer.step()
        scheduler.step()
```

OneCycleLR: melhor padrão para a maioria das tarefas. aquece até max_lr, então cosino decompõe. `scheduler.step()` Depois de cada lote, não de cada época.

## Inicialização do peso

```python
def init_weights(module):
    if isinstance(module, nn.Linear):
        nn.init.kaiming_normal_(module.weight, nonlinearity="relu")
        if module.bias is not None:
            nn.init.zeros_(module.bias)
    elif isinstance(module, nn.Conv2d):
        nn.init.kaiming_normal_(module.weight, mode="fan_out", nonlinearity="relu")

model.apply(init_weights)
```

## Modo de inferência

```python
model.eval()

with torch.inference_mode():
    outputs = model(inputs)
```

`torch.inference_mode()` é mais rápido do que `torch.no_grad()` Porque desativa o autogrado inteiramente, em vez de apenas suprimir o cálculo de gradientes.

## Lista de erros comuns

1. Aplicação de softmax antes de CrossEntropyLoss (inclui log_softmax internamente)
2. Esquecer de ligar para model.eval() durante a validação
3. Esquecer de mover tensores para o mesmo dispositivo que o modelo
4. Não chamando optimizer.zero_grad() (gradientes acumulam-se por padrão)
5. Usar torch.no_grad() durante o treinamento (desativar cálculo de gradiente)
6. Colocar num_workers muito alto (desperta muitos processos, destrói a memória)
7. Não usar pin_memory=True quando se treina em GPU
8. Salvar todo o objeto modelo em vez de state_dict (rupturas no refactor)
