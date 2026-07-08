---
id: UNC@20.15.2@MMLCommand@LST M2MUPFBINDGRP
type: MMLCommand
name: LST M2MUPFBINDGRP（查询UPF和M2M关联的UPF组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M2MUPFBINDGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M关联的UPF组管理
status: active
---

# LST M2MUPFBINDGRP（查询UPF和M2M关联的UPF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询UPF和M2M关联的UPF组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD M2MUPGROUP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M2MUPFBINDGRP]] · UPF和M2M关联的UPF组的绑定关系（M2MUPFBINDGRP）

## 使用实例

查询UPF和UPF组的绑定关系：

```
%%LST M2MUPFBINDGRP: UPFGRPNAME="upfgrp1";%%
RETCODE = 0  操作成功

结果如下
--------
  UPF组名称  =  upfgrp1
UPF实例标识  =  upf_instance_1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-M2MUPFBINDGRP.md`
