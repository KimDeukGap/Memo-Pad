import json, os

FILE = "memos.json"
memos = json.load(open(FILE, "r", encoding="utf-8")) if os.path.exists(FILE) else []

while True:
    print("\n--- [1] 메모 목록 [2] 메모 작성 [3] 메모 삭제 [4] 종료 ---")
    cmd = input("선택: ")
    
    if cmd == "1":
        if not memos:
            print("저장된 메모가 없습니다.")
        else:
            for i, m in enumerate(memos):
                print(f"{i+1}. {m}")
    elif cmd == "2":
        memo = input("메모 내용: ")
        memos.append(memo)
        json.dump(memos, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("메모가 저장되었습니다.")
    elif cmd == "3":
        idx = int(input("삭제할 메모 번호: ")) - 1
        if 0 <= idx < len(memos):
            removed = memos.pop(idx)
            json.dump(memos, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(f"메모가 삭제되었습니다: '{removed}'")
        else:
            print("존재하지 않는 번호입니다.")
    elif cmd == "4":
        break
