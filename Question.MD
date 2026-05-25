# 台科大資管系大一程式設計實作任務: Python + VS Code + GitHub Copilot (11402)

> 專案名稱：遺留代碼重生計劃 (Legacy Code Rebirth)

## 1. 任務背景

你接手了一個由前輩開發的「簡易記帳系統」`messy_tracker.py` 。雖然該程式目前可以執行，但內部邏輯混亂、變數命名不明確，且缺乏現代軟體開發的架構。

你的任務是：利用 GitHub Copilot 作為協作對象，將這段「充滿味道」的程式碼進行分析、文件化，並重構成一個專業級的 Python 專案。

## 2. 素材

- 原始程式碼： `messy_tracker.py` 
- 測試資料： `input_test.txt` 裡面有可以複製的輸入資料，請用來多多測試程式執行正確

## 3. 實作任務與步驟

### 第一階段：代碼審核 (Code Audit)

1. 請在 VSCode 中開啟 `messy_tracker.py`。
2. 使用 GitHub Copilot Chat 功能分析程式碼。
3. 在 `ANSWER.md` 中完成「變數與邏輯對照表」，找出神祕變數 a, b, cate_dict 的真實商業意義。
4. 診斷出 5 個以上的「代碼壞味道」，並說明為何這些設計會造成維護困難。

### 第二階段：Vibe-Coding 重構 (Refactor)

1. 目標： 撰寫 refined_tracker.py。
2. 要求： 透過 Prompt 引導 Copilot 完成以下改動：
    - 模組化： 將功能拆解為類別 (Class) 或函式 (Function)。
    - 格式升級： 捨棄 txt 混亂格式，改用 json 格式儲存。
    - 強健性： 增加對使用者輸入與檔案讀取的錯誤處理 (Try-Except)。
    - 優化： 修正原程式每次新增資料都要存檔的低效率行為。
3. 紀錄： 在 `ANSWER.md` 紀錄你使用的 3 個關鍵 Prompt 以及 AI 出錯後的修正對話。

### 第三階段：版本控制 (Git & GitHub)

1. 在本地初始化 Git 倉庫，並建立 .gitignore 排除 `__pycache__` 等暫存檔。
2. 開發過程中需有 Commit，紀錄你的開發進度。
3. 將專案推送到 GitHub (Public)。

---

## 溫馨提示

Vibe-Coding 的核心在於 **「精準的溝通」**。如果你發現 AI 給的 code 還是很亂，請試著告訴它：「請參考 Clean 同學重構順利！
