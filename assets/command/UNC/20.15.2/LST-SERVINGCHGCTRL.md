---
id: UNC@20.15.2@MMLCommand@LST SERVINGCHGCTRL
type: MMLCommand
name: LST SERVINGCHGCTRL（查询I-SMF/SGW的计费模式和CHF选择参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SERVINGCHGCTRL
command_category: 查询类
applicable_nf:
- SGW-C
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

# LST SERVINGCHGCTRL（查询I-SMF/SGW的计费模式和CHF选择参数）

## 功能

**适用NF：SGW-C、SMF**

该命令用于查询UNC作为I-SMF/SGW时的计费模式和CHF选择参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVINGCHGCTRL]] · I-SMF/SGW的计费模式和CHF选择参数（SERVINGCHGCTRL）

## 使用实例

查询UNC作为I-SMF/SGW时的计费模式和CHF选择参数：

```
%%LST SERVINGCHGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
拜访地用户QBC计费开关  =  打开QBC计费功能
归属地用户QBC计费开关  =  打开QBC计费功能
  漫游用户QBC计费开关  =  打开QBC计费功能
        用户主用CHF组  =  CHFGRP1
        用户备用CHF组  =  CHFGRP2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SERVINGCHGCTRL.md`
