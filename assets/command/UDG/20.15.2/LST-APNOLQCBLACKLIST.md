---
id: UDG@20.15.2@MMLCommand@LST APNOLQCBLACKLIST
type: MMLCommand
name: LST APNOLQCBLACKLIST（查询过载限速APN黑名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNOLQCBLACKLIST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 过载限速
- 过载限速控制APN黑名单
status: active
---

# LST APNOLQCBLACKLIST（查询过载限速APN黑名单）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询过载限速APN黑名单。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNOLQCBLACKLIST]] · 过载限速APN黑名单（APNOLQCBLACKLIST）

## 使用实例

查询过载限速APN黑名单：

```
LST APNOLQCBLACKLIST:;
```

```

RETCODE = 0  操作成功

结果如下
-----------------------
APN

testapn   
testapn1  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNOLQCBLACKLIST.md`
