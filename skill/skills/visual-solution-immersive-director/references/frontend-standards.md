# 共用切版規範｜獨立 Lin-EVO 與 Miffy-EVO

本方案只維護設計流程，不複製 Lin／Miffy 的工程條文。依當前工具已安裝／啟用的 Skill 定位來源；本機實際資料夾與安裝管理見本 repo 的 `skill/INSTALL.md`。

1. 切版、修改與校稿讀 Lin-EVO；靜態網站轉 EVO 讀 Miffy-EVO，完整讀取當次入口及必要 references。
2. 核對各自安裝紀錄的 source、skill_path、連結／複製模式，以及來源管理資料夾的 skill-sources.json（若有）。source 是安裝器位置，不保證 Skill 在其子資料夾。已安裝的有效連結直接讀取，不重新複製或把另一個 Skill 搬回去。
3. 本機目前 Lin 位於 lin-skill/Lin-EVO，Miffy 位於外層 Miffy-EVO；部分拆分配置的舊整包 Git 更新已停用。先讀本機實際版本，明列未確認遠端最新版，不執行舊 --update，也不以 workflow 自己的 Git 更新成功代表 Lin／Miffy 已更新。其他未拆分配置或未來有獨立 Git 來源時，才依該安裝的規範安全更新；保留本機修改與分歧，不 reset／stash。Miffy 的 evomni-html 仍由人工更新。
4. 缺少本輪需要的 Skill 時，依 [Skill 依賴與安裝](skill-dependencies.md) 從已確認的實際來源安裝；不讀歷史副本冒充最新版。無本機能力時使用已啟用的上傳版，不能宣稱已安裝或已讀本機檔案。
5. 本方案的方向、母版、角色、動態範圍、RWD 與確認節點仍有效。Lin 只提供工程規範；Miffy 接續轉換，不重新提案。真正衝突列來源及影響，缺契約不猜。
6. 交付分開列靜態驗證、客戶確認、工程師接入、後台儲存與發布驗證。
