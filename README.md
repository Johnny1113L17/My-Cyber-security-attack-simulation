# 🛡 CyberSecurity Attack Simulation with Reinforcement Learning

這是一個結合「資訊安全」與「強化學習」的簡易模擬器，使用 Python + OpenAI Gym + Stable-Baselines3 建構。專案目的是訓練一個代理人（攻擊者）在簡化的資安環境中學習如何發現並利用漏洞進行攻擊。

---

##  專案目標與特色

-  結合資安攻擊流程與強化學習
-  自訂網路安全模擬環境 `CyberSecurityEnv`
-  使用 PPO（Proximal Policy Optimization）演算法訓練攻擊代理人
-  具備獎勵機制與攻擊策略演化觀察

---

##  環境設計：`CyberSecurityEnv`

自訂環境繼承自 `gym.Env`，模擬基本的網路攻擊流程：

- **觀察空間**：長度為 5 的整數向量（代表漏洞、防火牆狀態等）
- **動作空間**：3 種行動：
  - `0`：掃描漏洞
  - `1`：攻擊漏洞
  - `2`：橫向移動（嘗試擴展滲透）
- **獎勵設計**：
  - 掃描成功：+0.1
  - 攻擊成功：+1.0 並結束模擬
  - 攻擊失敗：-0.5
  - 無效橫向移動：-0.1

---

##  專案結構

# -CyberSecurityRL/
├── env.py              ← 自訂強化學習資安環境
├── main.py             ← 主程式：訓練 / 測試都在這
├── README.md           ← 專案說明與學習心得


---

##  使用方式

### 安裝必要套件
```bash
pip install stable-baselines3 gym

---

##  執行訓練

python main.py
# 輸入：train

