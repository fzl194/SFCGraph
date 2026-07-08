---
id: UNC@20.15.2@MMLCommand@LST CDRGENRATECTRL
type: MMLCommand
name: LST CDRGENRATECTRL（查询话单产生速率）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRGENRATECTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 话单生成速率
status: active
---

# LST CDRGENRATECTRL（查询话单产生速率）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

LST CDRGENRATECTRL命令用来查询计费数据产生速率控制信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRGENRATECTRL]] · 话单产生速率（CDRGENRATECTRL）

## 使用实例

查询系统计费数据产生速率控制信息：

```
LST CDRGENRATECTRL:;
```

```

RETCODE = 0  操作成功。

话单产生速率控制
----------------
CDR产生速率（%）  =  50
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CDRGENRATECTRL.md`
