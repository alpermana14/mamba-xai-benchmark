set -e
cd ~
rm -rf ~/venv_opsA
if sudo -n true 2>/dev/null; then
  sudo -n apt-get install -y -q python3.12-venv >/dev/null 2>&1 && echo "apt venv installed" || echo "apt failed"
fi
if python3 -m venv ~/venv_opsA 2>/dev/null; then
  echo "venv with pip"
else
  python3 -m venv --without-pip ~/venv_opsA
  curl -sS https://bootstrap.pypa.io/get-pip.py -o ~/get-pip.py
  ~/venv_opsA/bin/python ~/get-pip.py -q
  echo "venv bootstrapped with get-pip"
fi
source ~/venv_opsA/bin/activate
pip install -q --upgrade pip
pip install -q torch==2.10.0 --index-url https://download.pytorch.org/whl/cu130
pip install -q "https://github.com/state-spaces/mamba/releases/download/v2.3.2.post1/mamba_ssm-2.3.2.post1+cu13torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl"
pip install -q numpy pandas scikit-learn scipy matplotlib einops tqdm shap
python - <<'PY'
import torch, mamba_ssm
print("torch", torch.__version__, "cuda", torch.cuda.is_available(), torch.cuda.get_device_name(0))
from mamba_ssm import Mamba
m = Mamba(d_model=16, d_state=2, d_conv=2, expand=1).cuda()
x = torch.randn(2, 10, 16, device="cuda", requires_grad=True)
y = m(x); y.sum().backward()
print("mamba forward/backward ok", tuple(y.shape), x.grad is not None)
PY
echo SETUP_DONE
