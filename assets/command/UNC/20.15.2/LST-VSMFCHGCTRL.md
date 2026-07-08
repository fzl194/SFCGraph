---
id: UNC@20.15.2@MMLCommand@LST VSMFCHGCTRL
type: MMLCommand
name: LST VSMFCHGCTRL（查询V-SMF的计费模式和CHF选择参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VSMFCHGCTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费控制
status: active
---

# LST VSMFCHGCTRL（查询V-SMF的计费模式和CHF选择参数）

## 功能

**适用NF：SMF**

该命令用于查询UNC作为V-SMF时的计费模式和CHF选择参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [V-SMF的计费模式和CHF选择参数（VSMFCHGCTRL）](configobject/UNC/20.15.2/VSMFCHGCTRL.md)

## 使用实例

查询UNC作为V-SMF时的计费模式和CHF选择参数：

```
%%LST VSMFCHGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
         计费模式  =  QBC计费
      CHF选择模式  =  Local
拜访用户主用CHF组  =  CHFGRP1
拜访用户备用CHF组  =  CHFGRP2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询V-SMF的计费模式和CHF选择参数（LST-VSMFCHGCTRL）_25328709.md`
