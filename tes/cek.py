import torch
import intel_extension_for_pytorch as ipex

print("-" * 30)
print("Sedang memeriksa GPU Intel Arc...")

if torch.xpu.is_available():
    print(f"✅ GPU DETECTED: {torch.xpu.get_device_name(0)}")
    print(f"✅ Driver Info : {torch.xpu.get_device_properties(0).driver_version}")
else:
    print("❌ GPU Tidak Terdeteksi")
print("-" * 30)