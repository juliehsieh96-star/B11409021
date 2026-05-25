# 台科大資管 Python 實作作業作答區

---

## 基本資料

學號： B11xxxxxx
系級： 資管系大一
姓名： 王小明

## 一、 原始碼分析報告 (Static Analysis) (20%)

### 變數與邏輯對照表


| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 a (in p_proc) | 將使用者輸入的字串依 / 分割後的欄位陣列 | X |
| Q2 b (in p_proc) | X | X |
| Q3 cate_dict | X | X |

### 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好

Q1： (範例：缺乏XXX，輸入XXX)

Q2： 

Q3： 

Q4：

Q5：

---

## 二、 Vibe-Coding 協作紀錄 (30%)

請記錄你如何引導 GitHub Copilot 進行重構。

### 1. 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A： ...

Prompt B： ...

Prompt C： ...
```

### 2. AI 錯誤處理

AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？

- 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)
- 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)

---

## 三、 成果驗證與測試 (30%)

確保你的 `refined_tracker.py` 功能正確。

1. 測試結果截圖 (Terminal)

>> 請貼在此處

請貼上執行程式並輸入 show 後，顯示資料清單的截圖（或文字紀錄）。

2. 產出的資料檔案格式

請貼上重構後生成的 records.json 前幾行內容：

```json
# 請貼在此處
```

## 四、 Git 提交紀錄 (Commit History) (20%)

請執行 git log --oneline 並將最近的 5 筆紀錄貼在此處，以證明你的開發流程。

```log
# 請貼在此處
```

請附上你的 GitHub Repository 連結：

```log
# 請貼在此處
```